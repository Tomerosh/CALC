import sympy

from fastapi import APIRouter

# from db import save_log
from calc.calc_utils import deconstruct
from calc.basics import solve_basic
from calc.deco import solve_deco
from calc.equation import solve_equation


router = APIRouter()
@router.post('/solve')
def solve(expression:str):
    # try:
    result = 0
    path = []
    print(expression)
    type, comps = deconstruct(expression)
    print(comps)
    if type == 'basic':
        result = solve_basic(comps)
    elif type == 'deco':
        result = solve_deco(comps)
    else:
        path, result = solve_equation(comps)
        # result = 0
    conclusion = {
        "expression": expression,
        "result": result,
        "path": path,
        "user_id": 1,
        "type": type
    }
    # save_log(conclusion)
    return conclusion
    # except:
    #     return {"result": 'Error', "path": {}}

def test(exp):
    response = solve(exp)
    path = response['path']
    for step in path:
        print(step['description'])
        print(step['expression'])
    print(response['result'])


a = '5-5*5'
b = "5x+5*5y"
c = "10+5x+10-2x=50+5x+2+4x"
d = '2x**2+5X'
e = '2x+4+4x=2+5x*10'
f = '2y+y/3+5=3y+4'
g = '2x+3*8+4x*5=5x/2+6x*2/3'
# print(solve(a))
# print(is_num('2.0x'))
test(g)
# 5, '*', 'x'