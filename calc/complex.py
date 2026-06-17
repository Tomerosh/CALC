import sympy
from sympy import sympify, Eq

OPERATORS = ['+', '-', '*', '/', '^', '=']
def solve_complex(exp):
    print('Solving Complex Expression...')
    path = []
    fixed_exp = ''
    for char in exp:
        if char == '^':
            fixed_exp += '**' 
        elif char.isalpha():
            if len(fixed_exp):
                if fixed_exp[-1] not in OPERATORS:
                    fixed_exp += '*'
                
            fixed_exp += char.lower()
        else:
            fixed_exp += char

    
    if '=' in fixed_exp:
        left, right = fixed_exp.split('=')
        eq = Eq(sympify(left), sympify(right))
        result = sympy.solve(eq)
    else:
        result = sympify(fixed_exp)
    return result
    

