s, n = input().split()
n = int(n)
s_len = len(s)
length = s_len

# 扩展长度直到足够大
while length < n:
    length *= 2

# 逆推调整n的位置
while length > s_len:
    half = length // 2
    if n > half:
        n -= half + 1
    length = half

# 输出结果，注意索引从0开始，所以n-1
print(s[n - 1])