import csv
import glob
import os
import random
from io import BytesIO

import qrcode
import streamlit as st

from ctet_questions import QUESTIONS as PY_QUESTIONS, SECTIONS


# ---------------------------------------------------------------------------
# Load questions from any CSV files in this folder (e.g. ctet_questions.csv).
# CSV columns: paper, section, question, option_A, option_B, option_C,
#              option_D, correct (A/B/C/D), explain
# This lets you add questions in a spreadsheet instead of editing Python.
# ---------------------------------------------------------------------------
def load_csv_questions():
    loaded = []
    here = os.path.dirname(os.path.abspath(__file__))
    for path in glob.glob(os.path.join(here, "*.csv")):
        if os.path.basename(path) == "ctet_template.csv":
            continue  # skip the example template
        try:
            with open(path, newline="", encoding="utf-8-sig") as f:
                for row in csv.DictReader(f):
                    letter = (row.get("correct") or "").strip().upper()
                    idx = {"A": 0, "B": 1, "C": 2, "D": 3}.get(letter)
                    if idx is None:
                        continue  # skip rows with a missing/bad answer letter
                    options = [
                        (row.get("option_A") or "").strip(),
                        (row.get("option_B") or "").strip(),
                        (row.get("option_C") or "").strip(),
                        (row.get("option_D") or "").strip(),
                    ]
                    if not all(options) or not (row.get("question") or "").strip():
                        continue  # skip incomplete rows
                    loaded.append({
                        "paper": (row.get("paper") or "Paper 1").strip(),
                        "section": (row.get("section") or "").strip(),
                        "question": row["question"].strip(),
                        "options": options,
                        "answer": idx,
                        "explain": (row.get("explain") or "").strip(),
                    })
        except Exception:
            pass  # a malformed CSV shouldn't crash the app
    return loaded


# Combine Python-file questions with any CSV questions
QUESTIONS = list(PY_QUESTIONS) + load_csv_questions()

# =========================================================
# CONFIG
# =========================================================
FREE_QUESTION_LIMIT = 3          # free questions before paywall

# UPI payment details
YOUR_UPI_ID = "harjeet.pahwa@oksbi"
MERCHANT_NAME = "CTET Practice"
PREMIUM_PRICE_INR = "99"         # launch offer (regular 199)

# Paid-customer unlock codes -- add one line per paying customer
UNLOCK_CODES = [
    "CTET-DEMO-2026",            # example / your own test code
    # "CTET-RAVI-2026",         # <- add a line like this for each paid customer
]

WHATSAPP_NUMBER = "91XXXXXXXXXX"  # <-- replace with your WhatsApp number, keep 91 prefix

# =========================================================
# PAGE + HEADER
# =========================================================
st.set_page_config(page_title="CTET Practice", page_icon="📝", layout="centered")

st.markdown("""
<style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    .ctet-header {
        background: linear-gradient(90deg, #4f46e5 0%, #7c3aed 50%, #2563eb 100%);
        padding: 22px 26px; border-radius: 14px; margin-bottom: 22px;
        box-shadow: 0 8px 24px rgba(79,70,229,0.25);
        display: flex; align-items: center; gap: 14px;
    }
    .ctet-header h1 { color: white; margin: 0; font-size: 28px; font-weight: 800; }
    .ctet-header p { color: #e0e7ff; margin: 2px 0 0 0; font-size: 14px; }
    .ctet-icon { font-size: 40px; line-height: 1; }
</style>
<div class="ctet-header">
    <div class="ctet-icon">📝</div>
    <div>
        <h1>CTET Practice</h1>
        <p>Paper 1 &amp; Paper 2 — practice questions with instant answers</p>
    </div>
</div>
""", unsafe_allow_html=True)

# =========================================================
# SESSION STATE
# =========================================================
defaults = {
    "answered_count": 0,      # how many questions answered (free counter)
    "score": 0,               # correct answers
    "has_paid": False,
    "current_q": None,        # the question dict being shown
    "answered_current": False,
    "selected_paper": None,
    "selected_section": None,
    "seen_indexes": [],       # to avoid repeats
    "chosen_index": None,     # which option the user picked for the current question
}
for k, v in defaults.items():
    if k not in st.session_state:
        st.session_state[k] = v


# =========================================================
# HELPERS
# =========================================================
def get_pool(paper, section):
    return [q for q in QUESTIONS if q["paper"] == paper and q["section"] == section]


def pick_question(paper, section):
    pool = get_pool(paper, section)
    # indexes not yet seen
    remaining = [i for i, q in enumerate(pool) if i not in st.session_state.seen_indexes]
    if not remaining:
        # all seen -> reset so they can loop again
        st.session_state.seen_indexes = []
        remaining = list(range(len(pool)))
    if not remaining:
        return None
    idx = random.choice(remaining)
    st.session_state.seen_indexes.append(idx)
    return pool[idx]


