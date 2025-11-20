N, r, c = map(int, input().split())
ans = 0
n = N

while n > 0:
    half = 1 << (n - 1)
    block = half * half

    if r < half and c < half:
        k = 0
    elif r < half and c >= half:
        k = 1
        c -= half
    elif r >= half and c < half:
        k = 2
        r -= half
    else:
        k = 3
        r -= half
        c -= half

    ans += k * block
    n -= 1

print(ans)
