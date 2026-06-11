from calc.calc_utils import brackets
from calc.calc_utils import join_exp

def solve_basic(comps):
    path = []
    components = comps.copy()
    while '(' in components:
        sub_comps, start, stop = brackets(components)
        result, sub_path = operate(sub_comps)
        components[start:stop] = [result]
        path += sub_path
    
    result, sub_path = operate(components)
    components = result
    path += sub_path
    return str(components[0]), path

def operate(components):
    sub_path = []
    i = 0
    while len(components) > 1:
        description = None
        if '^' in components:
            if components[i+1] == '^':
                description = f"Perform Power {components[i]} ^ {components[i+2]}"
                components[i:i+3] = [components[i] ** components[i+2]]
        elif '*' in components or '/' in components:
            if components[i+1] == '*':
                description = f"Multiply {components[i]} * {components[i+2]}"
                components[i:i+3] = [components[i] * components[i+2]]
            elif components[i+1] == '/':
                description = f"Divide {components[i]} / {components[i+2]}"
                components[i:i+3] = [components[i] / components[i+2]]
        else:
            if components[i+1] == '+':
                description = f"Add {components[i]} + {components[i+2]}"
                components[i:i+3] = [components[i] + components[i+2]]
            elif components[i+1] == '-':
                description = f"Substract {components[i]} - {components[i+2]}"
                components[i:i+3] = [components[i] - components[i+2]]
        i+=1
        if i == len(components):
            i = 0
        if description:

            expression = join_exp(components)
            sub_path.append({"expression": expression,
                            "description": description})


    return components, sub_path

