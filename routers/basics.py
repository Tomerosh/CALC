def solve_basic(comps):
    components = comps.copy()
    i = 0
    while len(components) > 1:
        if '*' in components or '/' in components:
            if components[i+1] == '*':
                components[i:i+3] = [float(components[i]) * float(components[i+2])]
            elif components[i+1] == '/':
                components[i:i+3] = [float(components[i]) / float(components[i+2])]
        else:
            if components[i+1] == '+':
                components[i:i+3] = [float(components[i]) + float(components[i+2])]
            elif components[i+1] == '-':
                components[i:i+3] = [float(components[i]) - float(components[i+2])]
        i+=1
        if i == len(components):
            i = 0

    return components[0]