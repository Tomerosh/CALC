
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

# # Simple
# a1 = '5-5*5'
# # Equation
# b1 = '2y+y/3+5=3y+4'
# b2 = '2x+4+4x=2+5x*10'
# b3 = "10+5x+10-2x=50+5x+2+4x"
# b4 = '2x+3*8+4x*5=5x/2+6x*2/3'
# # Complex
# c1 = '2x**2+5X'
# c2 = "5x+5*5y = 4y+2x*4"
# c4 = '2x+3*8+4x*5=5x^2'
# c5 = '3x^3+5x^22-7x+12=4x^3-6x3+9'
# c6 = '5x^2y-3xy^2+2x-4y=7x^2+8y^2*3'
# c7 = '(4x^3-2x^2+5x)/x-3x*4=12x^2-4x+5'

# # Failed
# f1 = '(2x^2-4x+3)/(x-2)+5x*3=(4x^2+1)/(x+2)'
# f2 = '10%90'
