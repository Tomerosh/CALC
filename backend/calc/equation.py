from calc.calc_utils import brackets, DIGITS, print_expression
from calc.terms import Number, Variable

def power_exp(comps):
    new_comps = []
    i = -1
    powers_count = comps.count('^')
    for j in range(powers_count):
        i = comps.index('^', i+1)
        result = comps[i-1] ** comps[i+1]
        if result:
            new_comps = comps[:i-1] + [result] + comps[i+min(2, len(comps)-1):]
    return new_comps

# Solve equation logic
def solve_equation(comps: list):
    print('Solving equation')
    path = [] # path memory
    # Split list at '='
    equal_index = comps.index('=')
    left_side = comps[:equal_index]
    right_side = comps[equal_index+1:]

    def calc_side(side, side_name):
        if '^' in side: # Power
            result = power_exp(side)
            if result:
                side = result
                path.append({"expression": result,
                            "description": f"Powers Operated"})
                print(path[-1]['description'])
                print(path[-1]['expression'])
            else:
                pass
                # power_ignore +=1
        elif '*' in side or '/' in side:
                i = 0
                while i < len(side):
                    if side[i] == '*':
                        result = side[i-1] * side[i+1]
                        if result:
                            side[i-1:i+2] = [result]
                            path.append({"expression": result,
                                        "description": f"Multiply {side[i-1]} & {side[i+1]}"})
                            print(path[-1]['description'])
                            print(path[-1]['expression'])
                    elif side[i] == '/':
                        result = side[i-1] / side[i+1]
                        if result:
                            path.append({"expression": result,
                                        "description": f"Divide {side[i-1]} & {side[i+1]}"})
                            print(path[-1]['description'])
                            print(path[-1]['expression'])
                            side[i-1:i+2] = [result]
                    i+=1
        else: # 2x+4+4x=2+5x*10
            running = True
            i = 0
            while running:
                # print('i =', i)
                if len(side) == 1:
                    return side
                if isinstance(side[i], Variable):
                    sub = side[i+1:]
                    for j in range(len(sub)):
                        if isinstance(sub[j], Variable):
                            if sub[j-1] == '+':
                                side[i] = side[i] + sub[j]
                                side.pop(i+j)
                                side.pop(i+j)
                                path.append({"expression": str(side + ['='] + right_side) if side_name == 'left' else str(left_side + ['='] + side),
                                            "description": f"Combined var {sub[j].name}"})
                                print(path[-1]['description'])
                                print(path[-1]['expression'])
                            elif sub[j-1] == '-':
                                side[i] = side[i] - sub[j]
                                side.pop(i+j)
                                side.pop(i+j)
                                path.append({"expression": str(side + ['='] + right_side) if side_name == 'left' else str(left_side + ['='] + side),
                                            "description": f"Substracted var {sub[j].name}"})
                                print(path[-1]['description'])
                                print(path[-1]['expression'])


                elif isinstance(side[i], Number):
                    sub = side[i+1:]
                    j = 0
                    while j < len(sub):

                        if isinstance(sub[j], Number):
                            if sub[j-1] == '+':
                                side[i] = side[i] + sub[j]
                                side.pop(i+j)
                                side.pop(i+j)
                                sub = sub[:j-1] + sub[j+1:]
                                path.append({"expression": str(side + ['='] + right_side) if side_name == 'left' else str(left_side + ['='] + side),
                                            "description": f"Add numbers"})
                                print(path[-1]['description'])
                                print(path[-1]['expression'])
                            elif sub[j-1] == '-':
                                side[i] = side[i] - sub[j]
                                side.pop(i+j)
                                side.pop(i+j)
                                path.append({"expression": str(side + ['='] + right_side) if side_name == 'left' else str(left_side + ['='] + side),
                                            "description": f"Substracted numbers"})
                                print(path[-1]['description'])
                                print(path[-1]['expression'])
                        j+= 1
                if len(side) == 1:
                    return side
                if side_name == 'left':
                    if isinstance(side[i], Number):
                        right_side.append('+')
                        if i != 0:
                            if side[i-1] == '+':
                                right_side.append(side[i]*(-1))
                                side.pop(i-1)
                                side.pop(i-1)
                            elif side[i] == '-':
                                right_side.append(side[i]*(-1)*(-1))
                                side.pop(i-1)
                                side.pop(i-1)
                        elif i == len(side) -1 :
                            right_side.append(side[i]*(-1))
                            side.pop(i-1)
                            side.pop(i-1)
                        else:
                            right_side.append(side[i]*(-1))
                            side.pop(i)
                        path.append({"expression": str(side + ['='] + right_side) if side_name == 'left' else str(left_side + ['='] + side),
                                    "description": f"Moved Number to right side"})
                        print(path[-1]['description'])
                        print(path[-1]['expression'])
                elif side_name == 'right':
                    if isinstance(side[i], Variable):
                        left_side.append('+')
                        print(i)
                        if i != 0:
                            if side[i-1] == '+':
                                left_side.append(side[i]*(-1))
                                side.pop(i-1)
                                side.pop(i-1)
                            elif side[i] == '-':
                                left_side.append(side[i]*(-1)*(-1))
                                side.pop(i-1)
                                side.pop(i-1)
                        elif i == len(side) -1 :
                            left_side.append(side[i]*(-1))
                            side.pop(i-1)
                            side.pop(i-1)
                        else:
                            left_side.append(side[i]*(-1))
                            side.pop(i)
                        path.append({"expression": str(left_side + ['='] + side),
                                    "description": f"Moved Number to right side"})
                        print(path[-1]['description'])
                        print(path[-1]['expression'])
                if len(side) == 1:
                    return side
                if side[0] == '+':
                    side.pop(0)
                if side[0] == '-':
                    side[1] = side[1] * (-1)
                    side.pop(0)
                i += 1
                if i == len(side):
                    i = 0

                    
    # while '(' in left_side:
    #     sub_comps, start, stop = brackets(left_side)
    #     left_side[start:stop] = [operate(sub_comps)]
    while len(left_side) > 1 or len(right_side) > 1:
        if len(left_side) > 1:
            left_side = calc_side(left_side, 'left')
        if len(right_side) > 1:
            right_side = calc_side(right_side, 'right')
    return f'{left_side[0].name} = {right_side[0].value / left_side[0].value}'

# comps = [Variable('x'), '^',  2 , '+' , 4, '+',]
# x = Variable('x')
# result = power_exp(comps)
# print(result if result else False)
# print('\n', e[0].power)

# comps = ['2x', '*', '2', '+', '2x', '+', '4', '=', '4']
# solve_equation(comps)

        # if not left_side[i].isdigit():
        #     if i == 0:
        #         right_side.append('-')
        #         right_side.append(left_side[i])
        #         left_side.pop(i)
        #     elif left_side[i-1] == '+':
        #         right_side.append('-')
        #         right_side.append(left_side[i])
        #         left_side.pop(i)
        #         left_side.pop(i-1)
        #         i+=1                
        #     elif left_side[i-1] == '-':
        #         right_side.append('+')
        #         right_side.append(left_side[i])
        #         left_side.pop(i)
        #         left_side.pop(i-1)
        #         i+=1                
        #     elif left_side[i-1] == ''


        

