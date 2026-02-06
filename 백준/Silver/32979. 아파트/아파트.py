N = int(input())
T = int(input())
hands = list(map(int, input().split()))
calls = list(map(int, input().split()))

idx = 0
result = []

for b in calls:
    idx = (idx + b - 1) % len(hands)
    result.append(hands[idx])

print(*result)