from fastapi import APIRouter

router = APIRouter()

@router.post('/basic_math/{equation}')
def solve(equation:str):
    result = 0
    path = []
    


    return {"result": result, "path": path}