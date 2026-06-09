from fastapi import APIRouter
from basics import solve_basic
from equation import solve_equation

router = APIRouter()

OPERATORS = ['+', '-', '*', '/', '^', '=', '(']

def deconstruct(equation:str): # equation => expression
    comps = [] # comps => components
    current_comp = ''

    variable_exists = False
    equal_exists = False
    fixed_equation = equation.replace(' ', '')
    for char in fixed_equation:
        if char in '0123456789.':
            current_comp += char
        elif char.isalpha():
            current_comp += char.lower()
            variable_exists = True
        elif char == '-' and len(current_comp) == 0:
            current_comp += char
        elif char in OPERATORS + ['(', ')']:
            comps.append(current_comp)
            current_comp = ''
            comps.append(char)
            if char == '=':
                equal_exists = True
        else:
            raise ValueError()
        
    if len(current_comp):
        comps.append(current_comp)
    if comps[-1] in OPERATORS:
        comps.pop()
    if comps[-1] == '=' and '=' not in comps[:-1]:
        equal_exists = False


    if variable_exists and equal_exists:
        type = 'equation'
    elif variable_exists:
        type = 'deco'
    else:
        type = 'basic'
    return type, comps
    

@router.post('/solve/{equation}')
def solve(equation:str):
    result = 0
    path = []
    type, comps = deconstruct(equation)
    if type == 'basic':
        solve_basic(comps)
    elif type == 'deco':
        pass
    else:
        solve_equation(comps)
    
    return {"result": result, "path": path}


a = '5 -5*5'
b = "5x+5*5y)="
c = "5x+10=50"
d = '2x**2+5X'
print(solve(c))