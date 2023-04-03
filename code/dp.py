#M = 998244353

def solve_dp(S,T):
    n = len(S)
    m = len(T)

    dp = [[0 for j in range(n)] for i in range(n)]

    i = 0
    while i < n:
        if i >= m or T[i] == S[0]:
            dp[i][i] = 1
        i+=1

    k = 1
    while k < n:
        c = S[k]

        i = 0
        j = k
        while j < n:
            if i >= m or c == T[i]:
                dp[i][j] += dp[i+1][j]
            if j >= m or c == T[j]:
                dp[i][j] += dp[i][j-1]
            #dp[i][j] %= M
            i += 1
            j += 1
        k += 1

    return (sum(dp[0][m-1:]) * 2) #% M