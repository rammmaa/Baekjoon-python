def solve(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False

    for i in range(2, int(n**0.5 + 1)):
        if is_prime[i]:
            for j in range(i+i, n + 1, i):
                is_prime[j] = False
    
    return [i for i in range(2, n + 1) if is_prime[i]]

prime_number = solve(1000)
N = int(input())
arr = list(map(int, input().split()))

cnt = 0

for i in arr:
    if i in prime_number:
        cnt += 1

print(cnt)