import sys
input = sys.stdin.readline

n, k = map(int, input().split())
dp = [0] * (k + 1)

for _ in range(n):
    w, v = map(int, input().split())
    if w > k:
        continue
    for x in range(k, w - 1, -1):
        nv = dp[x - w] + v
        if nv > dp[x]:
            dp[x] = nv

print(dp[k])