def upi_qr_png():
    clean_name = MERCHANT_NAME.replace(" ", "%20")
    upi_link = f"upi://pay?pa={YOUR_UPI_ID}&pn={clean_name}&am={PREMIUM_PRICE_INR}&cu=INR"
    qr = qrcode.QRCode(version=1, box_size=10, border=2)
    qr.add_data(upi_link)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    buf = BytesIO()
    img.save(buf, format="PNG")
    return upi_link, buf.getvalue()


# =========================================================
# 1. PAPER + SECTION SELECTION
# =========================================================
st.subheader("Choose what to practice")

col_a, col_b = st.columns(2)
with col_a:
    paper = st.selectbox("Paper", list(SECTIONS.keys()),
                         index=0 if st.session_state.selected_paper is None
                         else list(SECTIONS.keys()).index(st.session_state.selected_paper))
with col_b:
    section = st.selectbox("Section", SECTIONS[paper])

# If the user changed paper/section, reset the current question
if paper != st.session_state.selected_paper or section != st.session_state.selected_section:
    st.session_state.selected_paper = paper
    st.session_state.selected_section = section
    st.session_state.current_q = None
    st.session_state.answered_current = False
    st.session_state.seen_indexes = []

pool = get_pool(paper, section)
st.caption(f"{len(pool)} question(s) available in this section. "
           f"Score so far: {st.session_state.score} / {st.session_state.answered_count}")

st.divider()

# =========================================================
# 2. PAYWALL CHECK
# =========================================================
reached_limit = (
    st.session_state.answered_count >= FREE_QUESTION_LIMIT
    and not st.session_state.has_paid
)

if reached_limit:
    st.warning(f"You have completed your {FREE_QUESTION_LIMIT} free questions.")

    upi_link, qr_bytes = upi_qr_png()
    st.markdown(
        f"""
        <div style="background:#f8fafc; padding:22px; border-radius:14px;
                    border:2px solid #e2e8f0; text-align:center; margin-bottom:16px;">
            <h3 style="color:#4338ca; margin-bottom:4px;">Unlock Unlimited Practice 💎</h3>
            <p style="color:#475569; font-size:15px;">Launch offer:
               <span style="text-decoration:line-through; color:#94a3b8;">₹199</span>
               <b style="color:#4338ca;">₹{PREMIUM_PRICE_INR}</b> — one-time, unlimited questions.</p>
            <a href="{upi_link}" style="background:#4f46e5; color:white; padding:12px 24px;
               text-decoration:none; border-radius:8px; font-weight:bold; display:inline-block;">
               Pay via Google Pay / PhonePe / UPI</a>
        </div>
        """,
        unsafe_allow_html=True,
    )

    c1, c2, c3 = st.columns([1, 2, 1])
    with c2:
        st.image(qr_bytes, caption="Scan with any UPI app to pay", use_container_width=True)
        st.markdown(
            f"""<div style="text-align:center; color:#475569; font-size:14px; margin:8px 0 14px 0;">
            After paying <b>₹{PREMIUM_PRICE_INR}</b>, send your payment screenshot on WhatsApp to
            <b>{WHATSAPP_NUMBER}</b> to receive your <b>unlock code</b>.</div>""",
            unsafe_allow_html=True,
        )
        code = st.text_input("Enter your unlock code", type="password")
        if st.button("Unlock Access"):
            if code.strip().upper() in [c.strip().upper() for c in UNLOCK_CODES]:
                st.session_state.has_paid = True
                st.success("Unlocked! Enjoy unlimited practice.")
                st.rerun()
            else:
                st.error("Incorrect code. Please check the code sent to you after payment.")

# =========================================================
# 3. QUIZ INTERFACE
# =========================================================
else:
    if len(pool) == 0:
        st.info("No questions in this section yet. Add some to ctet_questions.py")
    else:
        # get a question if we don't have one
        if st.session_state.current_q is None:
            st.session_state.current_q = pick_question(paper, section)
            st.session_state.answered_current = False

        q = st.session_state.current_q

        st.markdown(f"**Q{st.session_state.answered_count + 1}. {q['question']}**")

        # show options as radio buttons
        choice = st.radio("Choose your answer:", q["options"],
                          index=None, key=f"choice_{st.session_state.answered_count}")

        if not st.session_state.answered_current:
            if st.button("Submit Answer"):
                if choice is None:
                    st.warning("Please select an answer first.")
                else:
                    # remember which option the user chose, so we can show the
                    # result correctly after the page reruns
                    st.session_state.chosen_index = q["options"].index(choice)
                    st.session_state.answered_current = True
                    st.session_state.answered_count += 1
                    if st.session_state.chosen_index == q["answer"]:
                        st.session_state.score += 1
                    st.rerun()
        else:
            # already answered -> show the stored result + next button
            chosen_index = st.session_state.get("chosen_index")
            correct_text = q["options"][q["answer"]]
            if chosen_index == q["answer"]:
                st.success("✅ Correct!")
            else:
                st.error(f"❌ Incorrect. Correct answer: {correct_text}")
            st.info(f"Explanation: {q['explain']}")

            if st.button("Next Question ➡️"):
                st.session_state.current_q = None
                st.session_state.answered_current = False
                st.session_state.chosen_index = None
                st.rerun()
