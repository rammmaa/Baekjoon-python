import sys
input = sys.stdin.readline

n = int(input().strip())

l, r = 1, 2000000000
while l < r:
    m = (l + r) // 2
    x = 1 + 3 * m * (m - 1)
    if n <= x:
        r = m
    else:
        l = m + 1

print(l)
