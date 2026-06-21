<h1 align="center">CALC++</h1>

<p align="center">
  <img src="https://github.com/tomerosh/CALC/blob/master/Screenshot.jpeg?" width="900">
</p>

<p align="center">
  Mathematical Expression Solver • FastAPI • PostgreSQL
</p>

<p align="center">
  <a href="https://docs.google.com/presentation/d/13DIW3E8abDl5Cjbue7YFsqHidUqpnTOLAdRc_MTgz4U/edit?usp=sharing">📊 Project Presentation</a>
</p>

---

## Overview

CALC++ is a backend web application designed to solve mathematical expressions, manage user accounts, and store calculation history. The project demonstrates backend development concepts including API design, database integration, and mathematical expression processing.

### Key Features

- Mathematical expression solving
- User profile management
- Calculation history logging
- Database persistence
- RESTful API architecture

---

## Authors

- [**Aviv Woloss**](https://github.com/Aviv-woloss)
- [**Tomer Oshri**](https://github.com/Tomerosh)

---

## Tech Stack

### Backend
- FastAPI
- Uvicorn
- SQLAlchemy
- PostgreSQL (psycopg)
- Jinja2
- SymPy
- bcrypt
- python-multipart

---

## Installation

### Clone the Repository

```bash
git clone <repository-url>
cd calc
```

### Install Dependencies

```bash
pip install fastapi uvicorn sqlalchemy "psycopg[binary]" jinja2 python-multipart sympy bcrypt
```

### Run the Application

```bash
uvicorn server:app --reload
```

---

## API Endpoints

| Method | Endpoint | Description |
|----------|----------|----------|
| GET | `/` | Home page |
| POST | `/login` | User login |
| POST | `/sign_up` | User registration |
| POST | `/solve/` | Solve a mathematical expression |
| GET | `/{username}` | Display user profile |

---

## Project Structure

```text
CALC++
│
├── calc/
│   ├── calc_utils.py
│   ├── complex.py
│   ├── equation.py
│   ├── simple.py
│   └── terms.py
│
├── router/
│   ├── user.py
│   │   ├── POST /login
│   │   ├── POST /register
│   │   └── GET /{username}
│   │
│   └── solve.py
│     
├── static (Frontend static files)
│
├── db.py
└── server.py
    └── GET /
```

---

## Database Schema

### Users Table

| Column | Type |
|----------|----------|
| user_id | Integer |
| username | String |
| hashed_password | String |

### Log Table

| Column | Type |
|----------|----------|
| exp_id | Integer |
| user_id | Integer |
| expression | String |
| type | String |
| time | Time |
| result | String |
| score | String |

---

## Future Improvements

- JWT-based authentication
- Advanced expression parsing
- Calculation history dashboard
- API documentation
- Unit and integration testing
- Docker deployment support

---

## License

This project was created for educational purposes as part of the CyberPro Full-Stack Course.
