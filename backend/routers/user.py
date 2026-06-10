from fastapi import APIRouter
form backend import users_utils
router = APIRouter()

@router.get('/{username}')
def get_user():
    return {"username": "aviv", "age": "ex@gmail.com"}


@router.post('/{username}:{password}')
def log_in():
    if {username} not in user_db:
        return{"massage" : "The user dosen't exsist"}
    else:
        if user_db.get({username}) == hash_password({password}):
            return{"wellcom back": "{username}"}
        else: 
            return{"massage" : {"The password uncurrect"}}


@router.post('/{username}:{password}')
def register():
    if {username} in user_db:
        return{"massage" : "The user already exsist"}
    else:
        user_db[username] = [hash_password({password})]
    return{"wellcom": "{username}"}