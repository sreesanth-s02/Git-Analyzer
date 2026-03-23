# 🚀 GitHub Profile Analyzer

A full-stack web application that analyzes GitHub profiles and provides intelligent insights based on different roles like **Frontend, Backend, Fullstack, and Data Science**.

---

## 🔍 Features

- 📊 Analyze any GitHub username
- 🎯 Role-based scoring (Frontend, Backend, Fullstack, Data Science)
- 🧠 Dual insights:
  - Recruiter Mode (evaluation-focused)
  - Student Mode (improvement-focused)
- ⚡ FastAPI backend for high performance
- 🎨 Interactive React frontend with charts and insights

---

## 🏗️ Tech Stack

### Backend
- Python
- FastAPI
- GitHub REST API

### Frontend
- React.js
- Chart.js (for visualizations)

---
## 📂 Project Structure

github-score/
├── backend/
│ ├── analyzer/
│ └── main.py
├── frontend/
│ ├── src/
│ └── public/
└── README.md


---

## ⚙️ Setup Instructions

### 1️⃣ Clone the repository

```bash
git clone https://github.com/sreesanth-s02/Git-Analyzer.git
cd Git-Analyzer

Backend Setup

cd backend
python -m venv venv
venv\Scripts\activate   # Windows
pip install -r requirements.txt
uvicorn main:app --reload

Backend runs at: http://127.0.0.1:8000

Frontend Setup

cd frontend
npm install
npm start

Frontend runs at: http://localhost:3000

API Endpoints
Analyze GitHub Profile

GET /analyze/{username}?role={role}&mode={mode}

Example:

http://127.0.0.1:8000/analyze/sreesanth-s02?role=frontend&mode=recruiter

🧠 How It Works
Fetches GitHub profile data using API
Extracts features like:
Repositories
Languages used
Activity
Applies scoring logic based on selected role
Generates insights for:
📌 Recruiters (evaluation)
📌 Students (improvement suggestions)

🏆 Use Cases
👨‍💼 Recruiters evaluating candidates
🎓 Students improving their GitHub profiles
💼 Portfolio enhancement tool
📜 License

This project is licensed under the MIT License.
