

from fastapi import Request, HTTPException, APIRouter
from fastapi.responses import HTMLResponse
from sqlalchemy import text
from db import engine
from fastapi.templating import Jinja2Templates
from pathlib import Path

router = APIRouter()
BASE_DIR = Path(__file__).resolve().parent.parent
frontend_dir = BASE_DIR / "frontend"
templates = Jinja2Templates(directory=str(frontend_dir))

# @router.get("/{username}", response_class=HTMLResponse)
# async def show_profile(request: Request, username: str):
#     with engine.connect() as conn:
#         user_id = conn.execute(
#             text("SELECT user_id FROM users WHERE username = :name"), 
#             {"name": username}
#         ).fetchone()[0]

#     user_logs = conn.execute(
#             text("SELECT expression, result FROM log WHERE user_id = :uid"), 
#             {"uid": user_id}
#         ).fetchall()
    
#     return templates.TemplateResponse(
#             "profile.html", 
#             {"request": request, "username": username, "logs": user_logs}
#         )

from fastapi.responses import HTMLResponse

@router.get("/{username}", response_class=HTMLResponse)
async def show_profile(request: Request, username: str):
    # עוצרים את הבקשה הסמויה של הדפדפן לאייקון כדי שלא תקריס לנו את השרת
    if username == "favicon.ico":
        return HTMLResponse(status_code=204)
        
    with engine.connect() as conn:
        # שולפים את המשתמש
        user_record = conn.execute(
            text("SELECT user_id FROM users WHERE username = :name"), 
            {"name": username}
        ).fetchone()
        
        # רשת הביטחון: אם המשתמש לא קיים בטבלה (או שיש שגיאת כתיב)
        if not user_record:
            return HTMLResponse(content="<h1>אופס! המשתמש לא נמצא במסד הנתונים</h1>", status_code=404)
            
        user_id = user_record[0]
        
        # שולפים את ההיסטוריה
        user_logs = conn.execute(
            text("SELECT expression, result FROM log WHERE user_id = :uid"), 
            {"uid": user_id}
        ).fetchall()
        
        return templates.TemplateResponse(
            "profile.html", 
            {"request": request, "username": username, "logs": user_logs}
        )