import sys

def main():
    it = iter(sys.stdin.read().splitlines())
    out = []

    for s in it:
        s = s.strip()
        if not s:
            continue
        n = int(s)
        if n == 0:
            break

        r = next(it).strip()
        v = [False] * (n + 1)

        for t in r.split(','):
            if not t:
                continue
            if '-' in t:
                a, b = t.split('-', 1)
                lo = int(a)
                hi = int(b)
                if lo > hi:
                    continue
                lo = max(1, lo)
                hi = min(n, hi)
                if lo <= hi:
                    for p in range(lo, hi + 1):
                        v[p] = True
            else:
                p = int(t)
                if 1 <= p <= n:
                    v[p] = True

        out.append(str(sum(v)))

    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()
