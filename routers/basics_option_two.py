 #  יצירת רשימה חדשה, אם זה אופרטור משאירים אותו - אם זה מספר הופכים לפלואט 
def solve_basic(raw_components: list):
    solution_steps = []
    
    working_equation = []
    for component in raw_components:
        if component == '':
            continue
        if component in ['+', '-', '*', '/', '^', '(', ')']:
            working_equation.append(component)
        else:
            working_equation.append(float(component))
            
# הסופה של המצב התחלתי להיסטוריה
    solution_steps.append(list(working_equation))

    while len(working_equation) > 1:
        
        block_start = 0
        block_end = len(working_equation)
        
        #בדיקה אם יש סוגריים בתרגיל 
        if ')' in working_equation:
            block_end = working_equation.index(')')
            for i in range(block_end - 1, -1, -1):
                if working_equation[i] == '(':
                    block_start = i
                    break
        
        #מחיקה של הסוגריים במידה ויש איבר בודד בהם
        if block_end != len(working_equation) and (block_end - block_start) == 2:
            number_inside = working_equation[block_start + 1]
            working_equation[block_start : block_end + 1] = [number_inside]
            continue

        operator_index = -1
        precedence_levels = [['^'], ['*', '/'], ['+', '-']]
        
        for current_level in precedence_levels:
            for i in range(block_start + 1, block_end):
                if working_equation[i] in current_level:
                    operator_index = i
                    break
            if operator_index != -1: 
                break
                
        if operator_index != -1:
            current_operator = working_equation[operator_index]
            left_number = working_equation[operator_index - 1]
            right_number = working_equation[operator_index + 1]
            
            if current_operator == '^':
                calculation_result = left_number ** right_number
            elif current_operator == '*':
                calculation_result = left_number * right_number
            elif current_operator == '/':
                if right_number == 0:
                    raise ValueError()
                calculation_result = left_number / right_number
            elif current_operator == '+':
                calculation_result = left_number + right_number
            elif current_operator == '-':
                calculation_result = left_number - right_number
            
            working_equation[operator_index - 1 : operator_index + 2] = [calculation_result]
            
            # הוספה להיסטוריה
            solution_steps.append(list(working_equation))
        else:
            break
            
    final_answer = working_equation[0]        
    return final_answer, solution_steps

# פליטה כרשימת פעולות
test_components = ['(', '3', '^', '3', '*', '2', ')', '+', '10','-' ,'(' ,'3' ,'+', '4', '*', '6' ,')']
print(solve_basic(test_components))