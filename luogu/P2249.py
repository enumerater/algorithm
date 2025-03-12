import bisect

n, m = map(int, input().split())
arr = list(map(int, input().split()))
qs = list(map(int, input().split()))

for q in qs:
    index = bisect.bisect_left(arr, q)
    if index < n and arr[index] == q:
        print(index + 1, end=' ')
    else:
        print(-1, end=' ')