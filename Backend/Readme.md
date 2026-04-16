# 🚀 School Trip Payment System (Backend - FastAPI)

This is the backend service for the School Trip Registration & Payment System built using **FastAPI, SQLModel, and a legacy payment integration adapter**.

---

## 📁 Tech Stack
- FastAPI
- SQLModel (ORM)
- PostgreSQL / SQLite (configurable)
- Pydantic validation
- Uvicorn
- Legacy Payment API Integration

---

## 🏗️ Architecture
app/
│
├── api/ # Controllers / Routes
├── services/ # Business logic
├── repositories/ # DB layer
├── models/ # SQLModel entities
├── integrations/ # Legacy payment adapter
├── core/ # Config + exceptions + middleware



---

## 🚀 How to Run

### 1. Create virtual environment
```bash
python3 -m venv venv

### 2. Activate Environment
source venv/bin/activate

### 3. Install Dependencies
pip install -r requirements.txt


### 3. Run Server
uvicorn app.main:app --reload