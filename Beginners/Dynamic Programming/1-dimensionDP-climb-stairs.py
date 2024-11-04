# You are climbing a staircase. It takes n steps to reach the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
# Example 1:

# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps
# Example 2:

# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step

def brute_force_climb_stairs(n):
    
    def climb(step = 0):
        if step > n:
            return 0
        if step == n:
            return 1
        else:
            return climb(step + 1) + climb(step + 2)
        
    return climb()

# top down 
def memoization_climb(n):
    cache = {}
    def climb(step = 0):
        if step in cache:
            return cache[step]
        
        if step > n:
            cache[step] = 0
        elif step == n:
            cache[step] = 1
        else:
            cache[step] = climb(step + 1) + climb(step + 2)
        
        return cache[step] 
        
    return climb()

# bottom up
def dp_climb(n):
    if n < 2:
        return n
    
    dp = [1,1] 
    i = n - 2
    while i > 0:
        temp = dp[0]
        dp[0] = dp[0] + dp[1]
        dp[1] = temp
        i -= 1

    return dp[0] + dp[1]


def test(actual, expected):
    if actual == expected:
        print("pass")
    else:
        print(f"failed expected {expected} but return {actual}")

     
test(brute_force_climb_stairs(3), 3)
test(memoization_climb(3), 3)
test(dp_climb(3), 3)

