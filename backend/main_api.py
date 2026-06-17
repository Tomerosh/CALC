import solve
from fastapi import FastAPI, Form, Request, Depends
from fastapi.encoders import jsonable_encoder
from fastapi.responses import FileResponse, HTMLResponse, Response, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from db import Log, User, create_user, get_db, get_user

# Define fastapi app
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Use ["*"] to allow all origins during development
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load static front files
app.mount("/static", StaticFiles(directory="../frontend/static"), name="static")
templates = Jinja2Templates(directory="../frontend/static")

# Link solve router to app
app.include_router(solve.router)


# Display login page
@app.get("/", response_class=HTMLResponse)
async def login_page(request: Request):
    return templates.TemplateResponse(name="login_page.html", request=request)

# Login user
@app.post("/login", response_class=HTMLResponse)
async def login(request: Request, username: str = Form(...), password: str = Form(...)):
    db_user = get_user(username)
    if db_user:
        if db_user.check_password(password):
            headers = {'Location': '/solve'}
            return Response(content=str({"username": username, "password": password}), headers=headers, status_code=307)

    return "Username or Password is worng"
        
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
    
    req = await request.body()
    data = req.decode().split('&')
    name = data[0].split('=')[1]
    password = data[1].split('=')[1]
    db_user = get_user(name)
    if db_user:
        if db_user.check_password(password):
            user_id = db_user.user_id
            return templates.TemplateResponse(
            name="main_page.html",
            request=request,
            context={"username": name, "user_id": user_id}
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
async def show_profile(username: str, request:Request, db: Session = Depends(get_db)):
    user_data = db.query(User).where(User.username == username).first()
    if user_data:
        logs = db.query(Log).where(Log.user_id == user_data.user_id).all()
        logs_json = jsonable_encoder(logs)

        return templates.TemplateResponse(
            name="profile.html", 
            request= request,
            context={"logs": logs_json}
        )
    else:
        return 'user not found'
# uvicorn.run(app)


# engine = create_engine("sqlite:///my_database.db")