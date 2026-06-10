def solve_basic(comps):
    components = comps.copy()
    while '(' in components:
        close = components.index(')')
        open = close - components[close::-1].index('(')
        components[open:close+1] = [operate(components[open+1:close])]
    components = operate(components)
    return components

def operate(components):
    i = 0
    while len(components) > 1:
        if '^' in components:
            if components[i+1] == '^':
                components[i:i+3] = [components[i] ** components[i+2]]
        elif '*' in components or '/' in components:
            if components[i+1] == '*':
                components[i:i+3] = [components[i] * components[i+2]]
            elif components[i+1] == '/':
                components[i:i+3] = [components[i] / components[i+2]]
        else:
            if components[i+1] == '+':
                components[i:i+3] = [components[i] + components[i+2]]
            elif components[i+1] == '-':
                components[i:i+3] = [components[i] - components[i+2]]
        i+=1
        if i == len(components):
            i = 0

    return components[0]