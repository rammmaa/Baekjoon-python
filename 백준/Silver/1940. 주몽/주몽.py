n = int(input())
m = int(input())
arr = list(map(int, input().split()))
arr.sort()

l, r = 0, n - 1
ans = 0

while l < r:
    s = arr[l] + arr[r]
    if s == m:
        ans += 1
        l += 1
        r -= 1
    elif s < m:
        l += 1
    else:
        r -= 1

print(ans)