n,m,e = [int(i) for i in input().split()]
ed = [[] for i in range(n + 1)]
for i in range(e):
    u,v = [int(i) for i in input().split()]
    ed[u].append(v)
vis = [0 for i in range(m + 1)]
def dfs(x):
    for v in ed[x]:
        if vis[v] == 0:
            vis[v] = 1
            if not match[v] or dfs(match[v]):
                match[v] = x
                vis[v] = 0 # 回溯
                return True
    return False
match = [0 for _ in range(m + 1)]
res = 0
for i in range(1,n + 1):
    if dfs(i):
        res += 1
print(res)