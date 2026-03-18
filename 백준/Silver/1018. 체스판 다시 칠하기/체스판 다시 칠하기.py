import sys
input = sys.stdin.readline

n, m = map(int, input().split())
b = [input().strip() for _ in range(n)]

ans = 10 ** 9

for si in range(n - 7):
    for sj in range(m - 7):
        c1 = 0
        c2 = 0
        for i in range(8):
            for j in range(8):
                cur = b[si + i][sj + j]
                e1 = 'W' if (i + j) % 2 == 0 else 'B'
                e2 = 'B' if (i + j) % 2 == 0 else 'W'

                if cur != e1:
                    c1 += 1
                if cur != e2:
                    c2 += 1
        ans = min(ans, c1, c2)

print(ans)