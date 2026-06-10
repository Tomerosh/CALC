
# CONSTANTS
DIGITS = '0123456789.'
OPERATORS = ['+', '-', '*', '/', '^', '=', '(']

# OPERATION = {
#     '+':
# }


def is_num(comp:str):
    if isinstance(comp, float):
        return True
    component = comp.replace('-', '')
    return component.isdigit() or '.' in component

def add_var(var_dict, var, num):
    if not var_dict.get(var):
        var_dict[var] = 0
    var_dict[var] += num

def split_num_var(comp):
    num = ''
    variable = ''
    for char in comp:
        if char in DIGITS or char == '-':
            num += char
        else:
            variable += char
    return num, variable

            
            

            


