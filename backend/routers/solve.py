from fastapi import APIRouter
from basics import solve_basic
from equation import solve_equation
from deco import solve_deco
from calc_utils import deconstruct, save_log

router = APIRouter()
@router.post('/solve/{expression}')
def solve(expression:str):
    result = 0
    path = []
    print(expression)
    type, comps = deconstruct(expression)
    if type == 'basic':
        result = solve_basic(comps)
    elif type == 'deco':
        result = solve_deco(comps)
    else:
        result = solve_equation(comps)
    conclusion = {
        "expression": expression,
        "result": result,
        # "path": path,
        "user_id": 1,
        "type": type
    }
    save_log(conclusion)
    return conclusion

a = '5-5*5'
b = "5x+5*5y"
c = "5x+10=50"
d = '2x**2+5X'
# print(solve(a))
# print(is_num('2.0x'))
print(deconstruct(b))
# 5, '*', 'x'