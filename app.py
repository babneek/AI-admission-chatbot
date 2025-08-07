import streamlit as st
from prompts import (
    get_greeting,
    get_interest_prompt,
    get_biology_check_prompt,
    get_biology_required_prompt,
    get_program_details_prompt,
    get_fee_structure_prompt,
    get_hostel_facilities_prompt,
    get_location_prompt,
    get_recognition_prompt,
    get_clinical_training_prompt,
    get_scholarship_prompt,
    get_seats_prompt,
    get_eligibility_prompt,
    get_info_prompt,
    get_positive_acknowledgement,
    get_negative_acknowledgement,
    get_fallback_prompt,
    get_end_convo_prompt,
)
from utils import (
    is_positive,
    is_negative,
    is_end_conversation,
    validate_email,
    validate_phone,
    anonymize_candidate_data,
)

# Initialize session state variables
if "step" not in st.session_state:
    st.session_state.step = 0
if "ended" not in st.session_state:
    st.session_state.ended = False
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "candidate" not in st.session_state:
    st.session_state.candidate = {}

def add_to_history(role, content):
    st.session_state.chat_history.append({"role": role, "content": content})

# Main chat area
st.title("Nursing College Admission Assistant")

for entry in st.session_state.chat_history:
    st.chat_message(entry["role"]).write(entry["content"])

if st.session_state.ended:
    st.info(get_end_convo_prompt())
    st.stop()

# Step 0: Greeting
if st.session_state.step == 0:
    st.session_state.chat_history.clear()
    add_to_history("assistant", get_greeting())
    st.session_state.step = 1
    st.rerun()

# Step 1: Admission Interest
elif st.session_state.step == 1:
    user_input = st.chat_input("Type your answer...")
    if user_input:
        add_to_history("user", user_input)
        if is_positive(user_input):
            add_to_history("assistant", get_biology_check_prompt())
            st.session_state.step = 2
        elif is_negative(user_input):
            add_to_history("assistant", get_negative_acknowledgement())
            st.session_state.ended = True
        else:
            add_to_history("assistant", get_fallback_prompt())
        st.rerun()

# Step 2: Biology Eligibility
elif st.session_state.step == 2:
    user_input = st.chat_input("Type your answer...")
    if user_input:
        add_to_history("user", user_input)
        if is_positive(user_input):
            add_to_history("assistant", get_program_details_prompt())
            st.session_state.step = 3
        elif is_negative(user_input):
            add_to_history("assistant", get_biology_required_prompt())
            st.session_state.ended = True
        else:
            add_to_history("assistant", get_fallback_prompt())
        st.rerun()

# Step 3: Program Details
elif st.session_state.step == 3:
    user_input = st.chat_input("Type your answer...")
    if user_input:
        add_to_history("user", user_input)
        if is_positive(user_input):
            add_to_history("assistant", get_fee_structure_prompt())
            st.session_state.step = 4
        elif is_negative(user_input):
            add_to_history("assistant", get_negative_acknowledgement())
            st.session_state.ended = True
        else:
            add_to_history("assistant", get_fallback_prompt())
        st.rerun()

# Step 4: Fee Structure
elif st.session_state.step == 4:
    add_to_history("assistant", get_hostel_facilities_prompt())
    st.session_state.step = 5
    st.rerun()

# Step 5: Hostel & Training Facilities
elif st.session_state.step == 5:
    add_to_history("assistant", get_location_prompt())
    st.session_state.step = 6
    st.rerun()

# Step 6: Location
elif st.session_state.step == 6:
    add_to_history("assistant", get_recognition_prompt())
    st.session_state.step = 7
    st.rerun()

# Step 7: Recognition & Accreditation
elif st.session_state.step == 7:
    add_to_history("assistant", get_clinical_training_prompt())
    st.session_state.step = 8
    st.rerun()

# Step 8: Clinical Training Locations
elif st.session_state.step == 8:
    add_to_history("assistant", get_scholarship_prompt())
    st.session_state.step = 9
    st.rerun()

# Step 9: Scholarships
elif st.session_state.step == 9:
    add_to_history("assistant", get_seats_prompt())
    st.session_state.step = 10
    st.rerun()

# Step 10: Seats Available
elif st.session_state.step == 10:
    add_to_history("assistant", get_eligibility_prompt())
    st.session_state.step = 11
    st.rerun()

# Step 11: End Conversation
elif st.session_state.step == 11:
    add_to_history("assistant", get_end_convo_prompt())
    st.session_state.ended = True
    st.rerun()