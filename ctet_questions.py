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

    # ===========================================================
    # PAPER 1 — Child Development & Pedagogy  (30 questions)
    # ===========================================================
    {
        "paper": "Paper 1",
        "section": "Child Development & Pedagogy",
        "question": "The concept of the 'Zone of Proximal Development' is associated with which theorist?",
        "options": ["Jean Piaget", "Lev Vygotsky", "B.F. Skinner", "Howard Gardner"],
        "answer": 1,
        "explain": "Vygotsky described the ZPD as the gap between what a learner can do alone and what they can do with guidance.",
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
    {
        "paper": "Paper 1",
        "section": "Child Development & Pedagogy",
        "question": "According to Piaget, a child who can think logically about concrete objects but not yet about abstract ideas is in which stage?",
        "options": ["Sensorimotor", "Preoperational", "Concrete operational", "Formal operational"],
        "answer": 2,
        "explain": "The Concrete Operational stage (ages 7–11) is marked by logical thinking about real, physical objects but limited abstract reasoning.",
    },
    {
        "paper": "Paper 1",
        "section": "Child Development & Pedagogy",
        "question": "Which of the following best describes 'formative assessment'?",
        "options": [
            "Assessment given at the end of the year to assign grades",
            "Ongoing assessment used to monitor learning and provide feedback during instruction",
            "A standardised test normed on a national sample",
            "An entrance test taken before the course begins",
        ],
        "answer": 1,
        "explain": "Formative assessment is continuous and diagnostic — it informs teaching while learning is still in progress.",
    },
    {
        "paper": "Paper 1",
        "section": "Child Development & Pedagogy",
        "question": "Howard Gardner's theory of Multiple Intelligences suggests that teachers should:",
        "options": [
            "Focus only on linguistic and logical-mathematical abilities",
            "Recognise and nurture a variety of intellectual strengths in children",
            "Rank students by a single IQ score",
            "Separate children with different intelligences into different classes",
        ],
        "answer": 1,
        "explain": "Gardner proposed eight intelligences (linguistic, logical, musical, spatial, etc.) to reflect the diverse ways children learn and excel.",
    },
    {
        "paper": "Paper 1",
        "section": "Child Development & Pedagogy",
        "question": "The Right of Children to Free and Compulsory Education Act (RTE) guarantees free education to children aged:",
        "options": ["3–14 years", "6–14 years", "5–16 years", "6–18 years"],
        "answer": 1,
        "explain": "RTE 2009 guarantees free and compulsory education for all children between 6 and 14 years of age.",
    },
    {
        "paper": "Paper 1",
        "section": "Child Development & Pedagogy",
        "question": "Which principle states that development moves from head to toe?",
        "options": ["Proximodistal principle", "Cephalocaudal principle", "Continuity principle", "Differentiation principle"],
        "answer": 1,
        "explain": "Cephalocaudal means 'head to tail'. Babies gain control of the head and neck before the trunk, and the trunk before the legs.",
    },
    {
        "paper": "Paper 1",
        "section": "Child Development & Pedagogy",
        "question": "A child with dyslexia primarily has difficulty with:",
        "options": ["Mathematical calculations", "Reading and decoding written language", "Social interaction", "Fine motor skills"],
        "answer": 1,
        "explain": "Dyslexia is a specific learning disability affecting reading accuracy, fluency, and decoding despite normal intelligence.",
    },
    {
        "paper": "Paper 1",
        "section": "Child Development & Pedagogy",
        "question": "Erikson's stage of 'Industry vs. Inferiority' corresponds to which age group?",
        "options": ["0–2 years", "2–6 years", "6–12 years", "12–18 years"],
        "answer": 2,
        "explain": "During the school-age years (6–12), children either develop a sense of competence (industry) or feel inferior if they consistently fail.",
    },
    {
        "paper": "Paper 1",
        "section": "Child Development & Pedagogy",
        "question": "An 'inclusive classroom' means:",
        "options": [
            "Teaching only gifted students",
            "Educating children with and without disabilities together in a common setting",
            "Grouping children by achievement level",
            "Using only lecture-based teaching",
        ],
        "answer": 1,
        "explain": "Inclusive education places learners with diverse needs — including those with disabilities — in mainstream classrooms with appropriate support.",
    },
    {
        "paper": "Paper 1",
        "section": "Child Development & Pedagogy",
        "question": "Which theorist believed that moral development moves through stages from obedience to principled ethics?",
        "options": ["B.F. Skinner", "Lawrence Kohlberg", "Albert Bandura", "John Dewey"],
        "answer": 1,
        "explain": "Kohlberg described three levels of moral development: pre-conventional, conventional, and post-conventional.",
    },
    {
        "paper": "Paper 1",
        "section": "Child Development & Pedagogy",
        "question": "Social learning theory, which emphasises learning through observation and imitation, was proposed by:",
        "options": ["Sigmund Freud", "Jean Piaget", "Albert Bandura", "Ivan Pavlov"],
        "answer": 2,
        "explain": "Bandura's social learning theory highlights how children learn by observing models and imitating behaviour.",
    },
    {
        "paper": "Paper 1",
        "section": "Child Development & Pedagogy",
        "question": "Growth is different from development in that growth is:",
        "options": [
            "Qualitative and internal",
            "Quantitative and measurable (e.g. height, weight)",
            "Concerned with emotions",
            "Lifelong and never stops",
        ],
        "answer": 1,
        "explain": "Growth refers to physical, measurable increases. Development is broader, including cognitive, emotional, and social changes.",
    },
    {
        "paper": "Paper 1",
        "section": "Child Development & Pedagogy",
        "question": "A teacher notices that a student understands a concept better when working with classmates than alone. This best illustrates:",
        "options": ["Negative transfer", "Vygotsky's Zone of Proximal Development", "Classical conditioning", "Rote memorisation"],
        "answer": 1,
        "explain": "The ZPD describes tasks a learner cannot yet manage alone but can accomplish with peer or teacher support.",
    },
    {
        "paper": "Paper 1",
        "section": "Child Development & Pedagogy",
        "question": "Which of the following is NOT a characteristic of child-centred education?",
        "options": [
            "Active participation of learners",
            "Learning through experience and discovery",
            "Teacher as the sole authority who transmits knowledge",
            "Respect for individual differences",
        ],
        "answer": 2,
        "explain": "Child-centred education shifts focus to the learner's activity and discovery. Teacher-as-sole-authority is the traditional 'teacher-centred' approach.",
    },

    # ===========================================================
    # PAPER 1 — Mathematics  (10 questions)
    # ===========================================================
    {
        "paper": "Paper 1",
        "section": "Mathematics",
        "question": "What is the smallest prime number?",
        "options": ["0", "1", "2", "3"],
        "answer": 2,
        "explain": "2 is the smallest prime number and the only even one. 1 is not prime because it has only one factor.",
    },
    {
        "paper": "Paper 1",
        "section": "Mathematics",
        "question": "Before children learn formal addition, the most appropriate skill to develop first is:",
        "options": ["Multiplication tables", "Number sense", "Algebraic notation", "Long division"],
        "answer": 1,
        "explain": "Number sense — understanding quantity, counting and comparison — is the foundation that operations like addition build on.",
    },
    {
        "paper": "Paper 1",
        "section": "Mathematics",
        "question": "The sum of the first five natural numbers is:",
        "options": ["10", "15", "20", "25"],
        "answer": 1,
        "explain": "1+2+3+4+5 = 15. Natural numbers start from 1.",
    },
    {
        "paper": "Paper 1",
        "section": "Mathematics",
        "question": "A fraction whose numerator is greater than its denominator is called a:",
        "options": ["Proper fraction", "Improper fraction", "Unit fraction", "Equivalent fraction"],
        "answer": 1,
        "explain": "An improper fraction has a numerator ≥ denominator, e.g. 7/4. A proper fraction has numerator < denominator.",
    },
    {
        "paper": "Paper 1",
        "section": "Mathematics",
        "question": "Which shape has all sides equal and all angles equal to 90°?",
        "options": ["Rectangle", "Rhombus", "Square", "Parallelogram"],
        "answer": 2,
        "explain": "A square has four equal sides AND four right angles. A rhombus has equal sides but angles are not necessarily 90°.",
    },
    {
        "paper": "Paper 1",
        "section": "Mathematics",
        "question": "The place value of 6 in the number 4,632 is:",
        "options": ["6", "60", "600", "6000"],
        "answer": 2,
        "explain": "In 4,632 the digit 6 is in the hundreds place, so its place value is 600.",
    },
    {
        "paper": "Paper 1",
        "section": "Mathematics",
        "question": "A teacher uses concrete objects, pictures, and then symbols in sequence while teaching a concept. This approach is known as:",
        "options": ["Rote learning", "CPA (Concrete–Pictorial–Abstract) approach", "Direct instruction", "Drill and practice"],
        "answer": 1,
        "explain": "The CPA approach (popularised by Jerome Bruner) moves learners from handling real objects to pictures and finally to abstract symbols.",
    },
    {
        "paper": "Paper 1",
        "section": "Mathematics",
        "question": "The LCM of 4 and 6 is:",
        "options": ["2", "8", "12", "24"],
        "answer": 2,
        "explain": "Multiples of 4: 4,8,12… Multiples of 6: 6,12… The smallest common multiple is 12.",
    },
    {
        "paper": "Paper 1",
        "section": "Mathematics",
        "question": "Which of the following is the best description of 'mathematical communication'?",
        "options": [
            "Speed of mental calculation",
            "Ability to express mathematical thinking through words, diagrams, and symbols",
            "Memorising formulae",
            "Copying solutions from the board",
        ],
        "answer": 1,
        "explain": "Mathematical communication involves explaining reasoning verbally, in writing, and through representations — a key 21st-century skill.",
    },
    {
        "paper": "Paper 1",
        "section": "Mathematics",
        "question": "If a rectangle has a length of 8 cm and a width of 5 cm, its perimeter is:",
        "options": ["13 cm", "26 cm", "40 cm", "80 cm"],
        "answer": 1,
        "explain": "Perimeter = 2 × (length + width) = 2 × (8+5) = 2 × 13 = 26 cm.",
    },

    # ===========================================================
    # PAPER 1 — Environmental Studies  (8 questions)
    # ===========================================================
    {
        "paper": "Paper 1",
        "section": "Environmental Studies",
        "question": "Which of the following is a renewable source of energy?",
        "options": ["Coal", "Petroleum", "Solar energy", "Natural gas"],
        "answer": 2,
        "explain": "Solar energy is renewable. Coal, petroleum and natural gas are fossil fuels and are non-renewable.",
    },
    {
        "paper": "Paper 1",
        "section": "Environmental Studies",
        "question": "The process by which water vapour cools and turns into liquid water, forming clouds, is called:",
        "options": ["Evaporation", "Condensation", "Precipitation", "Transpiration"],
        "answer": 1,
        "explain": "Condensation is the change from gas (water vapour) to liquid. It is how clouds and dew form.",
    },
    {
        "paper": "Paper 1",
        "section": "Environmental Studies",
        "question": "Which gas do plants absorb from the atmosphere during photosynthesis?",
        "options": ["Oxygen", "Nitrogen", "Carbon dioxide", "Hydrogen"],
        "answer": 2,
        "explain": "Plants take in CO₂ and water, and use sunlight to produce glucose and oxygen through photosynthesis.",
    },
    {
        "paper": "Paper 1",
        "section": "Environmental Studies",
        "question": "The best pedagogical approach for EVS at the primary level according to NCF 2005 is:",
        "options": [
            "Lecturing from a textbook",
            "Hands-on activities, observation, and exploration of the local environment",
            "Rote memorisation of facts",
            "Competitive written tests only",
        ],
        "answer": 1,
        "explain": "NCF 2005 recommends inquiry-based, activity-centred learning in EVS that connects to the child's immediate environment.",
    },
    {
        "paper": "Paper 1",
        "section": "Environmental Studies",
        "question": "Which of the following is a biodegradable waste?",
        "options": ["Plastic bottle", "Glass", "Vegetable peels", "Aluminium foil"],
        "answer": 2,
        "explain": "Biodegradable wastes (like vegetable peels) are broken down by microorganisms. Plastics, glass, and metals are non-biodegradable.",
    },
    {
        "paper": "Paper 1",
        "section": "Environmental Studies",
        "question": "Which organ of the human body purifies blood by filtering waste?",
        "options": ["Heart", "Lungs", "Kidneys", "Liver"],
        "answer": 2,
        "explain": "The kidneys filter blood to remove waste products and excess water, which leave the body as urine.",
    },
    {
        "paper": "Paper 1",
        "section": "Environmental Studies",
        "question": "The main cause of air pollution in Indian cities is:",
        "options": ["Volcanic eruptions", "Vehicle exhaust and industrial emissions", "Photosynthesis", "Rainfall"],
        "answer": 1,
        "explain": "Vehicle emissions (CO, NOx, particulate matter) and industrial smoke are the primary contributors to urban air pollution in India.",
    },
    {
        "paper": "Paper 1",
        "section": "Environmental Studies",
        "question": "An EVS teacher takes students to a nearby park to observe insects. This is an example of:",
        "options": ["Rote learning", "Field-based experiential learning", "Summative assessment", "Direct instruction"],
        "answer": 1,
        "explain": "Field trips and nature observation are experiential learning strategies strongly recommended for primary EVS.",
    },

    # ===========================================================
    # PAPER 1 — Language I  (7 questions)
    # ===========================================================
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
    {
        "paper": "Paper 1",
        "section": "Language I",
        "question": "The 'whole language approach' to reading emphasises:",
        "options": [
            "Isolated phonics drills before any reading",
            "Exposure to meaningful, authentic texts from the beginning",
            "Silent reading only",
            "Grammar rules taught before comprehension",
        ],
        "answer": 1,
        "explain": "The whole language approach immerses children in real texts and treats reading as a meaning-making process rather than decoding drills.",
    },
    {
        "paper": "Paper 1",
        "section": "Language I",
        "question": "Which skill is considered a 'receptive' language skill?",
        "options": ["Speaking", "Writing", "Listening", "Reading aloud"],
        "answer": 2,
        "explain": "Receptive skills involve receiving language: listening and reading. Productive skills involve producing language: speaking and writing.",
    },
    {
        "paper": "Paper 1",
        "section": "Language I",
        "question": "A student who confuses 'b' and 'd' in reading and writing may be showing signs of:",
        "options": ["ADHD", "Dyslexia", "Dyscalculia", "Autism"],
        "answer": 1,
        "explain": "Mirror-image letter confusion (b/d, p/q) is a common indicator of dyslexia, a specific learning difficulty with reading.",
    },
    {
        "paper": "Paper 1",
        "section": "Language I",
        "question": "The primary purpose of a 'reading aloud' activity by the teacher in a primary class is:",
        "options": [
            "To test students' decoding skills",
            "To model fluent reading and expose children to rich language",
            "To assess comprehension through MCQs",
            "To introduce grammar rules",
        ],
        "answer": 1,
        "explain": "Teacher read-alouds model expression, fluency, and vocabulary, and build a love of literature in young learners.",
    },
    {
        "paper": "Paper 1",
        "section": "Language I",
        "question": "In language teaching, 'communicative competence' refers to:",
        "options": [
            "Correct use of grammar only",
            "The ability to use language appropriately and effectively in real social contexts",
            "Memorising vocabulary lists",
            "Speed of reading",
        ],
        "answer": 1,
        "explain": "Communicative competence (Hymes) includes grammatical, sociolinguistic, discourse, and strategic competence for real-world communication.",
    },
    {
        "paper": "Paper 1",
        "section": "Language I",
        "question": "Which of the following best supports vocabulary development in young learners?",
        "options": [
            "Copying new words ten times",
            "Rich contextual exposure through stories, conversations, and wide reading",
            "Translating every word into the mother tongue",
            "Spelling tests every Friday",
        ],
        "answer": 1,
        "explain": "Research shows vocabulary is best acquired through rich, meaningful exposure in context — not isolated drilling.",
    },

    # ===========================================================
    # PAPER 1 — Language II  (5 questions)
    # ===========================================================
    {
        "paper": "Paper 1",
        "section": "Language II",
        "question": "According to Krashen's Input Hypothesis, language is acquired when learners receive input that is:",
        "options": [
            "Far above their current level",
            "Slightly beyond their current level (i+1)",
            "Exactly at their current level",
            "Below their current level",
        ],
        "answer": 1,
        "explain": "Krashen's i+1 hypothesis states that comprehensible input just above the learner's current ability drives acquisition.",
    },
    {
        "paper": "Paper 1",
        "section": "Language II",
        "question": "The most effective way to correct a young learner's spoken grammar error is:",
        "options": [
            "Stop and correct the error harshly in front of the class",
            "Ignore all errors completely",
            "Recast — repeat the utterance correctly without drawing negative attention",
            "Give extra homework as a penalty",
        ],
        "answer": 2,
        "explain": "Recasting provides a correct model implicitly. Research shows it is more effective than explicit correction for young learners.",
    },
    {
        "paper": "Paper 1",
        "section": "Language II",
        "question": "A teacher uses pictures, gestures, and real objects to explain meaning without translating. This technique is called:",
        "options": ["Grammar-translation method", "Direct method", "Silent way", "Audiolingual method"],
        "answer": 1,
        "explain": "The direct method avoids translation and links language directly to meaning through visual and physical context.",
    },
    {
        "paper": "Paper 1",
        "section": "Language II",
        "question": "Which activity best develops writing skills in early primary classes?",
        "options": [
            "Copying text from the blackboard",
            "Dictation at speed",
            "Guided writing with picture prompts and sentence frames",
            "Grammar exercises only",
        ],
        "answer": 2,
        "explain": "Guided writing with scaffolds (pictures, sentence starters) gives children structure to express ideas while developing writing skills.",
    },
    {
        "paper": "Paper 1",
        "section": "Language II",
        "question": "Which of the following is an example of 'extensive reading'?",
        "options": [
            "Close reading of a single paragraph for grammar analysis",
            "Reading a large number of books for general comprehension and enjoyment",
            "Reading aloud from the textbook page by page",
            "Memorising a poem",
        ],
        "answer": 1,
        "explain": "Extensive reading involves reading large quantities of material at or below one's level for fluency and enjoyment.",
    },

    # ===========================================================
    # PAPER 2 — Child Development & Pedagogy  (12 questions)
    # ===========================================================
    {
        "paper": "Paper 2",
        "section": "Child Development & Pedagogy",
        "question": "Piaget's Formal Operational stage, which begins around age 11–12, is characterised by:",
        "options": [
            "Object permanence",
            "Egocentrism",
            "Abstract and hypothetical reasoning",
            "Symbolic play",
        ],
        "answer": 2,
        "explain": "In the Formal Operational stage, adolescents can reason about hypothetical situations and think systematically about abstract concepts.",
    },
    {
        "paper": "Paper 2",
        "section": "Child Development & Pedagogy",
        "question": "Which assessment tool is most useful for tracking a student's progress over time?",
        "options": ["Single end-term examination", "Portfolio assessment", "MCQ quiz", "Oral test"],
        "answer": 1,
        "explain": "A portfolio collects work samples over time, showing growth, strengths, and areas for improvement better than a single test.",
    },
    {
        "paper": "Paper 2",
        "section": "Child Development & Pedagogy",
        "question": "The NEP 2020 emphasises foundational literacy and numeracy for children up to Grade:",
        "options": ["2", "3", "5", "8"],
        "answer": 1,
        "explain": "NEP 2020 highlights achieving universal Foundational Literacy and Numeracy by the end of Grade 3 (around age 8–9).",
    },
    {
        "paper": "Paper 2",
        "section": "Child Development & Pedagogy",
        "question": "A student who is gifted should be provided with:",
        "options": [
            "Extra homework from the same textbook",
            "Enrichment activities, higher-order challenges, and opportunities to mentor peers",
            "Separate schooling away from the class",
            "No special intervention since they will manage alone",
        ],
        "answer": 1,
        "explain": "Gifted learners need enrichment and extension tasks that challenge higher-order thinking, not just more of the same work.",
    },
    {
        "paper": "Paper 2",
        "section": "Child Development & Pedagogy",
        "question": "Which of the following is a sign of ADHD (Attention Deficit Hyperactivity Disorder) in a classroom?",
        "options": [
            "Reading slowly but with good comprehension",
            "Consistent difficulty sustaining attention, impulsivity, and excessive movement",
            "Reluctance to speak in public",
            "Strong preference for mathematics over language",
        ],
        "answer": 1,
        "explain": "ADHD is characterised by inattention, hyperactivity, and impulsivity that interfere with functioning in school and daily life.",
    },
    {
        "paper": "Paper 2",
        "section": "Child Development & Pedagogy",
        "question": "The process of adapting teaching methods, materials, and assessment for diverse learners is called:",
        "options": ["Mainstreaming", "Differentiated instruction", "Streaming", "Remediation"],
        "answer": 1,
        "explain": "Differentiated instruction modifies content, process, and product based on students' readiness, interest, and learning profile.",
    },
    {
        "paper": "Paper 2",
        "section": "Child Development & Pedagogy",
        "question": "Which type of question promotes higher-order thinking according to Bloom's Taxonomy?",
        "options": [
            "'What is the capital of India?'",
            "'List the bones in the human body.'",
            "'How would life change if there were no forests? Justify your answer.'",
            "'Define photosynthesis.'",
        ],
        "answer": 2,
        "explain": "Questions requiring analysis, evaluation, or creation sit at the top of Bloom's Taxonomy. Recall and definition questions are lower-order.",
    },
    {
        "paper": "Paper 2",
        "section": "Child Development & Pedagogy",
        "question": "Continuous and Comprehensive Evaluation (CCE) was introduced to:",
        "options": [
            "Replace all written examinations with oral tests",
            "Assess both scholastic and co-scholastic aspects of learning throughout the year",
            "Promote only rank-based competition",
            "Reduce the school hours",
        ],
        "answer": 1,
        "explain": "CCE shifted focus from year-end exams to year-round assessment of both academic achievement and personality/life skills.",
    },
    {
        "paper": "Paper 2",
        "section": "Child Development & Pedagogy",
        "question": "A teacher who asks 'What evidence supports your answer?' is developing which skill?",
        "options": ["Rote memory", "Critical thinking", "Handwriting", "Pronunciation"],
        "answer": 1,
        "explain": "Asking for evidence promotes reasoning and critical thinking — core 21st-century competencies.",
    },
    {
        "paper": "Paper 2",
        "section": "Child Development & Pedagogy",
        "question": "Which of the following correctly describes 'peer learning'?",
        "options": [
            "Students compete against each other for marks",
            "Students learn from and with each other through collaboration",
            "Students copy homework from peers",
            "Students receive one-to-one coaching from the teacher",
        ],
        "answer": 1,
        "explain": "Peer learning is a social-constructivist strategy where students explain, discuss, and construct knowledge together.",
    },
    {
        "paper": "Paper 2",
        "section": "Child Development & Pedagogy",
        "question": "The main aim of National Curriculum Framework (NCF) 2005 was to:",
        "options": [
            "Increase the number of textbooks",
            "Reduce the burden of examinations and shift towards constructivist, child-centred learning",
            "Make English the medium of instruction for all subjects",
            "Introduce more competitive examinations",
        ],
        "answer": 1,
        "explain": "NCF 2005 advocated reducing rote learning, connecting knowledge to life, and making education joyful and constructivist.",
    },
    {
        "paper": "Paper 2",
        "section": "Child Development & Pedagogy",
        "question": "According to Vygotsky, the role of language in cognitive development is that it:",
        "options": [
            "Has no influence on thinking",
            "Follows cognitive development and has no independent role",
            "Is a tool for thought that mediates higher mental functions",
            "Only develops after age 7",
        ],
        "answer": 2,
        "explain": "Vygotsky saw language as a cultural tool that transforms and mediates thinking — inner speech becomes the foundation of higher cognition.",
    },

    # ===========================================================
    # PAPER 2 — Mathematics & Science  (10 questions)
    # ===========================================================
    {
        "paper": "Paper 2",
        "section": "Mathematics & Science",
        "question": "The HCF of 36 and 48 is:",
        "options": ["6", "12", "18", "24"],
        "answer": 1,
        "explain": "Factors of 36: 1,2,3,4,6,9,12,18,36. Factors of 48: 1,2,3,4,6,8,12,16,24,48. The highest common factor is 12.",
    },
    {
        "paper": "Paper 2",
        "section": "Mathematics & Science",
        "question": "Newton's First Law of Motion states that an object at rest remains at rest unless acted upon by:",
        "options": ["Gravity alone", "An unbalanced (net) external force", "Friction", "Its own inertia"],
        "answer": 1,
        "explain": "Newton's First Law (Law of Inertia): objects maintain their state of motion unless a net external force acts on them.",
    },
    {
        "paper": "Paper 2",
        "section": "Mathematics & Science",
        "question": "Which type of change is dissolving sugar in water?",
        "options": ["Physical change", "Chemical change", "Nuclear change", "Biological change"],
        "answer": 0,
        "explain": "Dissolving sugar is a physical change — no new substance is formed and the sugar can be recovered by evaporating the water.",
    },
    {
        "paper": "Paper 2",
        "section": "Mathematics & Science",
        "question": "The sum of angles in a triangle is always:",
        "options": ["90°", "180°", "270°", "360°"],
        "answer": 1,
        "explain": "The interior angles of any triangle always add up to 180°.",
    },
    {
        "paper": "Paper 2",
        "section": "Mathematics & Science",
        "question": "Which part of the cell controls its activities and contains DNA?",
        "options": ["Cell membrane", "Cytoplasm", "Nucleus", "Mitochondria"],
        "answer": 2,
        "explain": "The nucleus is the control centre of the cell. It contains chromosomes (made of DNA) that carry genetic information.",
    },
    {
        "paper": "Paper 2",
        "section": "Mathematics & Science",
        "question": "A science teacher asks students to predict what will happen before conducting an experiment. This promotes:",
        "options": [
            "Rote memorisation of results",
            "Scientific inquiry and hypothesis formation",
            "Passive observation",
            "Copying from reference books",
        ],
        "answer": 1,
        "explain": "Prediction before observation is a key inquiry skill that builds hypothesis testing and scientific thinking.",
    },
    {
        "paper": "Paper 2",
        "section": "Mathematics & Science",
        "question": "If 3x + 7 = 22, what is x?",
        "options": ["3", "5", "7", "9"],
        "answer": 1,
        "explain": "3x = 22 – 7 = 15, so x = 15 ÷ 3 = 5.",
    },
    {
        "paper": "Paper 2",
        "section": "Mathematics & Science",
        "question": "Which of the following is an example of potential energy?",
        "options": [
            "A rolling ball",
            "Water stored behind a dam",
            "A running child",
            "Sound waves",
        ],
        "answer": 1,
        "explain": "Potential energy is stored energy due to position. Water behind a dam has gravitational potential energy.",
    },
    {
        "paper": "Paper 2",
        "section": "Mathematics & Science",
        "question": "The process of using errors as learning opportunities in mathematics teaching is best described as:",
        "options": [
            "Penalising students for wrong answers",
            "Analysing misconceptions to guide re-teaching",
            "Ignoring incorrect responses",
            "Moving quickly past errors to finish the syllabus",
        ],
        "answer": 1,
        "explain": "Errors reveal students' thinking. Analysing them helps teachers address misconceptions and deepen understanding.",
    },
    {
        "paper": "Paper 2",
        "section": "Mathematics & Science",
        "question": "Photosynthesis takes place mainly in the:",
        "options": ["Roots", "Stem", "Leaves", "Flowers"],
        "answer": 2,
        "explain": "Leaves contain chlorophyll and are the primary site of photosynthesis, where light energy converts CO₂ and water into glucose.",
    },

    # ===========================================================
    # PAPER 2 — Social Studies / Social Science  (8 questions)
    # ===========================================================
    {
        "paper": "Paper 2",
        "section": "Social Studies / Social Science",
        "question": "The Indian Constitution came into effect on:",
        "options": ["15 August 1947", "26 January 1950", "26 November 1949", "2 October 1952"],
        "answer": 1,
        "explain": "The Constitution of India was adopted on 26 November 1949 but came into force on 26 January 1950 — celebrated as Republic Day.",
    },
    {
        "paper": "Paper 2",
        "section": "Social Studies / Social Science",
        "question": "The best approach to teach history at the upper primary level is:",
        "options": [
            "Memorising dates and names",
            "Using source-based inquiry, timelines, and connecting events to students' lives",
            "Dictation from the textbook",
            "Watching only documentary films",
        ],
        "answer": 1,
        "explain": "Inquiry-based history teaching with primary sources and timelines develops historical thinking rather than passive memorisation.",
    },
    {
        "paper": "Paper 2",
        "section": "Social Studies / Social Science",
        "question": "The term 'secularism' in the Indian context means:",
        "options": [
            "The state has an official religion",
            "The state has no official religion and treats all religions equally",
            "Religion is banned in public life",
            "Only Hinduism, Islam, and Christianity are recognised",
        ],
        "answer": 1,
        "explain": "Indian secularism means the state has no official religion and does not favour or discriminate against any religion.",
    },
    {
        "paper": "Paper 2",
        "section": "Social Studies / Social Science",
        "question": "The Tropic of Cancer passes through which Indian state among the following?",
        "options": ["Kerala", "Madhya Pradesh", "Punjab", "Tamil Nadu"],
        "answer": 1,
        "explain": "The Tropic of Cancer (23.5°N) passes through Rajasthan, Gujarat, Madhya Pradesh, Chhattisgarh, Jharkhand, West Bengal, Tripura, and Mizoram.",
    },
    {
        "paper": "Paper 2",
        "section": "Social Studies / Social Science",
        "question": "The Preamble to the Indian Constitution describes India as a:",
        "options": [
            "Federal, Democratic Republic",
            "Sovereign, Socialist, Secular, Democratic Republic",
            "Unitary, Secular State",
            "Sovereign, Capitalist, Democratic Republic",
        ],
        "answer": 1,
        "explain": "The 42nd Amendment (1976) added 'Socialist' and 'Secular'. The full description is: Sovereign Socialist Secular Democratic Republic.",
    },
    {
        "paper": "Paper 2",
        "section": "Social Studies / Social Science",
        "question": "Which river is known as the 'Sorrow of Bihar'?",
        "options": ["Ganga", "Yamuna", "Kosi", "Son"],
        "answer": 2,
        "explain": "The Kosi river is called the 'Sorrow of Bihar' because its frequent and devastating floods have historically caused immense loss.",
    },
    {
        "paper": "Paper 2",
        "section": "Social Studies / Social Science",
        "question": "Concept mapping in social science teaching primarily helps students to:",
        "options": [
            "Memorise capitals and dates",
            "Visualise relationships between concepts and organise knowledge",
            "Practice handwriting",
            "Prepare for objective tests",
        ],
        "answer": 1,
        "explain": "Concept maps are graphic organisers that show how ideas are connected, supporting deeper understanding and meaningful learning.",
    },
    {
        "paper": "Paper 2",
        "section": "Social Studies / Social Science",
        "question": "Fundamental Rights in India are guaranteed under which Part of the Constitution?",
        "options": ["Part II", "Part III", "Part IV", "Part V"],
        "answer": 1,
        "explain": "Part III (Articles 12–35) of the Indian Constitution contains the Fundamental Rights guaranteed to all citizens.",
    },

    # ===========================================================
    # PAPER 2 — Language I  (5 questions)
    # ===========================================================
    {
        "paper": "Paper 2",
        "section": "Language I",
        "question": "The communicative language teaching (CLT) approach focuses on:",
        "options": [
            "Accuracy of grammar above all else",
            "Real-life communication and meaningful use of language",
            "Translation exercises",
            "Phonics rules only",
        ],
        "answer": 1,
        "explain": "CLT prioritises fluency and meaningful communication over isolated grammar accuracy.",
    },
    {
        "paper": "Paper 2",
        "section": "Language I",
        "question": "A teacher who asks upper primary students to debate a social issue is developing:",
        "options": [
            "Only vocabulary",
            "Critical thinking, argumentation, and oral communication skills",
            "Handwriting skills",
            "Listening comprehension alone",
        ],
        "answer": 1,
        "explain": "Debate integrates higher-order thinking with oral language skills — a powerful activity for upper primary learners.",
    },
    {
        "paper": "Paper 2",
        "section": "Language I",
        "question": "Which is a characteristic of 'process writing'?",
        "options": [
            "Writing a final draft in one sitting",
            "Moving through stages: pre-writing, drafting, revising, editing, publishing",
            "Copying a model paragraph",
            "Focusing only on spelling and punctuation",
        ],
        "answer": 1,
        "explain": "Process writing treats writing as a recursive cycle of planning, drafting, and revising — not a single-attempt product.",
    },
    {
        "paper": "Paper 2",
        "section": "Language I",
        "question": "Which of the following is an authentic assessment task for language learning?",
        "options": [
            "Fill-in-the-blank grammar exercise",
            "Writing a letter to the school principal requesting a change",
            "Selecting the correct tense from a list",
            "Identifying parts of speech in isolated sentences",
        ],
        "answer": 1,
        "explain": "Authentic assessment uses real-world tasks (like writing a letter) that have meaning beyond the classroom.",
    },
    {
        "paper": "Paper 2",
        "section": "Language I",
        "question": "Reading for the specific information you need (e.g. finding a phone number in a directory) is called:",
        "options": ["Skimming", "Scanning", "Intensive reading", "Extensive reading"],
        "answer": 1,
        "explain": "Scanning means moving quickly through text to find a specific fact or piece of information.",
    },

    # ===========================================================
    # PAPER 2 — Language II  (5 questions)
    # ===========================================================
    {
        "paper": "Paper 2",
        "section": "Language II",
        "question": "Which method of language teaching relies heavily on dialogue memorisation and pattern drills?",
        "options": ["Communicative Language Teaching", "Audiolingual Method", "Silent Way", "Natural Approach"],
        "answer": 1,
        "explain": "The Audiolingual Method uses repetition, drills, and dialogue memorisation based on behaviourist learning theory.",
    },
    {
        "paper": "Paper 2",
        "section": "Language II",
        "question": "A student makes the error 'He go to school every day.' This is an example of:",
        "options": ["Random error", "Developmental error due to overgeneralisation", "Copying error", "Pronunciation error"],
        "answer": 1,
        "explain": "Omitting the third-person '-s' is a developmental error where learners apply a general rule (no inflection) before mastering the exception.",
    },
    {
        "paper": "Paper 2",
        "section": "Language II",
        "question": "Reading quickly to get the general idea of a text is called:",
        "options": ["Scanning", "Skimming", "Intensive reading", "Decoding"],
        "answer": 1,
        "explain": "Skimming means reading quickly for the gist or main idea without attention to every word.",
    },
    {
        "paper": "Paper 2",
        "section": "Language II",
        "question": "The term 'mother tongue interference' in language learning refers to:",
        "options": [
            "Parents interrupting homework",
            "Errors caused by applying rules of the first language to the second language",
            "Using the mother tongue in translation exercises",
            "Refusing to learn a second language",
        ],
        "answer": 1,
        "explain": "Interference (also called negative transfer) occurs when L1 structures are incorrectly applied to L2, causing systematic errors.",
    },
    {
        "paper": "Paper 2",
        "section": "Language II",
        "question": "A teacher who provides sentence starters, word banks, and model paragraphs to help students write is using:",
        "options": ["Punishment", "Scaffolding", "Rote learning", "Summative assessment"],
        "answer": 1,
        "explain": "Writing supports like sentence frames and word banks are scaffolds that reduce cognitive load while students develop independence.",
    },

]
