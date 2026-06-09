REQUIRMENTS:
pip install sqlalchemy psycopg2

FILES:
data (tables):
    - users
    - log
BACKEND:
server.py
router:
    -user.py 
        /login
        /register -save_data('users', {"username": "aviv", "password":123})
        /{username} # Show profile
    -logic.py
        /basic_math -save_data('log', {"equation": x+2})
        /equation
        /decompoition

        components()
    -util
        save_data(table, data)
            if table==users
                data['username']
        load_data()



# Questions
# תרגילים מסוגים מוגדרים מראש: היוזר בוחר סוג תרגיל לפני שמזין את התרגיל ?
# פרופיל אישי- פרטי המשתמש או הפעולות שביצע?
# אבטחה - סיסמא בכל פעולה או טוקן?
# ספרייה רלוונטית? האם כדאי להשתמש בsympy כי הוא מראה את הפתרון הסופי בלבד. 
# הצגת שלבי הפתרון: כמה להראות ?
2x + 1 + 6 + 4x
6x + 7
או
2x + 1 + 6 + 4x
2x + 7 + 4x
6x + 7

# בהרחבות: גרף התקדמות - לתת "נקודות" למשתמש על כל תשובה נכונה ?
# המלצה על נושאים לתרגול לפי הצלחות של המשתמש ?

# איזה עוד סוגי תרגילים ? שברים, אחוזים
