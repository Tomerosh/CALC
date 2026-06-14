# from tempfile import template

# from fastapi import APIRouter, Request
# from fastapi.responses import HTMLResponse
# from sqlalchemy import text


# router = APIRouter()
# #הצגת עמוד הרשמה
# @router.get("/sign_up", response_class=HTMLResponse)
# async def sign_up_page(request: Request):
#     return template.TemplateResponse("sign_up_page.html", {"request": request})

# #שליחת מידע והתחברות
# @app.post("/login", response_class=HTMLResponse)
# async def login(request: Request, Login_username: str = Form(...), Login_password: str = Form(...)):
#     query = f"SELECT user_id, username FROM users WHERE username = '{Login_username}' AND password = '{Login_password}' "
#     with engine.connect() as conn:
#         user_record = conn.execute(text(query)).fetchone()
#         if user_record:
#             return templates.TemplateResponse(
#                 "main_page.html",
#                 {{"request": request, "username": db_username, "user_id": user_id}}
#             )
#         else:
#             return "Username or Password is worng"
        
# #שליחת מידע והרשמה
# @app.post("/sign_up", response_class=HTMLResponse)
# async def sign_up(request: Request, sign_up_username: str, sign_up_password: str):
#     query = f'INSERT INTO users (username, password) VALUES ({sign_up_username}, {sign_up_password})'
#     with engine.connect() as conn:
#         conn.execute(text(query))
#         conn.commit()
#         return "Registration was successful, log in from the login form."
    