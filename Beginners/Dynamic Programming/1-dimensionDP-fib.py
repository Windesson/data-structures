
# f(0) = 0
# f(1) = 1
# f(n) = f(n-1) + f(n-2)
# 0 1 2 3 4 5 6 7
# 0 1 1 2 3 5 8 13
def brute_force_fib(n):
    if n < 2:
        return n
    return brute_force_fib(n-1) + brute_force_fib(n-2)

# Memoization "ToDown" dynamic programming
def memoization_fib(n, cache = {}):
    if n < 2:
        return n
    if n in cache:
        return cache[n]
    
    cache[n] = brute_force_fib(n-1) + brute_force_fib(n-2)
    return cache[n]

# "BottomUp" from n perpective  
def BottomUpfib(n):
    if n < 2:
        return n
    
    dp = [0,1] 
    i = 2
    while i <= n:
        temp = dp[1]
        dp[1] = dp[0] + dp[1] 
        dp[0] = temp
        i += 1

    return dp[1]


if brute_force_fib(7) == memoization_fib(7) and brute_force_fib(7) == BottomUpfib(7):
    print("pass")
else:
    print("failed!")


