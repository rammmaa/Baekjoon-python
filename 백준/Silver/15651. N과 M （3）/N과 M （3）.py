import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = []
out = []

def dfs():
    if len(a) == m:
        out.append(' '.join(map(str, a)))
        return
    for i in range(1, n + 1):
        a.append(i)
        dfs()
        a.pop()

dfs()
sys.stdout.write('\n'.join(out))