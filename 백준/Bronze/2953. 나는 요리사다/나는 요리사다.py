arr = []

for _ in range(5):
    arr.append(sum(list(map(int, input().split()))))

print(arr.index(max(arr)) + 1, max(arr))