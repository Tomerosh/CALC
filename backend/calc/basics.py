def brackets(components):
    close = components.index(')')
    open = close - components[close::-1].index('(')
    sub_comps = components[open+1:close]
    return sub_comps, open, close+1
    

def solve_basic(comps):
    components = comps.copy()
    while '(' in components:
        sub_comps, start, stop = brackets(components)
        components[start:stop] = [operate(sub_comps)]
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

