import sys
input = sys.stdin.readline

n = int(input())
a = [tuple(map(int, input().split())) for _ in range(n)]
a.sort(key=lambda x: (x[1], x[0]))

cnt = 0
end = 0

for s, e in a:
    if s >= end:
        cnt += 1
        end = e

print(cnt)
