#Metodo dp
def ppp(S,T):
    #Aquise pueden detectar casillos O(n) comprobando que las letras de T sean subconjunto de las de S
    # Que len de T <= que len S

    prefix = compute_prefix(S,T)
    n = len(S)
    m = len(T)
    if T.__contains__(S[0]):#Aqui hay que ver bien que hacer, pero con buscar cuantos sufizo de T se pueden formas tal 
        #que el ultimo movimiento sea poner la letra hacia atras y luego combinar con una mtriz como la del else.
        sufix = compute_sufix(S, T)
        count= sufix[0][m-1] * (n - m +1)
        for i in range(1,m):           
            count += sufix[i][m-1]* prefix[m][i-1]
        count += sum((prefix[i][-1] - prefix[i+1][-1])* (2**(i -1)) *(T[-1]==S[i]) for i in range(m-1,n))*2
        return count
    #Si la primera letra no pertenece al prefijo(Puede extenderse a que en S haya un caracter que no pertenezca a T antes que aparezca en S el ultimo caracter de T)        
    return int(sum((prefix[i][-1] - prefix[i+1][-1])* (2**(i -1)) *(T[-1]==S[i]) for i in range(len(S))) *2)


def compute_prefix(S,T):
    m = len(T)
    n = len(S)

    dp = [[0 for j in range(m)] for i in range(n +1)]
    
    for i in range(n-1,-1,-1):
        dp[i][0] = (n - i)*(S[i] == T[0])  + dp[(i+1)%n][0] #Buscar de atras hacia adelante la primera letra demi palabra y acumular la distancia de ahi hasta el final

    for i in range(1,m):
        for j in range(n-1,-1,-1):
            dp[j][i] = dp[(j+1)%n][i] + dp[j][i-1] * (T[i] == S[j])

    return dp
    
def compute_sufix(S,T):
        m = len(T)
        dp = [[0 for j in range(m)] for i in range(m)]
                    
        for i in range(m):
            if T[i] == S[0]:
                dp[i][i] = 2
                
        for k in range(1, m):    
            c = S[k]
            i = 0        
            
            for j in range(k, m):
                if c == T[i]:
                    dp[i][j] += dp[i+1][j]
                if c == T[j]:
                    dp[i][j] += dp[i][j-1]            
                i += 1  
        return dp

