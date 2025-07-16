---
title: MediSyncAI
emoji: 🏥
colorFrom: pink
colorTo: yellow
sdk: streamlit
sdk_version: 1.35.0
app_file: main.py
pinned: false
license: mit
short_description: An AI-Powered Medical Assistant for Rural Clinics using Google Gemini + Streamlit
---

<!-- @format -->

# 🧠 MediSync.AI – AI-Powered Prescription Reader + Chatbot (Streamlit)

MediSync.AI is a GenAI-powered web application designed to **support rural healthcare centers** by automatically understanding **handwritten prescriptions** and providing **interactive medical insights** via a friendly chatbot. Built using **Google Gemini 2.0 Flash API** and **Streamlit**, this app bridges the information gap for patients and supports doctors with fast AI assistance.

---

## 📌 Features

- 📸 **Prescription Reader**  
  Upload an image of a handwritten prescription – the AI extracts medicine names, strengths, dosages, and notes.

- 💬 **Chatbot Assistant (MediSync)**  
  Chat with a knowledgeable and friendly AI to understand medications and general health queries.

- 📋 **Structured Output Format**  
  Extracted information is formatted into patient-friendly summaries using JSON parsing.

- ⚡ **Gemini-Powered**  
  Uses Google's **Gemini 2.0 Flash** LLM to power both the extraction and conversational layers.

---

## 🏥 Use Case: Rural Clinics

Patients in rural or underserved areas often struggle to interpret handwritten prescriptions. MediSync.AI helps by:

- Explaining medication names, dosage schedules, and durations.
- Offering basic conversational support for common medical queries.
- Supporting doctors with a simple tool to assist patient education.

---

## 🛠 Tech Stack

| Layer            | Tech Used                             |
| ---------------- | ------------------------------------- |
| 🌐 Frontend      | Streamlit                             |
| 🧠 GenAI Backend | Gemini 2.0 Flash (via Google APIs)    |
| ☁️ Deployment    | Streamlit Cloud / Localhost           |
| 🧪 Language      | Python                                |
| 📁 File Handling | `PIL`, `streamlit`, `dotenv`          |

---

## ⚙️ Gemini Features Used

- ✅ Prompt Engineering for Document Parsing
- ✅ Chat Memory for Contextual Conversations
- ✅ Structured JSON Response Generation
- ✅ Few-shot learning techniques
- ✅ Secure API Key via `st.secrets` or `.env`

---

## 📂 File Structure

mediSyncAI/

├── main.py
├── requirements.txt
├── .env
├── .gitignore
├── README.md
├── data/ # Optional image samples
│ └── sample1.jpg


---

## ▶️ How to Run (Locally)

1. **Clone the repo**  
```bash
git clone https://github.com/Sarita-021/mediSyncAI-App.git
cd mediSyncAI
```
---

## ▶️ How to Run (Locally)

1. **Clone the repo**  
```bash
git clone https://github.com/Sarita-021/mediSyncAI-App.git
cd mediSyncAI-App
```

2. Install dependencies
```bash
pip install -r requirements.txt
```

3. Add your Gemini API key
   Create a .env file:
```bash
GOOGLE_API_KEY = "your_actual_key_here"
```

4. Run the app
```bash
streamlit run main.py
```

5. Open in browser → Upload a prescription or ask medical questions!


## 📸 UI Preview
Upload Prescription

<img width="2880" height="1608" alt="image" src="https://github.com/user-attachments/assets/771d5002-ebd6-4942-b670-ad6797e5d22a" />
<img width="2860" height="1604" alt="image" src="https://github.com/user-attachments/assets/144a1d89-efd8-4585-9518-719fffd81323" />



## ⚠️ Disclaimer
MediSync.AI is intended for educational and assistive purposes only. It does not replace professional medical advice. Always consult a licensed medical professional for treatment and diagnosis.

## 👩‍💻 Author
Sarita | Gen AI Capstone 2025 | Tech Community Leader
