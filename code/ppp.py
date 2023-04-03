import numpy as np

#Metodo recusivo, lo comentado es pa que imprima las combinaciones de las posiciones de las letras
def Procastinacion(S,T):
    if len(T) > len(S):
        return 0
    return 2*Procastinacion2(S,T,f'{S[0]}',1,"0")

def Procastinacion2(S,T,A, index,pos):
    if len(S) <= index:
        # if T == A[0:len(T)]: print(pos)
        return T == A[0:len(T)]
    # if ((len(T) <= len(A)) and (T == A[0:len(T)]sum((matrix[i,-1] - matrix[i+1,-1])* (2**(i -1)) *(T[-1]==S[i]) for i in range(len(S))))): print(pos)
    return Procastinacion2(S,T,f'{A}{S[index]}',index+1, f"{pos}{index}") + Procastinacion2(S,T,f'{S[index]}{A}',index+1,f"{index}{pos}"  ) + ((len(T) <= len(A)) and (T == A[0:len(T)]))
    


#Esto es lo del array pi, al final no se si sirva de algo
# def compute_prefix(w):
#     m = np.zeros(shape=len(w))
#     k = 0
#     for q in range(1,len(w)):
#         while k > 0 and w[q] != w[k+1]:
#             k = m[k]
#         if w[q] == w[k+1]:
#             k+=1
#         m[q]= k
#     return m


#Metodo dp
def ppp(S,T):
    #Aquise pueden detectar casillos O(n) comprobando que las letras de T sean subconjunto de las de S
    # Que len de T <= que len S

    matrix = np.zeros(shape=(len(S)+1,len(T)))
    if T.__contains__(S[0]):#Aqui hay que ver bien que hacer, pero con buscar cuantos sufizo de T se pueden formas tal 
        #que el ultimo movimiento sea poner la letra hacia atras y luego combinar con una mtriz como la del else.
        pass
    
    
    else: #Si la primera letra no pertenece al prefijo(Puede extenderse a que en S haya un caracter que no pertenezca a T antes que aparezca en S el ultimo caracter de T)
        for i in range(len(S)-1,-1,-1):
            matrix[i,0] = (len(S) - i)*(S[i] == T[0])  + matrix[(i+1)%len(S),0] #Buscar de atras hacia adelante la primera letra demi palabra y acumular la distancia de ahi hasta el final

        for i in range(1,len(T)):
            for j in range(len(S)-1,-1,-1):
                matrix[j,i] = matrix[(j+1)%len(S),i] + matrix[j,i-1] * (T[i] == S[j]) 
        
        return sum((matrix[i,-1] - matrix[i+1,-1])* (2**(i -1)) *(T[-1]==S[i]) for i in range(len(S)))




# matrix = np.zeros(shape=(5+1,5+1,2))
# print(matrix[0,1])

# print(compute_prefix("ababababca"))
