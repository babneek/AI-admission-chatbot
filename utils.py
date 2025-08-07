import re
import os
from dotenv import load_dotenv

load_dotenv()

def is_end_conversation(user_input, keywords=None):
    if not keywords:
        keywords = ["exit", "quit", "end", "bye", "goodbye"]
    return any(word in user_input.lower() for word in keywords)

def validate_email(email):
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return re.match(pattern, email) is not None

def validate_phone(phone):
    pattern = r"^[\d\s\-\(\)\+]{7,}$"
    return re.match(pattern, phone) is not None

def anonymize_candidate_data(candidate):
    return {
        **candidate,
        "name": "[REDACTED]",
        "email": "[REDACTED]",
        "phone": "[REDACTED]"
    }

def is_positive(user_input):
    positive_keywords = ["haan", "yes", "y", "batao", "tell", "sure", "ok", "kya hai", "please", "more", "ji"]
    return any(word in user_input.lower() for word in positive_keywords)

def is_negative(user_input):
    negative_keywords = ["nahi", "no", "nah", "not interested", "nope"]
    return any(word in user_input.lower() for word in negative_keywords)