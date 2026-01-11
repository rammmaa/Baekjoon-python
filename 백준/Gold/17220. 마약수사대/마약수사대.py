from collections import deque

N, M = map(int, input().split())

graph = [[] for _ in range(26)]
in_degree = [0] * 26  # 진입 차수 (공급받는 곳이 있는지)

for _ in range(M):
    a, b = input().split()
    u, v = ord(a) - ord('A'), ord(b) - ord('A')
    graph[u].append(v)
    in_degree[v] += 1

line = input().split()
K = int(line[0])
arrested = set()
for i in range(1, K + 1):
    arrested.add(ord(line[i]) - ord('A'))

# 원산지: 진입차수가 0이면서 검거되지 않은 노드
# 원산지에서 BFS로 도달 가능한 노드들이 마약을 공급받을 수 있음
# 단, 검거된 노드는 통과 불가

visited = [False] * 26
queue = deque()

# 원산지 찾기 (진입차수 0 + 검거 안됨)
for i in range(N):
    if in_degree[i] == 0 and i not in arrested:
        queue.append(i)
        visited[i] = True

# BFS
while queue:
    cur = queue.popleft()
    for nxt in graph[cur]:
        if not visited[nxt] and nxt not in arrested:
            visited[nxt] = True
            queue.append(nxt)

# 마약을 공급받는 노드 수 (원산지 제외)
count = 0
for i in range(N):
    if visited[i] and in_degree[i] > 0:
        count += 1

print(count)
