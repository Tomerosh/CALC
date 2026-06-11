from fastapi import APIRouter, FastAPI, Form, Request, status
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from sqlalchemy import create_engine, text
from backend import solve
import uvicorn

app = FastAPI()

app.mount("/static", StaticFiles(directory="../frontend/static"), name="static")

app.include_router(solve.router)
templates = Jinja2Templates(directory="../frontend/static")
engine = create_engine("sqlite:///my_database.db")


#הצגה של העמוד התחברות
@app.get("/", response_class=HTMLResponse)
async def login_page(request: Request):
    return templates.TemplateResponse("login_page.html", {"request": request})


router = APIRouter()
#הצגת עמוד הרשמה
@router.get("/sign_up", response_class=HTMLResponse)
async def sign_up_page(request: Request):
    return templates.TemplateResponse("sign_up_page.html", {"request": request})

#שליחת מידע והתחברות
@app.post("/login", response_class=HTMLResponse)
async def login(request: Request, Login_username: str = Form(...), Login_password: str = Form(...)):
    query = f"SELECT user_id, username FROM users WHERE username = '{Login_username}' AND password = '{Login_password}' "
    with engine.connect() as conn:
        user_record = conn.execute(text(query)).fetchone()
        if user_record:
            return templates.TemplateResponse(
                "main_page.html",
                {{"request": request, "username": db_username, "user_id": user_id}}
            )
        else:
            return "Username or Password is worng"
        
#שליחת מידע והרשמה
@app.post("/sign_up", response_class=HTMLResponse)
async def sign_up(request: Request, sign_up_username: str, sign_up_password: str):
    query = f'INSERT INTO users (username, password) VALUES ({sign_up_username}, {sign_up_password})'
    with engine.connect() as conn:
        conn.execute(text(query))
        conn.commit()
        return "Registration was successful, log in from the login form."
    

# #שליחת תרגיל 
# @app.post("/solve", response_class=HTMLResponse)
# async def solve_expression()
    

#צפייה בפרופיל האישי
app.get("/{username}", response_class=HTMLResponse)
async def show_profile(request: Request, username: str):
    user_query = f"SELECT user_id FROM users WHERE username = {username}"
    with engine.connect() as conn:
        user_record = conn.execute(text(user_query)).fetchone()
        current_user_id = user_record[0]
        history_query = f"SELECT expression, result FROM log WHERE user_id = {current_user_id} "
        user_logs = conn.execute(text(history_query)).fetchall()
        return templates.TemplateResponse(
            "profile.html", 
        {"request": request, "username": username, "logs": user_logs}
    )

uvicorn.run(app)