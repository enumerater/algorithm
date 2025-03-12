from collections import deque
from math import inf
import sys
input = sys.stdin.readline
def spfa(n, edges):
    dis = [inf] * (n + 1)
    vis = [0] * (n + 1)
    count = [0] * (n + 1)
    dis[1] = 0
    queue = deque([1])
    vis[1] = 1

    while queue:
        u = queue.popleft()
        vis[u] = 0
        for v, w in edges[u]:
            if dis[v] > dis[u] + w:
                dis[v] = dis[u] + w
                count[v] += 1
                if count[v] >= n:
                    return True
                if not vis[v]:
                    queue.append(v)
                    vis[v] = 1
    return False

T = int(input())
for _ in range(T):
    n, m = map(int, input().split())
    edges = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v, w = map(int, input().split())
        edges[u].append((v, w))
        if w >= 0:
            edges[v].append((u, w))
    if spfa(n, edges):
        print("YES")
    else:
        print("NO")