import sys
input = sys.stdin.readline

X = int(input())

d = 1
while d * (d + 1) // 2 < X:
    d += 1

p = X - d * (d - 1) // 2

if d % 2 == 1:
    a = d - p + 1
    b = p
else:
    a = p
    b = d - p + 1

print(f"{a}/{b}")
