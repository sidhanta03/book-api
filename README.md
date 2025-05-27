# 📚 Book Management API (FastAPI + PostgreSQL + JWT)

This is a secure, scalable RESTful API for managing a collection of books with **user authentication**. It is built using **FastAPI** and **PostgreSQL**, with **JWT-based authentication** to protect routes. Authenticated users can perform **CRUD operations** on books.

---

## 🚀 Features

- ✅ User registration and login
- 🔐 JWT-based authentication and authorization
- 🔒 Secure password hashing using Bcrypt
- 📘 CRUD operations on books
- 📁 PostgreSQL integration using `psycopg2`
- 📄 Environment variable management with `.env`
- 🧪 Interactive API documentation via Swagger

---

## 🛠️ Tech Stack

| Layer       | Technology            |
|-------------|------------------------|
| Backend     | FastAPI (Python)       |
| Database    | PostgreSQL             |
| Auth        | JWT (`python-jose`)    |
| Hashing     | Bcrypt via `passlib`   |
| SQL Client  | `psycopg2`             |
| Env Loader  | `python-dotenv`        |

---

## 📦 Install Dependencies

Install all required packages:

```bash
pip install fastapi uvicorn psycopg2-binary python-dotenv python-jose passlib[bcrypt]



📘 Book CRUD Endpoints (Protected)

| Method | Endpoint      | Description      |
| ------ | ------------- | ---------------- |
| GET    | `/books`      | Get all books    |
| GET    | `/books/{id}` | Get a book by ID |
| POST   | `/books`      | Add a new book   |
| PUT    | `/books/{id}` | Update a book    |
| DELETE | `/books/{id}` | Delete a book    |


## ⚙️ Setup Instructions

1. Clone the repository:  
   ```bash
   git clone https://github.com/yourusername/fastapi-book-api.git
   cd fastapi-book-api
Create and activate a virtual environment:


python -m venv venv
source venv/bin/activate    # On Windows use: venv\Scripts\activate
Install dependencies:

pip install -r requirements.txt
Create a PostgreSQL database and user (using pgAdmin or psql).

Create a .env file in the root directory with these variables:

env
DATABASE_URL=postgresql://username:password@localhost:5432/dbname
SECRET_KEY=your_secret_key_here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

Run the FastAPI app:
uvicorn main:app --reload


