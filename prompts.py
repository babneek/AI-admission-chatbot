import openai

def get_greeting():
    return (
        "नमस्ते! मैं LiaPlus AI का Nursing College Admission Assistant हूँ। "
        "क्या आप हमारे Nursing College में admission लेने में रुचि रखते हैं?"
    )

def get_interest_prompt():
    return "क्या आप हमारे Nursing College में admission लेना चाहते हैं?"

def get_biology_check_prompt():
    return "क्या आपने 12वीं कक्षा में Biology विषय लिया था?"

def get_biology_required_prompt():
    return "B.Sc Nursing में admission के लिए Biology अनिवार्य है।"

def get_program_details_prompt():
    return (
        "B.Sc Nursing एक full-time प्रोग्राम है जिसमें आपको theoretical और practical दोनों तरह की शिक्षा मिलेगी। "
        "क्या आप प्रोग्राम के बारे में और जानकारी चाहते हैं?"
    )

def get_fee_structure_prompt():
    return (
        "Fee Structure:\n"
        "• Tuition Fee: ₹60,000\n"
        "• Bus Fee: ₹10,000\n"
        "• Total Annual Fees: ₹70,000\n"
        "Fees तीन installments में जमा करनी होती है:\n"
        "1st Installment: ₹30,000 (admission के समय)\n"
        "2nd Installment: ₹20,000 (पहले semester के बाद)\n"
        "3rd Installment: ₹20,000 (दूसरे semester के बाद)"
    )

def get_hostel_facilities_prompt():
    return (
        "Hostel Facilities:\n"
        "• 24x7 पानी और बिजली\n"
        "• CCTV सुरक्षा\n"
        "• On-site warden\n"
        "Hospital training भी शामिल है, जिसमें आप असली मरीजों के साथ काम करेंगे।"
    )

def get_location_prompt():
    return (
        "हमारा कॉलेज दिल्ली में स्थित है। "
        "क्या आप location या आसपास के क्षेत्र के बारे में और जानना चाहेंगे?"
    )

def get_recognition_prompt():
    return (
        "कॉलेज Indian Nursing Council (INC), Delhi द्वारा मान्यता प्राप्त है। "
        "क्या आप मान्यता के बारे में और जानना चाहेंगे?"
    )

def get_clinical_training_prompt():
    return (
        "Clinical Training Locations:\n"
        "• District Hospital (Backundpur)\n"
        "• Community Health Centers\n"
        "• Regional Hospital (Chartha)\n"
        "• Ranchi Neurosurgery and Allied Science Hospital (Ranchi, Jharkhand)"
    )

def get_scholarship_prompt():
    return (
        "Scholarship Options:\n"
        "• Government Post-Matric Scholarship (₹18k-₹23k)\n"
        "• Labour Ministry Scholarships (₹40k-₹48k) (Labour Registration वालों के लिए)"
    )

def get_seats_prompt():
    return "Nursing प्रोग्राम में कुल 60 सीटें उपलब्ध हैं।"

def get_eligibility_prompt():
    return (
        "Eligibility Criteria:\n"
        "• 12वीं में Biology\n"
        "• PNT Exam पास होना चाहिए\n"
        "• आयु: 17 से 35 वर्ष"
    )

def get_positive_acknowledgement():
    return "बहुत अच्छा! आगे बढ़ते हैं।"

def get_negative_acknowledgement():
    return "कोई बात नहीं! अगर भविष्य में आपको जानकारी चाहिए हो तो हमसे संपर्क करें। धन्यवाद!"

def get_fallback_prompt():
    return "माफ़ कीजिए, मैं समझ नहीं पाया। कृपया अपना उत्तर दोबारा दें।"

def get_end_convo_prompt():
    return "आपका समय देने के लिए धन्यवाद! अगर आपको और जानकारी चाहिए तो फिर से संपर्क करें। शुभकामनाएँ!"

def get_info_prompt(field):
    prompts = {
        "name": "कृपया अपना नाम बताएं।",
        "email": "कृपया अपना ईमेल पता दर्ज करें।",
        "phone": "कृपया अपना मोबाइल नंबर दर्ज करें।",
        "city": "आप किस शहर से हैं?",
        # Add more fields as needed
    }
    return prompts.get(field, f"कृपया अपनी {field} जानकारी दें।")