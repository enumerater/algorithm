from bisect import bisect_left,bisect_right,bisect

N,C = [int(i) for i in input().split()] 

li = [int(i) for i in input().split()]
li.sort()
res = 0
for B in li:
    A = B + C
    index_left = bisect_left(li,A)
    index_right = bisect_right(li,A)
    res += index_right - index_left
print(res)