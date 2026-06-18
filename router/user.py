from fastapi import APIRouter, Form, Request, Response, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from db import create_user, get_user, load_logs

# Define router
router = APIRouter()
templates = Jinja2Templates(directory="./static")

# Login user
@router.post("/login", response_class=HTMLResponse)
async def login(request: Request, username: str = Form(...), password: str = Form(...)):
    db_user = get_user(username)
    if db_user:
        if db_user.check_password(password):
            headers = {'Location': '/solve'}
            return Response(content=str({"username": username, "password": password}), headers=headers, status_code=307)

    return Response(status_code=status.HTTP_401_UNAUTHORIZED)
        
# Display Sign up page
@router.get("/sign_up", response_class=HTMLResponse)
async def sign_up_page(request: Request):
    return templates.TemplateResponse(name="sign_up.html", request=request)

# Handle user registration
@router.post("/sign_up", response_class=HTMLResponse)
async def sign_up(request: Request, username: str = Form(...), password: str = Form(...)):
    if get_user(username):
        return Response(status_code=status.HTTP_409_CONFLICT)
    
    create_user(username, password)
    return Response(status_code=status.HTTP_201_CREATED)
    
# צפייה בפרופיל האישי
@router.get("/{username}", response_class=HTMLResponse)
async def show_profile(username: str, request:Request):
    user = get_user(username)
    if user:
        logs = load_logs(username)
        logs_json = jsonable_encoder(logs)
        user_data = {
            "username": username,
            "logs": logs_json
        }
        return templates.TemplateResponse(
            name="profile.html", 
            request= request,
            context={"user_data": user_data}
        )
    else:
        return 'user not found'
    
    
# Return solve page
@router.post('/solve')
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
            name="solve.html",
            request=request,
            context={"username": name, "user_id": user_id}
            )
    return RedirectResponse('/')
