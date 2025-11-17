import sys
from math import gcd
input = sys.stdin.readline

N = int(input())
dir_count = {}

for _ in range(N):
    a, b, c = map(int, input().split())

    g = gcd(a, b)
    if g != 0:
        a //= g
        b //= g

    if a < 0 or (a == 0 and b < 0):
        a = -a
        b = -b

    key = (a, b)
    dir_count[key] = dir_count.get(key, 0) + 1

total = N * (N - 1) // 2

for cnt in dir_count.values():
    total -= cnt * (cnt - 1) // 2

print(total)
