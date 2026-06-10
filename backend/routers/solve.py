from fastapi import APIRouter
from basics import solve_basic
from equation import solve_equation
from deco import solve_deco
from calc_utils import is_num, save_log, DIGITS, OPERATORS
from variable import Variable

router = APIRouter()

def deconstruct(expression:str): 
    current_comp = ''
    comps = [] # comps => components
    variable_exists = False
    equal_exists = False
    fixed_expression = expression.replace(' ', '')
    for char in fixed_expression:
        is_var = False
        if char in '0123456789.':
            current_comp += char
        elif char == '-' and len(current_comp) == 0:
            current_comp += char
        elif char.isalpha():
            variable_exists = True
            is_var = True
            if len(current_comp):
                if is_num(current_comp):
                    val = float(current_comp)
                else:
                    comps.append(current_comp)
                current_comp = ''
                comps.append(Variable(char, val))
        elif char in OPERATORS + ['(', ')']:
            if len(current_comp):
                if is_num(current_comp):
                    comps.append(float(current_comp))
                else: 
                    comps.append(current_comp)
            current_comp = ''
            comps.append(char)
            if char == '=':
                equal_exists = True
            
        else:
            raise ValueError()
        
    if len(current_comp):
        if not is_var:
            comps.append(float(current_comp))
        else: 
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