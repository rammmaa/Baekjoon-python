import sys
input = sys.stdin.readline

# 에라토스테네스의 체로 1,000,000까지 소수 구하기
MAX = 1000001
is_prime = [True] * MAX
is_prime[0] = is_prime[1] = False

for i in range(2, int(MAX ** 0.5) + 1):
    if is_prime[i]:
        for j in range(i * i, MAX, i):
            is_prime[j] = False

while True:
    n = int(input())
    if n == 0:
        break

    found = False
    # a는 작은 홀수 소수부터, b-a가 최대가 되려면 a가 최소여야 함
    for a in range(3, n // 2 + 1, 2):
        if is_prime[a] and is_prime[n - a]:
            print(f"{n} = {a} + {n - a}")
            found = True
            break

    if not found:
        print("Goldbach's conjecture is wrong.")
