from math import inf

T = int(input())
for _ in range(T):
    n, m = map(int, input().split())
    ed = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v, w = map(int, input().split())
        ed[u].append((v, w))
        if w >= 0:
            ed[v].append((u, w))
    
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

    print("YES" if has_negative_cycle else "NO")