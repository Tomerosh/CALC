from calc_utils import is_num, DIGITS

def split_num_var(comp):
    num = ''
    variable = ''
    for char in comp:
        if char in DIGITS or char == '-':
            num += char
        else:
            variable += char
    return num, variable

# def isolate()

def solve_equation(comps: list):
    print('Solving equation')
    equal_index = comps.index('=')
    left_side = comps[:equal_index]
    print(left_side)                    

    right_side = comps[equal_index+1:]
    i = 0
    # 4 + x + 3
    while i < len(left_side):
        print('i:', i)
        if '^' in left_side: # Power
            i = left_side.index('^')
            if is_num(left_side[i-1]) and is_num(left_side[i+1]): # Two numbers
                    left_side[i-1:i+2] = [float(left_side[i-1]) ** float(left_side[i+1])]
            else:
                left_side[i-1:i+2] = [left_side[i-1] +  '^' + left_side[i+1]]

        elif '*' in left_side or '/' in left_side: 
            if left_side[i] == '*':
                print('*')
                if is_num(left_side[i-1]):
                    if is_num(left_side[i+1]): 
                        left_side[i-1:i+2] = [float(left_side[i-1]) * float(left_side[i+1])]
                    else:
                        num, variable = split_num_var(left_side[i+1])
                        left_side[i-1:i+2] = [str(float(left_side[i-1]) * float(num)) + variable]
                else: # Left in variable
                    num, variable = split_num_var(left_side[i-1])
                    if is_num(left_side[i+1]):
                        left_side[i-1:i+2] = [str(float(num) * float(left_side[i+1])) + variable]
                    else: 
                        num2, var2 = split_num_var(left_side[i+1])
                        if variable == var2:
                            left_side[i-1:i+2] = [str(float(num) * float(num2)) + variable]
                        else:
                            pass
                            # i+=1
                            # continue
            elif left_side[i] == '/':
                if is_num(left_side[i-1]):
                    if is_num(left_side[i+1]):
                        left_side[i-1:i+2] = [float(left_side[i-1]) / float(left_side[i+1])]
                    else:
                        num, variable = split_num_var(left_side[i+1])
                        left_side[i-1:i+2] = [str(float(left_side[i-1]) / float(num)) + variable]
                else:
                    num, variable = split_num_var(left_side[i-1])
                    if is_num(left_side[i+1]):
                        left_side[i-1:i+2] = [str(float(num) / float(left_side[i+1])) + variable]
                    else: 
                        num2, var2 = split_num_var(left_side[i+1])
                        if variable == var2:
                            left_side[i-1:i+2] = [str(float(num) / float(num2)) + variable]
                        else:
                            pass
                            # i+=1
                            # continue
            
        else:
            pass
            if is_num(left_side[i]):
                right_side.append('-')
                right_side.append(left_side[i])

        i+=1
        if i == len(left_side) - 1:
            i = 0
        print(left_side)

                           
# comps = ['2x', '*', '2', '+', '2x', '+', '4', '=', '4']
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


        

