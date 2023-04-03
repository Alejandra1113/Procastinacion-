import numpy as np

#Metodo recusivo, lo comentado es pa que imprima las combinaciones de las posiciones de las letras
def Procastinacion(S,T):
    if len(T) > len(S):
        return 0
    return 2*Procastinacion2(S,T,f'{S[0]}',1)

def Procastinacion2(S,T,A, index):
    if len(S) <= index:
        return T == A[0:len(T)]
    return Procastinacion2(S,T,f'{A}{S[index]}',index+1) + Procastinacion2(S,T,f'{S[index]}{A}',index+1) + ((len(T) <= len(A)) and (T == A[0:len(T)]))
    
