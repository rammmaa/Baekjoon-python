import sys
input = sys.stdin.readline

N, B = input().split()
B = int(B)
ans = 0

for letter in N:
    if letter.isdigit():
        ans = ans * B + int(letter)
    else:
        ans = ans * B + (ord(letter) - ord('A') + 10)

print(ans)
