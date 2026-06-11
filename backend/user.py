from fastapi import APIRouter

router = APIRouter()

@router.get('/{username}')
def get_user():
    return {"username": "aviv", "age": "ex@gmail.com"}
