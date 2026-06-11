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
            if fixed_exp[-1] not in OPERATORS:
                fixed_exp += '*'
                
            fixed_exp += char.lower()
        else:
            fixed_exp += char
    if '=' in fixed_exp:
        left, right = fixed_exp.split('=')
        eq = Eq(sympify(left), sympify(right))
        return sympy.solve(eq)
    else:
        eq = sympify(fixed_exp)
        return eq
    
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

while True:
    print(solve_complex(input('Enter Expression: ')))