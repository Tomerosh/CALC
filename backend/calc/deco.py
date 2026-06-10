# x + 2 + 4x + 10 + y


# 5x + 12  * 2x

def solve_deco(comps):
    print(comps)
    items = {
        'nums': [12],
        'x': ['5x', '2x']
    }
    for i in range(len(comps)):
        if isinstance(comps[i], float):
            print(comps[i])