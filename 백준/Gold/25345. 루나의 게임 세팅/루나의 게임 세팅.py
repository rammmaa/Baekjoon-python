import sys

MOD = 10**9 + 7
ip = sys.stdin.readline

n, k = map(int, ip().split())
ip()

f = [1] * (n + 1)
for i in range(1, n + 1):
    f[i] = f[i - 1] * i % MOD

ivf = [1] * (n + 1)
ivf[n] = pow(f[n], MOD - 2, MOD)
for i in range(n, 0, -1):
    ivf[i - 1] = ivf[i] * i % MOD

c = f[n] * ivf[k] % MOD * ivf[n - k] % MOD
ans = c * pow(2, k - 1, MOD) % MOD
print(ans)
