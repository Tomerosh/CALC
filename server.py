from router import solve, user
from fastapi import FastAPI, Request
from fastapi.responses import FileResponse, HTMLResponse, Response, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

# Define fastapi app
app = FastAPI()

# Load static front files
app.mount("/static", StaticFiles(directory="./static"), name="static")
templates = Jinja2Templates(directory="./static")

# Link solve router to app
app.include_router(solve.router)
app.include_router(user.router)

# Display login page
@app.get("/", response_class=HTMLResponse)
async def login_page(request: Request):
    return templates.TemplateResponse(name="login.html", request=request)


@app.get('/favicon.ico')
def favicon():
    return FileResponse('./static/favicon.ico')
