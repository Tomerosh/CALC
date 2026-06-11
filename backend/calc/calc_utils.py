from calc.terms import Variable, Number

# CONSTANTS
DIGITS = '0123456789.'
OPERATORS = ['+', '-', '*', '/', '^', '=', '(']

# Join components to string
def join_exp(comps):
    exp = ''
    for com in comps:
        exp += str(com) 
    return exp

#DELETE#
def print_expression(exp):
    for comp in exp:
        print(comp, end='')
    print('')

def is_num(comp:str):
    if isinstance(comp, float):
        return True
    component = comp.replace('-', '')
    return component.isdigit() or '.' in component

def add_var(var_dict, var, num):
    if not var_dict.get(var):
        var_dict[var] = 0
    var_dict[var] += num

# Find the most inner brackets
# Returns sub_list of components, start and stop indexes in og list
def brackets(components):
    close = components.index(')')
    open = close - components[close::-1].index('(')
    sub_comps = components[open+1:close]
    return sub_comps, open, close+1
    
# Operate all Powers (**) in expression
def power_exp(comps:list):
    new_comps = []
    i = -1
    powers_count = comps.count('^')
    for j in range(powers_count):
        i = comps.index('^', i+1)
        result = comps[i-1] ** comps[i+1]
        if result:
            new_comps = comps[:i-1] + [result] + comps[i+min(2, len(comps)-1):]
    return new_comps

def deconstruct(expression:str): 
    vars = set()
    current_comp = ''
    comps = [] # comps => components
    equal_exists = False
    fixed_expression = expression.replace(' ', '')
    for char in fixed_expression:
        is_var = False
        if char in '0123456789.':
            current_comp += char
        elif char == '-' and len(current_comp) == 0:
            current_comp += char
        elif char.isalpha(): # 2x + 1
            is_var = True
            if len(current_comp):
                val = current_comp
                current_comp = ''
                comps.append(Variable(char, val))
                vars.add(char)
            else:
                comps.append(Variable(char))
                vars.add(char)

        elif char in OPERATORS + ['(', ')']:
            if len(current_comp):
                if is_num(current_comp):
                    comps.append(Number(current_comp))
                else: 
                    var = Variable(current_comp)
                    comps.append(var)
                    vars.add(var.name)

            current_comp = ''
            comps.append(char)
            if char == '=':
                equal_exists = True
            
        else:
            raise ValueError()
        
    if len(current_comp):
        if not is_var:
            comps.append(Number(current_comp))
        else: 
            var = Variable(current_comp)
            comps.append(var)
            vars.add(var.name)

    if comps[-1] in OPERATORS:
        comps.pop()
    if comps[-1] == '=' and '=' not in comps[:-1]:
        comps.pop()
        equal_exists = False
    if len(vars) > 1 or (len(vars) and '^' in expression):
        exp_type = 'Complex'
    elif len(vars) and equal_exists:
        exp_type = 'One Var equation'
    elif len(vars):
        exp_type = 'Simplify Exp'
    else:
        exp_type = 'Simple Math'
    return exp_type, comps
    
# Handle results list 
def fix_results(results:list):
    if not isinstance(results, list):
        return str(results)
    fixed_result = ''
    result_count = len(results)
    for i in range(result_count):
        if isinstance(results[i], dict):
            for key in results[i].keys():
                fixed_result += f'{key} = {results[i][key]}'
        else:
            fixed_result += str(float(results[i]))
        fixed_result += " | " if i < result_count - 1 else ''
    return fixed_result
