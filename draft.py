from variable import Variable

def print_expression(exp):
    for comp in exp:
        print(comp, end='')

def is_num(comp:str):
    if isinstance(comp, float):
        return True
    component = comp.replace('-', '')
    return component.isdigit() or '.' in component

OPERATORS = ['+', '-', '*', '/', '^', '=', '(']
def deconstruct(expression:str): 
    try:
        current_comp = ''
        comps = [] # comps => components
        variable_exists = False
        equal_exists = False
        fixed_expression = expression.replace(' ', '')
        for char in fixed_expression:
            is_var = False
            if char in '0123456789.':
                current_comp += char
            elif char == '-' and len(current_comp) == 0:
                current_comp += char
            elif char.isalpha():
                variable_exists = True
                is_var = True
                val = 1
                if len(current_comp):
                    if is_num(current_comp):
                        val = float(current_comp)
                    else:
                        comps.append(current_comp)
                    current_comp = ''
                comps.append(Variable(char, val))
            elif char in OPERATORS + ['(', ')']:
                if len(current_comp):
                    if is_num(current_comp):
                        comps.append(float(current_comp))
                    else: 
                        comps.append(current_comp)
                current_comp = ''
                comps.append(char)
                if char == '=':
                    equal_exists = True
                
            else:
                raise ValueError(f'Invalid character: {char}')
    except ValueError as e:
        return(e)
        
    if len(current_comp):
        if not is_var:
            comps.append(float(current_comp))
        else: 
            comps.append(current_comp)
    if comps[-1] in OPERATORS:
        comps.pop()
    if comps[-1] == '=' and '=' not in comps[:-1]:
        equal_exists = False


    if variable_exists and equal_exists:
        type = 'equation'
    elif variable_exists:
        type = 'deco'
    else:
        type = 'basic'
    return type, comps
    
a = deconstruct('(1+2x)s 2 + 2x')
print_expression(a[1])

print('1')