import random as rand
import json

A1 = 'abc'
A2 = 'abcd'
A3 = 'abcde'
A4 = 'abcdef'

def generate_T(alphabet, size):
    return rand.choices(alphabet, k=size)  

def generate_S(T, alphabet, size):
    len_T = len(T)
    choc = rand.choices(alphabet, k=size)
    S = T + choc
    rand.shuffle(S)
    return S

def list_to_str(array):
    s = ''
    for c in array:
        s+=c
    return s

def generate_cases():
    cases = []
    for size_T in range(2, 20):
        for j in range(6):
            T = generate_T(A1, size_T)
            for size_S in range(0, 10*size_T):
                S = generate_S(T, A1, size_S)
                cases.append((list_to_str(S), list_to_str(T)))
            for size_S in range(0, 5*size_T):
                S = generate_S(T, A2, size_S)
                cases.append((list_to_str(S), list_to_str(T)))
            for size_S in range(0, 5*size_T):
                S = generate_S(T, A3, size_S)
                cases.append((list_to_str(S), list_to_str(T)))
    return cases

cases = generate_cases()
with open('cases_01.json', 'w') as fd:
    json.dump(cases, fd)
