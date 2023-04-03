import json

def check(path_1, range_1, path_2, range_2):
    with open(path_1) as fp:
        solutions_1 = fp.readlines()
    with open(path_2) as fp:
        solutions_2 = fp.readlines()
    eq = 0    
    for i, j in zip(range_1,range_2):
        if solutions_1[i].split()[1] == solutions_2[j].split()[1]:
            eq += 1
    return eq

print(check('result_cases_01_dp.txt', range(0,266), 'result_cases_01_ppp_265.txt', range(0,266)))
    