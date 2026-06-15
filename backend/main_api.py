from fastapi import APIRouter, FastAPI, Form, Request, status
from fastapi.responses import FileResponse, HTMLResponse, Response, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import create_engine, text
from db import create_user, get_user, load_log
import solve
# from profile_api import router as profile_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Use ["*"] to allow all origins during development
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.mount("/static", StaticFiles(directory="../frontend/static"), name="static")
app.include_router(solve.router)
# app.include_router(profile_router)

templates = Jinja2Templates(directory="../frontend/static")

#הצגה של העמוד התחברות
# Display login page
@app.get("/", response_class=HTMLResponse)
async def login_page(request: Request):
    return templates.TemplateResponse(name="login_page.html", request=request)

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
            headers = {'Location': '/solve'}
            return Response(content=str({"username": username, "password": password}), headers=headers, status_code=307)

    return "Username or Password is worng"
        
#הצגת עמוד הרשמה
# Display Sign up page
@app.get("/sign_up", response_class=HTMLResponse)
async def sign_up_page(request: Request):
    return templates.TemplateResponse(name="sign_up_page.html", request=request)

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
    
# Return solve page
@app.post('/solve')
async def get_solve(request:Request):
    # req = await request.json()
    # print(req)
    # name = req['username']
    # password = req['password']
    # db_user = get_user(name)
    # if db_user:
    #     if db_user.check_password(password):
    #         return templates.TemplateResponse(
    #         name="main_page.html",
    #         request=request
    #         )
    req = await request.body()
    data = req.decode().split('&')
    name = data[0].split('=')[1]
    password = data[1].split('=')[1]
    db_user = get_user(name)
    if db_user:
        if db_user.check_password(password):
            return templates.TemplateResponse(
            name="main_page.html",
            request=request,
            context={"username": name}
            )
    return RedirectResponse('/')

# @app.get("/solve", response_class=HTMLResponse)
# async def solve_redirect(request:Request):
#     return RedirectResponse('/')

@app.get('/favicon.ico')
def favicon():
    return FileResponse('../frontend/static/favicon.ico')


# צפייה בפרופיל האישי
@app.get("/{username}", response_class=HTMLResponse)
async def show_profile(username: str, request:Request):
    
    logs = load_log(username)
    return templates.TemplateResponse(
        name="profile.html", 
        request= request,
        context={"logs": logs[0].expression}
    )
# uvicorn.run(app)


# engine = create_engine("sqlite:///my_database.db")