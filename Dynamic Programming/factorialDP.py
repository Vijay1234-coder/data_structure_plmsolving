dp = [-1] * 100002
mod=10**9 +7

def fact(n):
    if n == 0 :
        return 1
    if dp[n] != -1:
        return dp[n]
    else:
        dp[n] = n * fact((n - 1) % mod) % mod
        return dp[n]


t = int(input())
for i in range(t):
    n = int(input())
    print(fact(n % mod))