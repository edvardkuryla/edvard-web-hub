![Python](https://img.shields.io/badge/python-3.10+-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.128.0-05998b.svg)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-latest-316192.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

# Edvard's Digital Service Hub

A robust backend platform for a personal brand website and digital service store. Built with **FastAPI**, **PostgreSQL**, and **JWT Authentication**.

## 🚀 Overview
This project serves as the core engine for my personal website. It combines a professional portfolio with a specialized e-commerce system where clients can browse and purchase digital services.

## 🛠 Tech Stack
* **Framework:** [FastAPI](https://fastapi.tiangolo.com/) (Asynchronous Python)
* **Database:** [PostgreSQL](https://www.postgresql.org/) with [SQLAlchemy ORM](https://www.sqlalchemy.org/)
* **Security:** [JWT (JSON Web Tokens)](https://jwt.io/) for secure authentication and [Argon2](https://argon2-cffi.readthedocs.io/en/stable/) for password hashing.
* **Environment:** [python-dotenv](https://saurabh-kumar.com/python-dotenv/) for secure configuration.

## ✨ Key Features
* **User Authentication:** Secure Sign-up and Login using JWT.
* **Service Catalog:** Backend support for listing digital services/products.
* **Secure API:** CORS-enabled middleware for frontend integration (React/Vue).
* **Data Integrity:** Automated database schema management with SQLAlchemy.

## ⚙️ Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git](https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git)
   cd YOUR_REPO_NAME

2. **Set up virtual environment:**
python -m venv venv
source venv/bin/activate  # On Linux/Fedora

3. **Install dependencies:**
pip install -r requirements.txt

4. **Environment Variables: Create a .env file in the root directory and add:**
DATABASE_URL=postgresql://user:password@localhost/dbname
SECRET_KEY=your_super_secret_key

5. **Run the server:**
uvicorn app.main:app --reload