from fastapi import APIRouter, FastAPI, Form, Request, status
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from sqlalchemy import create_engine, text
from db import create_user, get_user
import solve

app = FastAPI()

app.mount("/static", StaticFiles(directory="../frontend/static"), name="static")
app.include_router(solve.router)

templates = Jinja2Templates(directory="../frontend/static")

#הצגה של העמוד התחברות
# Display login page
@app.get("/", response_class=HTMLResponse)
async def login_page(request: Request):
    return templates.TemplateResponse(name="login_page.html", request=request)

#הצגת עמוד הרשמה
# Display Sign up page
@app.get("/sign_up", response_class=HTMLResponse)
async def sign_up_page(request: Request):
    return templates.TemplateResponse(name="sign_up_page.html", request=request)

#שליחת מידע והתחברות
@app.post("/login", response_class=HTMLResponse)
async def login(request: Request, username: str = Form(...), password: str = Form(...)):
    
    # query = f"SELECT user_id, username FROM users WHERE username = '{Login_username}' AND password = '{Login_password}' "
    # with engine.connect() as conn:
    #     user_record = conn.execute(text(query)).fetchone()
    #     if user_record:
    db_user = get_user(username)
    if db_user:
        if db_user.check_password(password):
            return templates.TemplateResponse(
                name="main_page.html",
                request=request,
            )

    return "Username or Password is worng"
        
#שליחת מידע והרשמה
@app.post("/sign_up", response_class=HTMLResponse)
async def sign_up(request: Request, username: str = Form(...), password: str = Form(...)):
    # query = f'INSERT INTO users (username, password) VALUES ({username}, {password})'
    # with engine.connect() as conn:
    #     conn.execute(text(query))
    #     conn.commit()
    if get_user(username):
        return "Username already in use"
    
    create_user(username, password)
    return "Registration was successful, log in from the login form."
    

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

# uvicorn.run(app)


# engine = create_engine("sqlite:///my_database.db")