import sys
sys.setrecursionlimit(9999)
n,m = [int(i) for i in input().split()]
ed = [[] for i in range(n + 1)]
rev = [[] for i in range(n + 1)]
for _ in range(m):
    u,v = [int(i) for i in input().split()]
    ed[u].append(v)
    rev[v].append(u)

vis = [0] * (n + 1)
stack = []
def dfs1(x):
    vis[x] = 1
    for i in ed[x]:
        if not vis[i]:
            dfs1(i)
    stack.append(x)
def dfs2(x, y):
    vis[x] = 1
    f[x] = y
    for i in rev[x]:
        if not vis[i]:
            dfs2(i, y)
for i in range(1, n + 1):
    if not vis[i]:
        dfs1(i)
f = [0] * (n + 1)
vis = [0] * (n + 1)
while stack:
    x = stack.pop()
    if not vis[x]:
        dfs2(x, x)
res = len(set(f[1:n + 1]))
print(res)
components = {}
for i in range(1, n + 1):
    if f[i] not in components:
        components[f[i]] = []
    components[f[i]].append(i)

for key in components:
    print(*components[key])