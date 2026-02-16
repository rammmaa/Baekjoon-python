import sys

input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [False] * (N + 1)


def dfs(start):
    stack = [start]
    visited[start] = True

    while stack:
        cur = stack.pop()
        for nxt in graph[cur]:
            if not visited[nxt]:
                visited[nxt] = True
                stack.append(nxt)


count = 0
for node in range(1, N + 1):
    if not visited[node]:
        dfs(node)
        count += 1

print(count)
