from collections import deque

N, M = map(int, input().split())
targets = list(map(int, input().split()))
q = deque(range(1, N + 1))

count = 0
for t in targets:
    idx = q.index(t)
    left = idx
    right = len(q) - idx
    
    count += min(left, right)
    
    if left <= right:
        for _ in range(idx):
            q.append(q.popleft())
    else:
        for _ in range(len(q) - idx):
            q.appendleft(q.pop())
    
    q.popleft()

print(count)
