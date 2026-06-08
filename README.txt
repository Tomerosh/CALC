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
    -util
        save_data(table, data)
            if table==users
                data['username']
        load_data()
