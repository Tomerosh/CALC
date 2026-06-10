|CALCULATOR++|
a Backend middle project for CyberPro Full-Stack Course
Created by: Aviv Woloss & Tomer Oshri

* BACKEND *
DEPENDENCIES:
fastapi
uvicorn
sqlalchemy 
psycopg2

Endpoints:
GET/ # Home page
POST/login # User register
POST/register # User register
GET/{username} # Show profile
POST/solve/{expression} # Solve expression

FILES:
-calc:
    -basics.py
    -calc_utils.py
    -deco.py
    -equation.py
    -variable.py
-router:
    -user.py 
        POST/login
        POST/register 
        GET/{username} 
    -solve.py
        POST/solve/{expression}
-db.py
    -save_data()
    -load_data()
-server.py
    GET/ # Home page

DATA TABLES:
    - users
        - user_id: Integer
        - username: String
        - hashed_password: String
    - log
        - exp_id: Integer
        - user_id: Integer
        - expression: String
        - type: String
        - time: Time
        - result: String




