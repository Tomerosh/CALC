from fastapi import APIRouter, Request
from db import get_user, save_log
from calc.calc_utils import deconstruct, fix_result
from calc.simple import solve_basic
from calc.equation import solve_equation
from calc.complex import solve_complex

# Define router
router = APIRouter()

# Main expression solving logic
@router.post('/solve/')
async def solve(request:Request):
        req = await request.json()
        expression, solution, username = req.values()
    # try:
        # req = request.get('user_id')   
        # data = req.decode()
        # print('DATA:', req)

        # Set response vars
        result = 0
        path = []
        # Deconstruct expression to components
        exp_type, comps = deconstruct(expression)
        # Handle expression with no operators
        if exp_type == "No Operators":
            result = expression
        # Solve simple math
        elif exp_type == 'Simple Math':
            result, path = solve_basic(comps)
        # Solve equations with one variable
        elif exp_type == 'One Var equation':
            result, path = solve_equation(comps)
        # Solve anything else
        elif exp_type in ['Complex', 'Simplify Exp']:
            result = solve_complex(expression)
            result = fix_result(result)
        # If no expression type specified
        else:
            result, path = 'Cannot Solve', []
            
        # Check if solution correct
        if solution:
            print('SOLUTION')
        # solution_correct = is_correct(result, solution)

        user_id = get_user(username).user_id
        # Define conclusion for response
        conclusion = {
            "user_id": user_id,
            "expression": expression,
            "type": exp_type,
            "result": result,
            "path": path
        }
        # Save conclusion to log table
        await save_log(conclusion)

        return conclusion
    # except Exception as e:
    #     print('ERROR: ', e,)
    #     return {"expression": expression,"result": 'Failed', "path": []}
