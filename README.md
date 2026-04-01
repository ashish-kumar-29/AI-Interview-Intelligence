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
