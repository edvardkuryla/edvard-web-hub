![Python](https://img.shields.io/badge/python-3.10+-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.128.0-05998b.svg)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-latest-316192.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

# Edvard’s Digital Service Hub

A modern backend platform for a personal brand website and digital service marketplace.  
Built with **FastAPI**, **PostgreSQL**, and **JWT authentication**.

---

## 🚀 Overview

This project is the core backend of my personal digital ecosystem.

It serves as a foundation for:
- a personal portfolio website
- a digital services marketplace
- secure user authentication
- future business logic and integrations

The system is intentionally designed to be clean, minimal, and extensible,
with a strong focus on scalability and long-term growth.

---

## 🛠 Tech Stack

- **Language:** Python 3.10+
- **Framework:** FastAPI
- **Database:** PostgreSQL
- **ORM:** SQLAlchemy
- **Authentication:** JWT (JSON Web Tokens)
- **Password Hashing:** Argon2
- **Environment Configuration:** python-dotenv

---

## ✨ Features

- 🔐 Secure user authentication with JWT
- 🧾 Base structure for managing digital services and products
- 🌐 API-first design (ready for React / Vue / mobile clients)
- 🛡 Modern security practices
- 🗄 Database schema management via SQLAlchemy
- 📄 Automatic API documentation (Swagger / OpenAPI)

---

## 📂 Project Structure

```text
.
├── app/
│   ├── main.py          # Application entry point
│   ├── database.py      # Database connection & session
│   ├── models/          # SQLAlchemy models
│   ├── routers/         # API route definitions
│   └── schemas/         # Pydantic schemas
├── .env # Make yourself
├── .gitignore
├── requirements.txt
└── README.md
```

---

## 🔮 Architecture & Future Plans

The project is structured to allow easy expansion without breaking core logic.

Planned improvements include:
- middleware-based authentication and authorization
- role-based access control
- service and order management
- improved security layers
- background tasks and integrations
- production-ready deployment setup

---

## ⚙️ Setup & Run

Create a virtual environment, install dependencies, configure environment variables,
ensure PostgreSQL is running, and start the server with:

uvicorn app.main:app --reload

The API will be available at:
http://127.0.0.1:8000

Interactive documentation:
http://127.0.0.1:8000/docs

---

## 📄 License

MIT License