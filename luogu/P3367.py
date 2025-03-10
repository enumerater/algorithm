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