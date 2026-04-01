# 🚀 AI Interview Intelligence Platform

An end-to-end **AI-powered interview preparation platform** that analyzes resumes, generates interview questions, evaluates spoken answers, and provides communication feedback with downloadable reports.

---

## 📌 Overview

AI Interview Intelligence helps candidates prepare for interviews by:

* 📄 Analyzing resumes against job descriptions
* 🤖 Generating AI-based interview questions
* 🎤 Conducting mock interviews with speech recognition
* 📊 Evaluating communication skills
* 📥 Generating professional PDF reports

---

## ✨ Features

### 🔍 Resume Analyzer

* Upload resume and paste job description
* Get:

  * Alignment Score
  * Strengths
  * Missing Skills
  * Recommendations

---

### 🤖 AI Interview Question Generator

* Generates:

  * Technical questions
  * Behavioral questions
  * Scenario-based questions

---

### 🎤 AI Interview Simulator

* One question at a time
* Voice recording using Speech Recognition
* Live transcription (word-by-word like ChatGPT)
* Controls:

  * Start / Stop / Reset / Submit

---

### 📊 Communication Analysis

* Words Per Minute (WPM)
* Filler Words Detection
* Fluency Score
* Clarity Score
* Confidence Score
* Overall Communication Score

---

### 📈 Interview Dashboard

* Progress bar for interview
* Real-time feedback
* AI-generated suggestions

---

### 📄 Professional PDF Report

Includes:

* Resume Analysis
* Interview Questions
* User Answers
* Communication Metrics
* Overall Evaluation
* AI Feedback

---

## 📸 Screenshots

## Starting Page
<img width="1889" height="1172" alt="Screenshot 2026-04-02 020538" src="https://github.com/user-attachments/assets/0aa38855-0525-4458-b895-be0d2850c48b" />
<img width="1871" height="1177" alt="Screenshot 2026-04-02 020552" src="https://github.com/user-attachments/assets/7c9cffd7-92a3-47a6-a427-1b866d973a63" />

## Resume Analysis
<img width="1902" height="1163" alt="Screenshot 2026-04-02 020927" src="https://github.com/user-attachments/assets/df9505ad-0e64-47e0-988a-2eb602349cf8" />

## Questions Generate
<img width="1912" height="810" alt="Screenshot 2026-04-02 020947" src="https://github.com/user-attachments/assets/889c7ad2-7d8b-41d4-8d1d-f3674b7eb3ad" />

## Interview Simulation
<img width="1342" height="1157" alt="Screenshot 2026-04-02 021218" src="https://github.com/user-attachments/assets/ac695b88-947e-46ff-a39c-353115a74be1" />

## Report
<img width="1045" height="1167" alt="Screenshot 2026-04-02 021408" src="https://github.com/user-attachments/assets/d73c332b-5557-44c9-a077-691eb47e62f7" />

## PDF Generate
<img width="726" height="1033" alt="Screenshot 2026-04-02 021446" src="https://github.com/user-attachments/assets/36e61e61-cc64-4321-a028-8737c7eae538" />
<img width="723" height="652" alt="Screenshot 2026-04-02 021453" src="https://github.com/user-attachments/assets/e620fe3c-957c-491e-97b8-5d8c5c81c60a" />






---

## 🛠️ Tech Stack

### Frontend

* HTML
* CSS
* JavaScript

### Backend

* FastAPI (Python)

### APIs / Tools

* Speech Recognition (Web API)
* jsPDF (PDF generation)

---

## ⚙️ Setup Instructions

### 1️⃣ Clone Repository

```
git clone https://github.com/your-username/ai-interview-intelligence.git
cd ai-interview-intelligence
```

---

### 2️⃣ Run Backend (FastAPI)

```
pip install fastapi uvicorn
python -m uvicorn app.main:app --reload
```

Backend runs at:

```
http://127.0.0.1:8000
```

---

### 3️⃣ Run Frontend

Just open:

```
index.html
```

in your browser.

---

## 🔐 Authentication

* Simple login/signup using localStorage
* Username stored and used across pages
* Session-based navigation

---

## 🧠 How It Works

```
Resume → AI Analysis → Question Generation → Interview Simulation
        ↓
Speech Recognition → Transcript → Metrics Calculation
        ↓
Communication Analysis → Report → PDF Download
```

---

## 📊 Communication Scoring Logic

Metrics are calculated using:

* WPM (Words Per Minute)
* Filler Word Count
* Sentence Structure
* Response Length

Final score is derived from:

```
Fluency + Clarity + Confidence
```

---

## 🚧 Future Improvements

* 🎯 Real AI evaluation using GPT
* 🎙️ Voice tone & emotion detection
* 📊 Radar chart analytics
* ☁️ Cloud deployment
* 👤 Full user dashboard
* 📈 Interview progress tracking

---

## 🎯 Use Cases

* Students preparing for interviews
* Job seekers improving communication skills
* Placement preparation platforms
* AI-based hiring simulations

---


---

## 👨‍💻 Author

**Ashish Kumar**

* Passionate about AI, Web Development, and Problem Solving
* Building real-world projects to solve interview preparation challenges

---

## ⭐ Support

If you like this project:

* ⭐ Star the repository
* 🍴 Fork it
* 📢 Share it

---

## 💡 Tagline

> “Practice smarter, not harder — with AI-powered interview intelligence.”
