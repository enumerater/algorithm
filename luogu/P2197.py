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