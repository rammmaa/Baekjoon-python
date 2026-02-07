import sys
input = sys.stdin.readline

n, c = map(int, input().split())
arr = []

for _ in range(n):
    arr.append(int(input()))

arr.sort()

a = 1
b = arr[-1] - arr[0]

while a <= b:
    mid = (a + b) // 2

    cnt = 1
    last = arr[0]

    for i in range(1, n):
        if arr[i] - last >= mid: 
            cnt += 1
            last = arr[i]
    
    if cnt >= c:     
        a = mid + 1
    else:            
        b = mid - 1

print(b)