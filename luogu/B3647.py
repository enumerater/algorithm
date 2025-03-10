from math import inf
n,m = [int(i) for i in input().split()]
dis = [[inf for i in range(n + 1)] for i in range(n + 1)]

for i in range(1,n + 1):
    dis[i][i] = 0
for _ in range(m):
    u,v,w = [int(i) for i in input().split()]
    if w < dis[u][v]:  
        dis[u][v] = w
        dis[v][u] = w
for k in range(1,n + 1):
    for i in range(1,n + 1):
        for j in range(1,n + 1):
            if dis[i][j] > dis[i][k] + dis[k][j]:
                dis[i][j] = dis[i][k] + dis[k][j]

for i in range(1,n + 1):
    for j in range(1,n + 1):
        print(dis[i][j],end = ' ')
    print()