#Metodo dp
def ppp(S,T):
    n = len(S)
    m = len(T)
    if n> m: return 0

    prefix = compute_prefix(S,T)
    count = 0

    if T.__contains__(S[0]):
        sufix = compute_sufix(S, T)
        count= sufix[0][m-1] * (n - m + 1)
        
        for i in range(1,m):           
            count += sufix[i][m-1+i]* prefix[m][i-1]
    
    return count + int(sum((prefix[i][-1] - prefix[i+1][-1])* (2**(max(i-1,0))) *(T[-1]==S[i]) for i in range(n))*2)

def compute_prefix(S,T):
    m = len(T)
    n = len(S)

    dp = [[0 for j in range(m)] for i in range(n +1)]

    
    for i in range(n-1,-1,-1):
        dp[i][0] = (n - i)*(S[i] == T[0])  + dp[(i+1)%n][0] #Buscar de atras hacia adelante la primera letra demi palabra y acumular la distancia de ahi hasta el final

    for i in range(1,m):
        for j in range(n-i -1,-1,-1):
            dp[j][i] = dp[(j+1)%n][i] + dp[(j+1)%n][i-1] * (T[i] == S[j])

    return dp
    
 def compute_sufix(S,T):
    m = len(T)
    dp = [[0 for j in range(2*m)] for i in range(2*m)]
    tmdp = [[0 for j in range(2*m)] for i in range(2*m)]
            
    for i in range(2*m):
        if i >= m or T[i] == S[0]:
            tmdp[i][i] = 2
        
    for k in range(1, m):    
        c = S[k]
        i = 0        
    
        for j in range(k, m  k):
            if j >= m:
                dp[i][j] += dp[i][j-1]
                tmdp[i][j] += tmdp[i][j-1]          
        
            if j< m and c==T[j]:
                dp[i][j] += tmdp[i][j-1]
                tmdp[i][j] += tmdp[i][j-1]
        
            if i >= m or c == T[i]:
                dp[i][j] += dp[i+1][j]
                tmdp[i][j] += tmdp[i+][j]
            i += 1  
    return dp  
