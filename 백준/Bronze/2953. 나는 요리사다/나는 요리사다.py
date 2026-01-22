import sys
input = sys.stdin.readline

best_i = 0
best_s = -1

for i in range(5):
    s = sum(map(int, input().split()))
    if s > best_s:
        best_s = s
        best_i = i + 1

print(best_i, best_s)
