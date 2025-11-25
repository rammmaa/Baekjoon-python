import math

N = int(input())

def solution():
    global N
    v = []
    answer = []

    i = 2
    while i <= math.isqrt(N):
        while N % i == 0:
            N //= i
            v.append(i)
        i += 1

    if N != 1:
        v.append(N)

    if len(v) == 1:
        print(-1)
        return

    for i in range(0, len(v), 2):
        if i == len(v) - 1:
            answer[-1] *= v[i]
        else:
            answer.append(v[i] * v[i + 1])

    for elem in answer:
        print(elem, end=" ")

solution()
