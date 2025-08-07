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