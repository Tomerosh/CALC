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
            else:
                pass
                # power_ignore +=1
        elif '*' in side or '/' in side:
            i = 0
            while i < len(side):
                if side[i] == '*':
                    result = side[i-1] * side[i+1]
                    if result:
                        description = f"Multiply {side[i-1]} * {side[i+1]}"
                        side[i-1:i+2] = [result]
                        expression = side + ['='] + right_side
                        path.append({"expression": expression,
                                    "description": description})

                elif side[i] == '/':
                    result = side[i-1] / side[i+1]
                    if result:
                        description = f"Divide {side[i-1]} / {side[i+1]}"
                        expression = result
                        side[i-1:i+2] = [result]
                        expression = side + ['='] + right_side
                        path.append({"expression": expression,
                                    "description": description})
                i+=1
                # print(expression)
                # print(description)
                    
        else: 
            running = True
            i = 0
            while running:
                print(path)
                # print('i =', i)
                # Finish loop when only 1 component left
                if len(side) == 1:
                    return side
                # Check if comp is a var
                if isinstance(side[i], Variable):
                    # Create search list
                    sub = side[i+1:]
                    # Search for more vars
                    for j in range(len(sub)):
                        # Check if comp is a var
                        if isinstance(sub[j], Variable):
                            print('TEST')
                            print('i', i, 'j', j)
                            if j != 0:
                                # Perform Addition
                                if sub[j-1] == '+':
                                    description = f"Combined var {sub[j].name}"
                                    # Update comp list
                                    side[i] = side[i] + sub[j]
                                    print('TEST')
                                    print(side)
                                    print(sub)
                                    print(side[i], '+', sub[j])
                                    side.pop(i+j)
                                    side.pop(i+j)
                                    

                                    expression = str(side + ['='] + right_side) if side_name == 'left' else str(left_side + ['='] + side)
                                    path.append({"expression": expression,
                                                "description": description})
                                    break
                                # Substract
                                elif sub[j-1] == '-':
                                    # Update comp list
                                    side[i] = side[i] - sub[j]
                                    side.pop(i+j)
                                    side.pop(i+j)
                                    path.append({"expression": str(side + ['='] + right_side) if side_name == 'left' else str(left_side + ['='] + side),
                                                "description": f"Substracted var {sub[j].name}"})
                                    break
                            else:
                                description = f"Combined var {sub[j].name}"
                                # Update comp list
                                side[i] = side[i] + sub[j]
                                side.pop(i+j)
                                side.pop(i+j)
                                expression = str(side + ['='] + right_side) if side_name == 'left' else str(left_side + ['='] + side)
                                path.append({"expression": expression,
                                            "description": description})
                                break


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

                            elif sub[j-1] == '-':
                                side[i] = side[i] - sub[j]
                                side.pop(i+j)
                                side.pop(i+j)
                                path.append({"expression": str(side + ['='] + right_side) if side_name == 'left' else str(left_side + ['='] + side),
                                            "description": f"Substracted numbers"})

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
                elif side_name == 'right':
                    if isinstance(side[i], Variable):
                        left_side.append('+')
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
                            side.pop(i)
                        
                        path.append({"expression": str(left_side + ['='] + side),
                                    "description": f"Moved Number to left side"})
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
        print(description)
        print(expression)
        return side

                   
    # while '(' in left_side:
    #     sub_comps, start, stop = brackets(left_side)
    #     left_side[start:stop] = [operate(sub_comps)]
    while len(left_side) > 1 or len(right_side) > 1:
        print(path)
        if len(left_side) > 1:
            left_side = calc_side(left_side, 'left')
        if len(right_side) > 1:
            right_side = calc_side(right_side, 'right')
    return path, f'{left_side[0].name} = {right_side[0].value / left_side[0].value}'


        

