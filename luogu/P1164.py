N,M = [int(i) for i in input().split()]
li = [0] + [int(i) for i in input().split()]

dp = [[0 for i in range(M+1)] for j in range(N+1)]

for i in range(N+1):
    dp[i][0] = 1
    
for i in range(1,N+1):
    for j in range(1,M+1):
        if j >= li[i]:
            dp[i][j] += dp[i-1][j-li[i]]
        dp[i][j] += dp[i-1][j]
print(dp[N][M])