# from calc.calc_utils import OPS, brackets, DIGITS, join_exp, power_exp
# from calc.terms import Number, Variable

# # Solve equation logic
# def solve_equation(comps:list):
#     print('Solving equation')
#     path = [] # path memory
#     # Split list at '='
#     equal_index = comps.index('=')
#     left_side = comps[:equal_index]
#     right_side = comps[equal_index+1:]


    
#     def calc_side(side, side_name):
#         # Power in comp list
#         if '^' in side: 
#             result = power_exp(side)
#             if result:
#                 if side_name == 'left':
#                     expression = join_exp(result + ['='] + left_side)
#                 else:
#                     expression = join_exp(right_side + ['='] + result)
#                 # Log operation
#                 path.append({"expression": expression,
#                             "description": f"Powers Operated"})
#             else:
#                 # TODO: Ignore unhandled powers
#                 # power_ignore +=1
#                 pass

#         # Handle mult and div
#         elif '*' in side or '/' in side:
#             i = 0
#             while i < len(side):
#                 if side[i] == '*':
#                     result = side[i-1] * side[i+1]
#                     if result:
#                         description = f"Multiply {side[i-1]} * {side[i+1]}"
#                         side[i-1:i+2] = [result]
#                         if side_name == 'left':
#                             expression = join_exp(side + ['='] + right_side)
#                         else:
#                             expression =  join_exp(left_side + ['='] + side)
#                         path.append({"expression": expression,
#                                     "description": description})

#                 elif side[i] == '/':
#                     result = side[i-1] / side[i+1]
#                     if result:
#                         description = f"Divide {side[i-1]} / {side[i+1]}"
#                         side[i-1:i+2] = [result]
#                         if side_name == 'left':
#                             expression = join_exp(side + ['='] + right_side)
#                         else:
#                             expression =  join_exp(left_side + ['='] + side)
#                         path.append({"expression": expression,
#                                     "description": description})
#                 i+=1
                    
#         else:         
#             print(side)
#             running = True
#             i = 0
#             while running:
#                 # Finish loop when only 1 component left
#                 # Check if comp is a var
#                 if isinstance(side[i], Variable):
#                     # Create search list
#                     sub = side[i+1:]
#                     # Search for more vars
#                     for j in range(len(sub)):
#                         # Check if comp is a var
#                         if isinstance(sub[j], Variable):
#                             if j != 0:
#                                 # Perform Addition
#                                 if sub[j-1] == '+':
#                                     description = f"Combined var {sub[j].name} ({side[i]} + {sub[j]})"
#                                     # Update comp list
#                                     side[i] = side[i] + sub[j]
#                                     side.pop(i+j)
#                                     side.pop(i+j)
#                                     if side_name == 'left':
#                                         expression = join_exp(side + ['='] + right_side)
#                                     else:
#                                         expression =  join_exp(left_side + ['='] + side)
#                                     path.append({"expression": expression,
#                                                 "description": description})
#                                     break
#                                 # Substract
#                                 elif sub[j-1] == '-':
#                                     description = f"Substract var {sub[j].name} (({side[i]} - {sub[j]})"
#                                     # Update comp list
#                                     side[i] = side[i] - sub[j]
#                                     side.pop(i+j)
#                                     side.pop(i+j)
#                                     if side_name == 'left':
#                                         expression = join_exp(side + ['='] + right_side)
#                                     else:
#                                         expression =  join_exp(left_side + ['='] + side)
#                                     path.append({"expression": expression,
#                                                 "description": f"Substracted var {sub[j].name}"})
#                                     break
#                             else:
#                                 description = f"Combined var {sub[j].name} ({side[i]} + {sub[j]})"
#                                 # Update comp list
#                                 side[i] = side[i] + sub[j]
#                                 side.pop(i+j)
#                                 side.pop(i+j)
#                                 if side_name == 'left':
#                                     expression = join_exp(side + ['='] + right_side)
#                                 else:
#                                     expression =  join_exp(left_side + ['='] + side)
#                                 path.append({"expression": expression,
#                                             "description": description})
#                                 break

#                 elif isinstance(side[i], Number):
#                     sub = side[i+1:]
#                     j = 0
#                     while j < len(sub):

