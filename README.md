# 📘 TravelBook API — Basic Flask Project

A simple REST API built with **Flask** and **Flask-SQLAlchemy** for managing a list of travel destinations.  
Perfect for beginners learning backend development or anyone needing a lightweight API template.

---

## 🚀 Features

- 📌 SQLite database using SQLAlchemy ORM  
- 📌 API endpoints for retrieving travel destinations  
- 📌 Auto-creates database on first run  
- 📌 Clean, beginner-friendly Flask structure  
- 📌 Easy to extend into a full travel log or booking app  

---

## 📁 Project Structure

```plaintext
API-basic-project-about-travebook/
│
├── main.py               # Main Flask application
├── api.py                # (Optional / helper file)
├── requirements.txt      # Dependencies
├── instance/
│   └── travel.db         # Auto-generated SQLite database
└── API_env/              # Virtual environment (if using venv)
```

---

## 🛠️ Tech Stack

- **Python 3.x**
- **Flask**
- **Flask-SQLAlchemy**
- **SQLite**

---

## 📦 Installation & Setup

### 1. Clone the repository

git clone https://github.com/Hanzecode/API-basic-project-about-travebook.git
cd API-basic-project-about-travebook
### 2. (Optional but recommended) Create a virtual environment

#### macOS / Linux:
```bash
python3 -m venv API_env
source API_env/bin/activate
```
#### Window:
``` bash
python -m venv API_env
.\API_env\Scripts\activate
```
#### Run the API :

python main.py
