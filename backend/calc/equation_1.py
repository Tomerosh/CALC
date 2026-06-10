from calc_utils import is_num, add_var
DIGITS = '0123456789.'

'20'
'20.0'
'-20'
'-'
# 

# def split_num_var(comp):
#     num = ''
#     variable = ''
#     for char in comp:
#         if char in DIGITS or char == '-':
#             num += char
#         else:
#             variable += char
#     return num, variable
def combine(comps):
    for i in range(len(comps)):
        comps[i]
def solve_equation(comps: list):
    print('Solving equation')
    equal_index = comps.index('=')
    left_side = comps[:equal_index]
    print(left_side)                    

    right_side = comps[equal_index+1:]
    i = 0
    # 2 * 4 * x + 5 + x
    vars = {}
    
    while i < len(left_side):
        print(i)
        print(left_side)
        print(vars)
        if '^' in left_side: # Power
            if left_side[i] == '^':
                if is_num(left_side[i-1]):
                    if is_num(left_side[i+1]): # Two numbers
                        left_side[i-1:i+2] = [float(left_side[i-1]) ** float(left_side[i+1])]

        elif '*' in left_side or '/' in left_side: 
            if left_side[i] == '*':
                if is_num(left_side[i-1]):
                    if is_num(left_side[i+1]): 
                        left_side[i-1:i+2] = [float(left_side[i-1]) * float(left_side[i+1])]
                    else:
                        add_var(vars, left_side[i+1], left_side[i-1])
                else: # Left in variable
                    if is_num(left_side[i+1]):
                        add_var(vars, left_side[i-1], left_side[i+1])
                    else: # two vars
                        i+=1
                        continue
                        # if variable == var2:
                        #     left_side[i:i+2] = [str(float(num) * float(num2)) + variable]
                        # else:
                        #     i+=1
                        #     continue
            if left_side[i] == '/':
                if is_num(left_side[i-1]):
                    if is_num(left_side[i+1]):
                        left_side[i:i+2] = [float(left_side[i-1]) / float(left_side[i+1])]
                    else:
                        add_var(vars, left_side[i-1], left_side[i+1])
                else:
                    if is_num(left_side[i+1]):
                        add_var(vars, left_side[i+1], left_side[i-1])
                    else: 
                        # num2, var2 = split_num_var(left_side[i+1])
                        # if variable == var2:
                        #     left_side[i:i+2] = [str(float(num) / float(num2)) + variable]
                        # else:
                        #     i+=1
                        #     continue
                        i+=1
                        continue
            else:
                i+=1
                continue
            
        else:
            pass
            # if is_num(left_side[i]):
            #     right_side.append('-')
            #     right_side.append(left_side[i])

        i+=1
        if i == len(left_side):
            i = 0

# 2 * x + x + 4 + 10 + 4 * x


# comps = [2.0, '*' ,'x', '*', 2.0, '+', 2.0, '*', 'x', '+', 'x', '=', '4']
comps = ['2x', '*', 2, '+', 2.0, '*', 'x', '+', 'x', '=', '4']
# solve_equation(comps)


        # if not left_side[i].isdigit():
        #     if i == 0:
        #         right_side.append('-')
        #         right_side.append(left_side[i])
        #         left_side.pop(i)
        #     elif left_side[i-1] == '+':
        #         right_side.append('-')
        #         right_side.append(left_side[i])
        #         left_side.pop(i)
        #         left_side.pop(i-1)
        #         i+=1                
        #     elif left_side[i-1] == '-':
        #         right_side.append('+')
        #         right_side.append(left_side[i])
        #         left_side.pop(i)
        #         left_side.pop(i-1)
        #         i+=1                
        #     elif left_side[i-1] == ''


        

