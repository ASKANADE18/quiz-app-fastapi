# 🧠 Quiz App using FastAPI

An interactive multiple-choice quiz application built with **FastAPI** for the backend and **HTML + JavaScript** for the frontend.

## 🚀 Features

- 📋 Add single or multiple quiz questions
- 🎯 Take quizzes with real-time scoring
- 🔁 Reset quiz questions (for development/demo)
- 📊 Score calculation via backend (or local fallback)
- 🌐 Clean, responsive frontend served via FastAPI
- 🔧 Modular structure with separate routes, models, and schemas

---

## 🛠️ Tech Stack

- **Backend:** FastAPI, SQLAlchemy, Pydantic
- **Frontend:** HTML, CSS, JavaScript
- **Database:** SQLite (easy to use for local dev)
- **Server:** Uvicorn

---

## 📁 Project Structure
<img width="500" alt="Screenshot 2025-06-13 at 9 35 16 PM" src="https://github.com/user-attachments/assets/586b77a4-fad0-4b23-8b2c-48b9dc7322fe" />

## 📌 API Endpoints

| Method | Endpoint        | Description                        |
|--------|------------------|------------------------------------|
| GET    | `/quiz/`         | Fetch all questions                |
| POST   | `/quiz/`         | Add a single quiz question         |
| POST   | `/quiz/bulk`     | Add multiple questions at once     |
| POST   | `/quiz/submit`   | Submit answers and get score       |
| POST   | `/quiz/reset`    | Delete all quiz questions          |
| GET    | `/`              | Load the interactive quiz UI       |

---

## 🧪 Running the Project Locally

```bash
# 1. Clone the repository
git clone https://github.com/your-username/quiz-app-fastapi.git
cd quiz-app-fastapi

# 2. Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate   # On Windows use: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the FastAPI server
uvicorn main:app --reload

# Visit: http://127.0.0.1:8000/

