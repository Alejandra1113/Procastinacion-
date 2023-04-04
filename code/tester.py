import json
import dp
import ppp

def run_tester(path_cases, solve, keys):
    with open(path_cases) as fp:
        cases = json.load(fp)
        #print(len(cases))
    
    for key in keys:
        result = solve(cases[key][0], cases[key][1])
        print(f'{key} {result}')


run_tester('cases_01.json', dp.solve_dp, range(22680))
#run_tester('cases_01.json', ppp.Procastinacion, range(500,1000))
#run_tester('cases_01.json', 'result_cases_01_ppp', ppp.Procastinacion)