import sys
input = sys.stdin.readline

N, B = map(int, input().split())
ans = ""

while (N > 0):
    a = N % B
    N = N // B
    if a < 10:
        ans += str(a)
    else:
        ans += chr(ord('A') + a - 10)

print(ans[::-1])