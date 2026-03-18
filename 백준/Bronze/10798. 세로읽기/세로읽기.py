import sys
input = sys.stdin.readline

lines = [input().strip() for _ in range(5)]

result = []
for i in range(15):
    for j in range(5):
        if i < len(lines[j]):
            result.append(lines[j][i])

print(''.join(result))
