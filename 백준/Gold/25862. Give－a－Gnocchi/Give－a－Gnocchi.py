import sys

def solve():
    input_data = sys.stdin.readline().split()
    if not input_data:
        return
    n = int(input_data[0])
    k = int(input_data[1])


    MAX_LIMIT = 30000
    is_prime = [True] * (MAX_LIMIT + 1)
    is_prime[0] = is_prime[1] = False
    
    for i in range(2, int(MAX_LIMIT**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, MAX_LIMIT + 1, i):
                is_prime[j] = False
                
    primes = [i for i in range(MAX_LIMIT + 1) if is_prime[i]]
    
    small_primes = [p for p in primes if p <= n]
    large_primes = [p for p in primes if p > n]
    

    if n < 30:
        count = 0
        curr = 1
        while count < k:
            curr += 1
            
            is_divisible = False
            for p in small_primes:
                if curr % p == 0:
                    is_divisible = True
                    break
            if is_divisible:
                continue

            if curr <= MAX_LIMIT:
                if is_prime[curr]:
                    continue
            
            # 조건을 만족하는 합성수 발견
            count += 1
            
        print(curr)
        
    else:

        
        subset = large_primes[:250] 
        candidates = []
        subset_len = len(subset)
        
        for i in range(subset_len):
            for j in range(i, subset_len):
                val = subset[i] * subset[j]
                candidates.append(val)
        
        candidates.sort()
        print(candidates[k-1])

if __name__ == '__main__':
    solve()