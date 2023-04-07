import json

def check(path_1, range_1, path_2, range_2):
    with open(path_1) as fp:
        solutions_1 = fp.readlines()
    with open(path_2) as fp:
        solutions_2 = fp.readlines()
    eq = 0   
    fails = [] 
    for i, j in zip(range_1,range_2):
        if solutions_1[i].split()[1] == solutions_2[j].split()[1]:
            eq += 1
        else:  
            fails.append(solutions_1[i].split()[0])
    return eq, fails

goods, fails = check('code/result_dp.txt', range(0,22680), 'code/result_dpNxM.txt', range(0,22680))
print(goods)
if len(fails) > 0:
    print(fails[:50])
    