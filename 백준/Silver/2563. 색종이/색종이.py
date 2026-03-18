import sys
input = sys.stdin.readline

n = int(input())
paper = [[False] * 100 for _ in range(100)]

for _ in range(n):
    a, b = map(int, input().split())
    # a: 왼쪽 아래 모서리 x좌표, b: y좌표
    # 가로, 세로는 10
    for i in range(a, a + 10):
        for j in range(b, b + 10):
            paper[i][j] = True

ans = 0
for i in range(100):
    for j in range(100):
        if paper[i][j]:
            ans +=1

print(ans)