#                         if isinstance(sub[j], Number):
#                             if sub[j-1] == '+':
#                                 description = f"Add numbers {side[i]} + {sub[j]}"
#                                 side[i] = side[i] + sub[j]
#                                 side.pop(i+j)
#                                 side.pop(i+j)
#                                 sub = sub[:j-1] + sub[j+1:]
#                                 if side_name == 'left':
#                                     expression = join_exp(side + ['='] + right_side)
#                                 else:
#                                     expression =  join_exp(left_side + ['='] + side)
#                                 path.append({"expression": expression,
#                                             "description": description})

#                             elif sub[j-1] == '-':
#                                 description = f"Substracted numbers {side[i]} - {sub[j]}"
#                                 side[i] = side[i] - sub[j]
#                                 side.pop(i+j)
#                                 side.pop(i+j)
#                                 if side_name == 'left':
#                                     expression = join_exp(side + ['='] + right_side)
#                                 else:
#                                     expression =  join_exp(left_side + ['='] + side)
#                                     path.append({"expression": expression,
#                                                 "description": description})
                        
#                         j+= 1
#                 if not len(side):
#                     side.append(Number(0))
#                 if side_name == 'left':
#                     if isinstance(side[i], Number):
#                         right_side.append('+')
#                         description = f"Moved Number {side[i]} to right side"
#                         if i != 0:
#                             if side[i-1] == '+':
#                                 right_side.append(side[i]*(-1))
#                                 side.pop(i-1)
#                                 side.pop(i-1)
#                             elif side[i] == '-':
#                                 right_side.append(side[i]*(-1)*(-1))
#                                 side.pop(i-1)
#                                 side.pop(i-1)
#                         else:
#                             right_side.append(side[i]*(-1))
#                             side.pop(i)
#                         expression = join_exp(side + ['='] + right_side)
#                         path.append({"expression":  expression,
#                                     "description": description})
#                 elif side_name == 'right':
#                     if isinstance(side[i], Variable):
#                         left_side.append('+')
#                         description = f"Moved Variable {side[i]} to left side"
#                         if i != 0:
#                             if side[i-1] == '+':
#                                 left_side.append(side[i]*(-1))
#                                 side.pop(i-1)
#                                 side.pop(i-1)
#                             elif side[i] == '-':
#                                 left_side.append(side[i]*(-1)*(-1))
#                                 side.pop(i-1)
#                                 side.pop(i-1)
#                         else:
#                             left_side.append(side[i]*(-1))
#                             side.pop(i)
                        
#                         if not len(side):
#                             side.append(Number(0))
                        
#                         path.append({"expression": join_exp(left_side + ['='] + side),
#                                     "description": description})
#                 if not len(side):
#                     side.append(Number(0))
#                 if len(side) == 1:
#                     return side
#                 if side[0] == '+':
#                     side.pop(0)
#                 if side[0] == '-':
#                     side[1] = side[1] * (-1)
#                     side.pop(0)
#                 i += 1
#                 if i == len(side):
#                     i = 0
#         return side

                   
#     while len(left_side) > 1 or len(right_side) > 1 or isinstance(left_side[0], Number) or isinstance(right_side[0], Variable):
#         print(left_side, right_side)
#         if len(left_side) > 1 or isinstance(left_side[0], Number):
#             left_side = calc_side(left_side, 'left')
#         if len(right_side) > 1 or isinstance(right_side[0], Variable):
#             right_side = calc_side(right_side, 'right')
        
#     if left_side[0].value == 0:
#         left_side[0] = Number(0)
#         result = f'{left_side[0]} = {right_side[0]}'
#     else:
#         right_side.append('/')
#         right_side.append(Number(left_side[0].value))
#         left_side[0].value = 1
#         path.append({"expression": join_exp(left_side + ['='] + right_side),
#                     "description": f"Isolate Variable {left_side[0].name}"})
#         result = f'{left_side[0].name} = {right_side[0] / right_side[2]}'
#         path.append({"expression": join_exp(result),
#                     "description": f"Divide Numbers {right_side[0]} / {right_side[2]}"})
#     return result, path

#     # while '(' in left_side:
#     #     sub_comps, start, stop = brackets(left_side)
#     #     left_side[start:stop] = [operate(sub_comps)]


        

