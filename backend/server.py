from fastapi import FastAPI
from routers import user
from routers import solve

app = FastAPI()

app.include_router(user.router)
app.include_router(solve.router)

@app.get('/')
def home():
    return 'HOME'