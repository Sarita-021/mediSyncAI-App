import os
import json
import re
import streamlit as st
from PIL import Image
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Configure GenAI
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel("gemini-2.0-flash")

# Image Extraction Prompt
prompt = """
You are a medical assistant AI. Extract structured data from this handwritten prescription image.

Here are some common medicines, strength and usage:
Medicine Name	Strength Example	Usage
Paracetamol	500mg, 650mg	Pain relief, fever
Amoxicillin	250mg, 500mg	Antibiotic
Azithromycin	250mg, 500mg	Antibiotic
Ibuprofen	400mg, 600mg	Pain relief, anti-inflammatory
Cefixime	200mg	Antibiotic
Pantoprazole	40mg	Acidity, ulcer prevention
Domperidone	10mg	Anti-nausea
Metformin	500mg, 1000mg	Diabetes
Amlodipine	5mg	Blood pressure
Cetirizine	10mg	Anti-allergy
Ranitidine	150mg	Acidity
Dolo 650	650mg	Fever, pain relief
Ondansetron	4mg, 8mg	Anti-vomiting
Levocetirizine	5mg	Allergy
Losartan	50mg	Blood pressure
Clavulanic Acid	125mg (with Amox)	Antibiotic combo
Salbutamol	Inhaler/Syrup	Asthma

Focus on extracting:
- Patient name
- List of medicines prescribed
- Strength (mg, ml, etc.)
- Dosage frequency (e.g., 1-0-1)
- Duration
- Additional notes

Return ONLY this JSON format:
{
  "patient_name": "",
  "medicines": [
    {
      "name": "",
      "strength": "",
      "dosage_frequency": "",
      "duration": ""
    }
  ],
  "notes": ""
}
If any field is missing, return it as null.
"""

# Chat system prompt
chat_system_prompt = """
You are a friendly and knowledgeable AI medical assistant named MediSync.
You help patients understand their prescriptions, medications, and basic symptoms.

Example:
Q: I was prescribed Paracetamol 650mg. What is it for?
A: Paracetamol is used to relieve fever and mild to moderate pain, such as headaches or body aches.

Always include this disclaimer: "Please consult a licensed medical professional before taking any medication."
"""

chat_session = model.start_chat(history=[])
chat_session.send_message(chat_system_prompt)


# Streamlit UI
st.set_page_config(page_title="MediSync.AI", layout="wide")

st.markdown("# 🧠 MediSync.AI - Prescription Reader + Chatbot")

tab1, tab2 = st.tabs(["📸 Upload Prescription", "💬 Chat with MediSync"])

# --- Tab 1: Image Upload ---
with tab1:
    st.markdown("### Upload Prescription Image")
    image = st.file_uploader("Choose an image", type=["png", "jpg", "jpeg"])

    if st.button("Extract Info"):
        if image:
            image_pil = Image.open(image)
            response = model.generate_content([prompt, image_pil])

            text = response.text.strip()
            if text.startswith("```json"):
                text = re.sub(r"```json|```", "", text).strip()

            try:
                data = json.loads(text)
                st.markdown("### 👩‍⚕️ Prescription Summary")

                st.write(f"**Patient Name:** {data.get('patient_name') or 'N/A'}")

                st.write("**Medicines Prescribed:**")
                for med in data.get("medicines", []):
                    st.markdown(f"- 💊 **{med.get('name', 'Unknown')}** – {med.get('strength', 'N/A')} – Dosage: {med.get('dosage_frequency', 'N/A')} – Duration: {med.get('duration', 'N/A')}")

                st.write(f"**Notes:** {data.get('notes') or 'None'}")

            except Exception as e:
                st.error(f"Error parsing JSON response:\n{text}")
        else:
            st.warning("Please upload a prescription image.")

# --- Tab 2: Chatbot ---
with tab2:
    st.markdown("### MediSync-AI Chatbot")
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    # Chat messages container
    chat_container = st.container()
    with chat_container:
        for msg in st.session_state.chat_history:
            with st.chat_message(msg["role"]):
                st.markdown(msg["content"])

    # Chat input at bottom
    user_input = st.chat_input("Type your medical question here...")

    if user_input:
        st.session_state.chat_history.append({"role": "user", "content": user_input})
        with chat_container:
            with st.chat_message("user"):
                st.markdown(user_input)

        try:
            ai_response = chat_session.send_message(user_input)
            reply = ai_response.text
        except Exception as e:
            reply = f"❌ Error: {e}"

        st.session_state.chat_history.append({"role": "assistant", "content": reply})
        with chat_container:
            with st.chat_message("assistant"):
                st.markdown(reply)
        st.rerun()

