import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = []
out = []

def dfs(st):
    if len(a) == m:
        out.append(' '.join(map(str, a)))
        return
    for i in range(st, n + 1):
        a.append(i)
        dfs(i)
        a.pop()

dfs(1)
sys.stdout.write('\n'.join(out))