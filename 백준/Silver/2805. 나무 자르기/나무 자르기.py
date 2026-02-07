n, m = map(int, input().split())
arr = list(map(int, input().split()))

a, b = 0, max(arr)

while a <= b:
    mid = (a + b) // 2
    total = sum(t - mid for t in arr if t > mid)

    if total >= m:
        a = mid + 1
    else:
        b = mid - 1

print(b)
