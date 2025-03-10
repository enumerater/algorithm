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