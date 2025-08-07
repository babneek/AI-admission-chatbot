# AI Nursing College Admission Assistant

An intelligent, rule-based chatbot built with Streamlit to guide prospective students through the Nursing College admission process. The assistant provides clear, step-by-step information about eligibility, program details, fees, facilities, scholarships, and more—ensuring a professional and user-friendly experience.

## Features
- Clean Streamlit UI for interactive chat
- Handles multi-step admission queries
- Checks eligibility (Biology in 12th, age, PNT exam)
- Provides detailed program, fee, hostel, and scholarship info
- Explains recognition, clinical training, and seat availability
- Handles positive/negative user responses gracefully
- No LLM/API required—fully rule-based for reliability and speed

## Setup & Installation
1. **Clone the repository**
   ```bash
   git clone https://github.com/babneek/AI-admission-chatbot
   cd chatbot
   ```
2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the app**
   ```bash
   streamlit run app.py
   ```

## Usage Guide
- Launch the app and follow the assistant’s prompts.
- Respond to questions about your interest, eligibility, and information needs.
- Type 'exit' at any time to end the conversation.

## Conversation Flow
- **Greeting:** Welcomes and asks about admission interest
- **Eligibility Check:** Asks about Biology in 12th; explains requirement
- **Program Details:** Describes B.Sc Nursing program and offers more info
- **Fee Structure:** Provides detailed fee breakdown and installments
- **Hostel & Training:** Explains hostel and hospital training facilities
- **Location:** Shares college location and offers more info
- **Recognition:** Explains INC recognition and offers more info
- **Clinical Training:** Lists clinical training locations
- **Scholarships:** Describes available scholarships
- **Seats & Eligibility:** Shares seat count and full eligibility criteria
- **Response Handling:** Continues for positive responses, ends politely for negative

## Technical Details
- **Frontend:** Streamlit
- **Logic:** Rule-based, modular prompt functions (`prompts.py`)
- **Session Management:** Streamlit session state for chat history and flow
- **No LLM/API:** All responses are deterministic and template-driven

## Customization
- Edit `prompts.py` to update or localize responses
- Adjust conversation flow in `app.py` for new requirements

## Acknowledgements
- Inspired by the need for accessible education guidance
- Built with passion for improving student admission experiences