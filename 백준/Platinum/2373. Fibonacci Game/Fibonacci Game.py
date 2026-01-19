import sys
input = sys.stdin.readline

n = int(input())

f = [1, 2]
while f[-1] + f[-2] <= n:
    f.append(f[-1] + f[-2])

if n in set(f):
    print(-1)
else:
    r = n
    ans = 10**18
    i = len(f) - 1
    skip = False

    while i >= 0:
        if skip:
            skip = False
            i -= 1
            continue
        if f[i] <= r:
            r -= f[i]
            ans = min(ans, f[i])
            skip = True
        i -= 1

    print(ans)
