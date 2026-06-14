from calc.calc_utils import OPERATORS, brackets, join_exp, calculate
from calc.terms import Number, Variable

def transfer(eq, i):
    equation = eq.copy()
    path = []
    j = 0
    while j < len(equation[i]):
        print(path)
        if i == 0:
            if isinstance(equation[i][j], Number):
                description = f'Transfer Number {equation[i][j]} right'
                if len(equation[1]):
                    equation[1].append('+')
                equation[1].append(equation[i][j]*-1)
                if j != 0:
                    equation[0].pop(j-1)
                    equation[0].pop(j-1)
                else:
                    equation[0].pop(0)
                    if equation[0][0] == '-':
                        equation[0][1] = equation[0][1] * -1
                    equation[0].pop(0)

                path.append({"expression": join_exp(equation[0] + ['='] + equation[1]), "description": description})
                j -= 1
        elif i == 1:
            if isinstance(equation[i][j], Variable):
                description = f'Transfer Variable {equation[i][j]} left'
                if len(equation[0]):
                    equation[0].append('+')
                equation[0].append(equation[i][j]*-1)
                if j != 0:
                    equation[1].pop(j-1)
                    equation[1].pop(j-1)
                else:
                    equation[1].pop(0)
                    if equation[1][0] == '-':
                        equation[1][1] = equation[0][1] * -1
                    equation[1].pop(0)
                path.append({"expression": join_exp(equation[0] + ['='] + equation[1]), "description": description})
                j -= 1
        j += 1
        
    return equation, path
def distribute(comps, operand, operator, op_side):
    result = []
    print('DISTRIBUTE: ', comps, operand)
    for comp in comps:
        res = comp
        if comp not in OPERATORS:
            if operator == '*':
                res = comp*operand
            else:
                if op_side == 'left':
                    res = operand/comp
                else:
                    res = comp/operand
        result.append(res)
    return result
        
def solve_equation(comps):
    print('Solving equation')
    path = [] # path memory
    equal_index = comps.index('=')
    left_side = comps[:equal_index].copy()
    right_side = comps[equal_index+1:].copy()
    equation = [left_side, right_side]
    
    while len(equation[0]) > 1 or len(equation[1]) > 1 or isinstance(equation[0][0], Number) or isinstance(equation[1][0], Variable):
        for i in range(len(equation)):
            while '(' in equation[i]:
                sub_comps, start, stop = brackets(comps)
                result, sub_path = calculate(sub_comps)
                for step in sub_path:
                    if i == 0:
                        step['expression'] = join_exp(equation[0][:start] + step['expression'] + equation[0][stop+1:] + ['='] + equation[1])
                    else:
                        step['expression'] = join_exp(equation[0] + ['='] + equation[1][:start] + step['expression'] + equation[1][stop+1:])
                if len(result) > 1:
                    equation[i][start:stop] = ['('] + result + [')']
                    if start > 0:
                        if equation[i][start-1] in '/\\*':
                            description = f'Distribute brackets {equation[i][start-2:stop]}'
                            result = distribute(equation[i][start+1:stop-1], equation[i][start-2], equation[i][start-1], 'left')
                            equation[i][start-2:stop] = result
                    if stop < len(equation[i]) -1:
                        if equation[i][stop+1] in '/\\*':
                            description = f'Distribute brackets {equation[i][start:stop+3]}'
                            result = distribute(equation[i][start+1:stop-1], equation[i][stop+1], equation[i][stop+1], 'right')
                            equation[i][start:stop+3] = result
                else:
                    equation[i][start:stop] = result


                path += sub_path
            result, sub_path = calculate(equation[i])
            for step in sub_path:
                if i == 0:
                    step['expression'] = join_exp(step['expression'] + ['='] + equation[1])
                else:
                    step['expression'] = join_exp(equation[0] + ['='] + step['expression'])
            path += sub_path
            equation[i] = result

            equation, sub_path = transfer(equation, i)
            path += sub_path
    if equation[0][0].value == 0:
        is_equal = equation[0][0] == equation[1][0]
        result = f'{equation[0][0]} {'=' if is_equal else '!='} {equation[1][0]}'
    else:
        equation[1].append('/')
        equation[1].append(Number(equation[0][0].value))
        equation[0][0].value = 1
        path.append({"expression": join_exp(equation[0] + ['='] + equation[1]),
                    "description": f"Isolate Variable {equation[0][0].name}"})
        result = f'{equation[0][0].name} = {equation[1][0] / equation[1][2]}'
        path.append({"expression": join_exp(result),
                    "description": f"Divide Numbers {equation[1][0]} / {equation[1][2]}"})
        

    return result, path