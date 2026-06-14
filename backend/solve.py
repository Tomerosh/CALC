from fastapi import APIRouter, Form
# from db import save_log
from db import save_log
from calc.calc_utils import deconstruct, fix_result
from calc.simple import solve_basic
from calc.equation import solve_equation
from calc.complex import solve_complex

router = APIRouter()

# Main expression solving logic
@router.post('/solve/')
async def solve(expression:str = Form(...)):
    # try:
        result = 0
        path = []
        exp_type, comps = deconstruct(expression)
        if exp_type == "No Operators":
            result = expression
        elif exp_type == 'Simple Math':
            result, path = solve_basic(comps)
        elif exp_type == 'One Var equation':
            result, path = solve_equation(comps)
        elif exp_type in ['Complex', 'Simplify Exp']:
            result = solve_complex(expression)
            result = fix_result(result)
        else:
            result, path = 'Cannot Solve', []

        # Define conclusion for response
        conclusion = {
            "user_id": 1,
            "expression": expression,
            "type": exp_type,
            "result": result,
            "path": path
        }
        await save_log(conclusion)
        return conclusion
    # except Exception as e:
    #     print('ERROR: ', e,)
    #     return {"expression": expression,"result": 'Failed', "path": []}

def test(exp):
    response = solve(exp)
    path = response['path']
    for step in path:
        print(step['description'])
        print(step['expression'])
    print(response['result'])

# Simple
a1 = '5-5*5'
# Equation
b1 = '2x+4+4x=2+5x*10'
b2 = "10+5x+10-2x=50+5x+2+4x"
b3 = '2x+3*8+4x*5=5x/2+6x*2/3'
# Complex
c1 = '2x**2+5X'
c2 = "5x+5*5y = 4y+2x*4"
c3 = '2y+y/3+5=3y+4'
c4 = '2x+3*8+4x*5=5x^2'

# solve(b)
# print(solve(a))
# print(is_num('2.0x'))
# 5, '*', 'x'

# b = Variable('x', 1, -5)
# print(a**2)

# print(a**2)
# print(4*x**-2**2)


# print(type(Variable('x', '2', 1).value))
# print(Variable('x', 2) + Variable('x', 3, 2))
        
# import sympy

# x, y = sympy.symbols('x y')

# exp = 2 * x * 4 * x

# a = Variable('x', 4)
# # b = Variable('x', 2)
# # c = 'a'
# num = Number(2)
# test(c)