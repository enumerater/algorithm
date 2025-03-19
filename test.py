N = int(input())
booms = [0] + list(map(int, input().split()))
ed = [[] for _ in range(N + 1)]
for i in range(1, N):
    indexs = list(map(int, input().split()))
    t = 1
    for idx in indexs:
        if idx == 1:
            j = i + t
            if j <= N:  # 确保不越界
                ed[i].append(j)
                ed[j].append(i)
        t += 1
def dfs(u):
    vis[u] = 1
    res[u] = booms[u]
    for v in ed[u]:
        if not vis[v]:
            res[u] += dfs(v)
    return res[u]
res_r = 0
for i in range(1,N+1):
    res = [0] * (N + 1)
    vis = [0] * (N + 1)
    dfs(i)
    res_r = max(res_r, max(res))
print(res_r)