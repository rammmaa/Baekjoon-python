arr = [int(input()) for _ in range(9)]
total = sum(arr)

for i in range(9):
    for j in range(i + 1, 9):
        if total - arr[i] - arr[j] == 100:
            for k in range(9):
                if k != i and k != j:
                    print(arr[k])
            exit(0)
        