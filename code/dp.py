def solve_dp(S,T):
    n = len(S)
    m = len(T)

    if m > n:
        return 0

    dp = [[0 for j in range(n)] for i in range(n)]
        
    for i in range(n):
        if i >= m or T[i] == S[0]:
            dp[i][i] = 2
    
    for k in range(1, n):    
        c = S[k]

        i = 0        
        for j in range(k, n):
            if i >= m or c == T[i]:
                dp[i][j] += dp[i+1][j]
            if j >= m or c == T[j]:
                dp[i][j] += dp[i][j-1]            
            i += 1            

    return sum(dp[0][m-1:])
