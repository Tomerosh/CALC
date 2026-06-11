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
        print(i)
        print(len(components))
        if '^' in components:
            if components[i] == '^':
                description = f"Perform Power {components[i-1]} ^ {components[i+1]}"
                components[i-1:i+2] = [components[i-1] ** components[i+1]]
                i-=1
        elif '*' in components or '/' in components:
            if components[i] == '*':
                description = f"Multiply {components[i-1]} * {components[i+1]}"
                components[i-1:i+2] = [components[i-1] * components[i+1]]
                i-=1
            elif components[i] == '/':
                description = f"Divide {components[i-1]} / {components[i+1]}"
                components[i-1:i+2] = [components[i-1] / components[i+1]]
                i-=1
        else:
            if components[i] == '+':
                description = f"Add {components[i-1]} + {components[i+1]}"
                components[i-1:i+2] = [components[i-1] + components[i+1]]
                i-=1
            elif components[i] == '-':
                description = f"Substract {components[i-1]} - {components[i+1]}"
                components[i-1:i+2] = [components[i-1] - components[i+1]]
                i-=1

        if i == len(components) -1:
            i = 0
        else:
            i+=1
        if description:

            expression = join_exp(components)
            sub_path.append({"expression": expression,
                            "description": description})


    return components, sub_path

