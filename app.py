import streamlit as st
from prompts import (
    get_greeting,
    get_info_prompt,
    get_tech_questions_prompt,
    get_fallback_prompt,
    get_end_convo_prompt,
    get_interest_prompt,
    get_negative_acknowledgement,
)
from utils import (
    call_llm,
    is_end_conversation,
    validate_email,
    validate_phone,
    anonymize_candidate_data,
)

st.set_page_config(page_title="Nursing College Admission Assistant", layout="centered")

# Initialize session state
if "conversation_step" not in st.session_state:
    st.session_state.conversation_step = 0
    st.session_state.chat_history = []
    st.session_state.user_eligible = None

def add_to_history(role, content):
    st.session_state.chat_history.append({"role": role, "content": content})

# Display chat history
st.title("Nursing College Admission Assistant")
for entry in st.session_state.chat_history:
    st.chat_message(entry["role"]).write(entry["content"])

def is_positive(text):
    return any(word in text.lower() for word in ["haan", "yes", "batao", "kya hai", "sahi hai"])

def is_negative(text):
    return any(word in text.lower() for word in ["nahi", "no", "mat karo", "chhodo", "koi baat nahi"])

# Conversation-ending keywords
END_KEYWORDS = ["exit", "quit", "end", "bye", "goodbye"]

# Candidate info fields in order
INFO_FIELDS = [
    ("name", "Full Name"),
    ("email", "Email Address"),
    ("phone", "Phone Number"),
    ("experience", "Years of Experience"),
    ("position", "Desired Position(s)"),
    ("location", "Current Location"),
    ("tech_stack", "Tech Stack (languages, frameworks, databases, tools)")
]

# Main chat area
st.title("TalentScout Hiring Assistant")
st.write("Welcome to TalentScout! Please interact with our AI assistant to begin your application.")

# Display chat history
for entry in st.session_state.chat_history:
    st.chat_message(entry["role"]).write(entry["content"])

# End conversation gracefully
if st.session_state.ended:
    st.info(get_end_convo_prompt())
    st.stop()

# Chatbot logic
if st.session_state.step == 0:
    add_to_history("assistant", get_greeting())
    st.session_state.step = 1
    st.rerun()

elif st.session_state.step == 1:
    # Admission interest
    if not (st.session_state.chat_history and st.session_state.chat_history[-1]["role"] == "assistant"):
        add_to_history("assistant", get_interest_prompt())
    user_input = st.chat_input("Type your answer...")
    if user_input:
        if is_positive(user_input):
            st.session_state.step = 2
        elif is_negative(user_input):
            add_to_history("assistant", get_negative_acknowledgement())
            st.session_state.ended = True
        else:
            add_to_history("assistant", get_fallback_prompt())
        add_to_history("user", user_input)
        st.rerun()

# Info gathering
elif st.session_state.step <= len(INFO_FIELDS):
    field, label = INFO_FIELDS[st.session_state.step-1]
    prompt = get_info_prompt(field)
    # Only add the assistant's question if it's not already the last message
    if not (st.session_state.chat_history and st.session_state.chat_history[-1]["role"] == "assistant" and st.session_state.chat_history[-1]["content"] == prompt):
        add_to_history("assistant", prompt)
    user_input = st.chat_input("Type your answer...")  # Use a generic prompt
    if user_input:
        if is_end_conversation(user_input, END_KEYWORDS):
            st.session_state.ended = True
            st.rerun()
        # Validation
        if field == "email" and not validate_email(user_input):
            add_to_history("assistant", "Please enter a valid email address.")
        elif field == "phone" and not validate_phone(user_input):
            add_to_history("assistant", "Please enter a valid phone number.")
        else:
            st.session_state.candidate[field] = user_input.strip()
            st.session_state.step += 1
            st.rerun()

# Tech stack question generation
elif st.session_state.step == len(INFO_FIELDS) + 1:
    tech_stack = st.session_state.candidate.get("tech_stack", "")
    years = st.session_state.candidate.get("experience", "1")
    techs = [t.strip() for t in tech_stack.split(",") if t.strip()]
    questions = []
    for tech in techs:
        prompt = get_tech_questions_prompt(tech, years)
        qlist = call_llm(prompt, n=3)
        if isinstance(qlist, list):
            questions.extend([(tech, q) for q in qlist])
        else:
            questions.append((tech, qlist))
    st.session_state.tech_questions = questions
    st.session_state.step += 1
    st.rerun()

# Ask technical questions
elif st.session_state.step == len(INFO_FIELDS) + 2:
    idx = len(st.session_state.answered_questions)
    if idx < len(st.session_state.tech_questions):
        tech, question = st.session_state.tech_questions[idx]
        user_input = st.chat_input(f"[{tech}] {question}")
        if user_input:
            if is_end_conversation(user_input, END_KEYWORDS):
                st.session_state.ended = True
                st.rerun()
            st.session_state.answered_questions.append({"tech": tech, "question": question, "answer": user_input})
            add_to_history("user", user_input)
            st.rerun()
    else:
        st.session_state.step += 1
        st.rerun()

# End conversation
else:
    add_to_history("assistant", get_end_convo_prompt())
    st.session_state.ended = True
    st.rerun()