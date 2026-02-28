import sys
input = sys.stdin.readline

n, c = map(int, input().split())
s = list(map(int, input().split()))

cnt = {}
fst = {}

for i, x in enumerate(s):
    if x not in cnt:
        cnt[x] = 0
        fst[x] = i
    cnt[x] += 1

keys = list(cnt.keys())
keys.sort(key=lambda x: (-cnt[x], fst[x]))

out = []
for x in keys:
    out.extend([x] * cnt[x])

print(*out)