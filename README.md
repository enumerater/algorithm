# 算法项目

## 介绍
记录刷题等。
## 最小公倍数

### lcm(a,b) =  (a*b)/gcd(a,b)

```python
def lcm(a,b):
	return (a*b)/gcd(a,b)
```

# 贪心

### 最长时间序列

### 贪心，对结束时间排序

# 并查集

P3367 【模板】并查集

```python
import sys
input = sys.stdin.readline
N, M = [int(i) for i in input().split()]
li = list(range(N + 1))
def find(a):
    if a == li[a]:
        return a
    li[a] = find(li[a])
    return li[a]
def merge(a, b):
    root_a = find(a)
    root_b = find(b)
    if root_a != root_b:
        li[root_b] = root_a
for _ in range(M):
    op, a, b = input().split()
    a, b = int(a), int(b)
    if op == '1':
        merge(a, b)
    elif op == '2':
        if find(a) == find(b):
            print("Y")
        else:
            print("N")
```

应用，最小生成树 P3366 【模板】最小生成树

```python
import sys
input = sys.stdin.readline
N, M = [int(i) for i in input().split()]
li = [i for i in range(N + 1)]
def find(a):
    if li[a] != a:
        li[a] = find(li[a])
    return li[a]

def merge(a, b):
    root_a = find(a)
    root_b = find(b)
    if root_a != root_b:
        li[root_a] = root_b

edges = []
for _ in range(M):
    x, y, z = [int(i) for i in input().split()]
    edges.append([z, x, y])
edges.sort()
res = 0
components = N
for z, x, y in edges:
    if find(x) != find(y):
        merge(x, y)
        res += z
        components -= 1
    if components == 1:
        print(res)
        break
else:
    print('orz')
```

# 卡特兰数 1 2 5 14 42 132   C(2n 2)/(n + 1)

# 最长有序子序列

B3637 最长上升子序列

```python
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
```

# 二分匹配

P3386 【模板】二分图最大匹配

```python
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
```

点覆盖边  = 最大匹配数

边覆盖点 = n - 最大匹配数 = 最大独立集

# 博弈

P2197 【模板】Nim 游戏

```python
T = int(input())
for _ in range(T):
    n = input()
    li = [int(i) for i in input().split()]
    a = li[0]
    for i in li[1:]:
        a = i^a
    if  a == 0:
        print('No')
    else:
        print('Yes')
```

异或和为0必败  反之必胜

多组游戏也是异或和

# 计算几何

叉乘，凸包

# 最短路

1dijk堆优化 

P3371 【模板】单源最短路径（弱化版）

P4779

[【模板】单源最短路径（标准版）](https://www.luogu.com.cn/problem/P4779)

```python
from heapq import heappush,heappop,heapify
import sys
input = sys.stdin.readline
n,m,s = [int(i) for i in input().split()]
MAX = 2**31 - 1
ed = [[] for i in range(n+1)]
for _ in range(m):
    u,v,w = [int(i) for i in input().split()]
    ed[u].append((v,w))
vis = [0 for i in range(n + 1)]
res = [MAX for i in range(n + 1)]
hp = [(0,s)]
res[s] = 0
while hp:
    p_w,p_node = heappop(hp)
    if vis[p_node] == 1:
        continue
    vis[p_node] = 1
    for c_node,c_w in ed[p_node]:
        if res[p_node] + c_w <= res[c_node]:
            res[c_node] = min(res[c_node],res[p_node] + c_w)
            heappush(hp,(res[c_node],c_node))
print(*res[1:])
```

Floyd B3647 【模板】Floyd

```python
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
```

bellman-ford 

```python
from math import inf

T = int(input())
for _ in range(T):
    n, m = map(int, input().split())
    ed = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v, w = map(int, input().split())
        ed[u].append((v, w))
    
    dis = [inf] * (n + 1)
    dis[1] = 0  # 假设源节点是1

    # 正确松弛逻辑：n-1轮，每轮处理所有边
    for _ in range(n-1):
        updated = False
        for u in range(1, n+1):
            if dis[u] == inf:
                continue
            for (v, w) in ed[u]:
                if dis[v] > dis[u] + w:
                    dis[v] = dis[u] + w
                    updated = True
        if not updated:
            break  # 提前终止优化

    # 检测负权环
    has_negative_cycle = False
    for u in range(1, n+1):
        if dis[u] == inf:
            continue
        for (v, w) in ed[u]:
            if dis[v] > dis[u] + w:
                has_negative_cycle = True
                break
        if has_negative_cycle:
            break

    print("Yes" if has_negative_cycle else "No")
```

spfa

```

```

