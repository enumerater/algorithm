import sys
input = sys.stdin.readline
n = int(input())
li = [0] + [int(i) for i in input().split()]
dp = [1] * (n + 1)
for i in range(2,n + 1):
    for j in range(1,i):
        if li[i] > li [j]:
            dp[i] = max(dp[j] + 1,dp[i])
print(max(dp))