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