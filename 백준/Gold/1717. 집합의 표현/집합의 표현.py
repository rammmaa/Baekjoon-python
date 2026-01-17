import sys

input = sys.stdin.readline

def main():
    n, m = map(int, input().split())
    p = list(range(n + 1))
    s = [1] * (n + 1)

    def f(x):
        while p[x] != x:
            p[x] = p[p[x]]
            x = p[x]
        return x

    out = []
    for _ in range(m):
        t, a, b = map(int, input().split())
        ra = f(a)
        rb = f(b)
        if t == 0:
            if ra != rb:
                if s[ra] < s[rb]:
                    ra, rb = rb, ra
                p[rb] = ra
                s[ra] += s[rb]
        else:
            out.append("YES\n" if ra == rb else "NO\n")

    sys.stdout.write(''.join(out))

if __name__ == "__main__":
    main()
