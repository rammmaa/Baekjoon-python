import sys
input = sys.stdin.readline

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

w = 0
b = 0

def go(x, y, s):
    global w, b
    c = a[x][y]
    for i in range(x, x+s):
        for j in range(y, y+s):
            if a[i][j] != c:
                h = s // 2
                go(x, y, h)
                go(x, y+h, h)
                go(x+h, y, h)
                go(x+h, y+h, h)
                return
    if c == 0:
        w += 1
    else:
        b += 1

go(0, 0, n)
print(w)
print(b)
