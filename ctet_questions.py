"""
CTET QUESTION BANK
==================
This is where your questions live. The app reads from the QUESTIONS list below.

WHERE TO GET QUESTIONS (safely):
  1. Official CTET papers + answer keys, free from CBSE: https://ctet.nic.in
     (Look for "Previous Year Question Papers" / "Answer Keys".)
  2. Questions you write yourself, based on the NCERT syllabus.
  3. AI-generated questions that YOU verify before adding.

  Do NOT copy questions out of a paid book or paid app to resell them -- that is
  a copyright problem. The official CBSE papers are free and are the real exam,
  so use those.

HOW TO ADD A QUESTION:
  Copy one block between the {curly braces}, paste it at the end of the list,
  and edit the five fields. That's it -- no other code changes needed.

  paper    : "Paper 1" or "Paper 2"
  section  : must exactly match a name in SECTIONS below
  question : the question text
  options  : list of exactly 4 options
  answer   : index of the correct option -> 0=first, 1=second, 2=third, 3=fourth
  explain  : one or two lines shown to the student after they answer

TIP: the most common mistake is the answer index. Remember it starts at 0.
     If the correct option is the 3rd one in the list, answer = 2.
"""

# Section names for each paper (these build the dropdown menus)
SECTIONS = {
    "Paper 1": [
        "Child Development & Pedagogy",
        "Language I",
        "Language II",
        "Mathematics",
        "Environmental Studies",
    ],
    "Paper 2": [
        "Child Development & Pedagogy",
        "Language I",
        "Language II",
        "Mathematics & Science",
        "Social Studies / Social Science",
    ],
}

# ---------------------------------------------------------------------------
# QUESTIONS
# A few generic samples so the app runs and you can demo it.
# Replace and expand these with your own verified questions.
# ---------------------------------------------------------------------------
QUESTIONS = [

    # ===================== TEMPLATE (copy me) ==============================
    # {
    #     "paper": "Paper 1",
    #     "section": "Child Development & Pedagogy",
    #     "question": "Type the question here?",
    #     "options": ["First option", "Second option", "Third option", "Fourth option"],
    #     "answer": 0,   # 0=first, 1=second, 2=third, 3=fourth
    #     "explain": "Short reason the correct answer is correct.",
    # },
    # ======================================================================

    # ---------- Paper 1 : Child Development & Pedagogy ----------
    {
        "paper": "Paper 1",
        "section": "Child Development & Pedagogy",
        "question": "The concept of the 'Zone of Proximal Development' is associated with which theorist?",
        "options": ["Jean Piaget", "Lev Vygotsky", "B.F. Skinner", "Howard Gardner"],
        "answer": 1,
        "explain": "Vygotsky described the Zone of Proximal Development as the gap between what a learner can do alone and what they can do with guidance.",
    },
    {
        "paper": "Paper 1",
        "section": "Child Development & Pedagogy",
        "question": "A teacher giving a partly-worked example and gradually withdrawing support as the learner improves is using:",
        "options": ["Conditioning", "Scaffolding", "Rote drill", "Norm-referencing"],
        "answer": 1,
        "explain": "Scaffolding means giving support early in learning and slowly removing it as the learner becomes able to work independently.",
    },
    {
        "paper": "Paper 1",
        "section": "Child Development & Pedagogy",
        "question": "Learning driven by a child's own interest and curiosity, rather than by rewards, is called:",
        "options": ["Extrinsic motivation", "Intrinsic motivation", "Negative reinforcement", "External regulation"],
        "answer": 1,
        "explain": "Intrinsic motivation comes from within the learner. Extrinsic motivation relies on outside rewards or punishments.",
    },

    # ---------- Paper 1 : Mathematics ----------
    {
        "paper": "Paper 1",
        "section": "Mathematics",
        "question": "What is the smallest prime number?",
        "options": ["0", "1", "2", "3"],
        "answer": 2,
        "explain": "2 is the smallest prime number and the only even one. (1 is not prime; it has only one factor.)",
    },
    {
        "paper": "Paper 1",
        "section": "Mathematics",
        "question": "Before children learn formal addition, the most appropriate skill to develop first is:",
        "options": ["Multiplication tables", "Number sense", "Algebraic notation", "Long division"],
        "answer": 1,
        "explain": "Number sense -- understanding quantity, counting and comparison -- is the foundation that operations like addition build on.",
    },

    # ---------- Paper 1 : Environmental Studies ----------
    {
        "paper": "Paper 1",
        "section": "Environmental Studies",
        "question": "Which of the following is a renewable source of energy?",
        "options": ["Coal", "Petroleum", "Solar energy", "Natural gas"],
        "answer": 2,
        "explain": "Solar energy is renewable. Coal, petroleum and natural gas are fossil fuels and are non-renewable.",
    },

    # ---------- Paper 1 : Language I ----------
    {
        "paper": "Paper 1",
        "section": "Language I",
        "question": "In a multilingual primary classroom, the most appropriate approach is to:",
        "options": [
            "Ignore the home languages of learners",
            "Allow learners to express themselves in their own language and build from there",
            "Insist only on the school language from day one",
            "Separate children by language group",
        ],
        "answer": 1,
        "explain": "Good practice respects the child's home language and uses it as a bridge, rather than ignoring or suppressing it.",
    },

]
