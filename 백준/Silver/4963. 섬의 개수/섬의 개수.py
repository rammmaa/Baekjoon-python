import sys

it = iter(map(int, sys.stdin.buffer.read().split()))
d = [(-1, -1), (-1, 0), (-1, 1),
     (0, -1),          (0, 1),
     (1, -1),  (1, 0), (1, 1)]

out = []
while True:
    w = next(it)
    h = next(it)
    if w == 0 and h == 0:
        break

    a = [[next(it) for _ in range(w)] for _ in range(h)]
    c = 0

    for i in range(h):
        for j in range(w):
            if a[i][j] == 1:
                c += 1
                st = [(i, j)]
                a[i][j] = 0
                while st:
                    x, y = st.pop()
                    for dx, dy in d:
                        nx = x + dx
                        ny = y + dy
                        if 0 <= nx < h and 0 <= ny < w and a[nx][ny] == 1:
                            a[nx][ny] = 0
                            st.append((nx, ny))

    out.append(str(c))

sys.stdout.write("\n".join(out))
