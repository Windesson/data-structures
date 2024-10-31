#https://leetcode.com/problems/climbing-stairs/description/

# You are climbing a staircase. It takes n steps to reach the top.
# Each time you can either climb 1 or 2 steps. 
# In how many distinct ways can you climb to the top?

# At every step you can either climb 1 or 2 steps. once 

def climbingStairRecursion(steps):
    memo = {}
    return climbingStair(steps, 0, memo)

# DFS Depth First Search 
def climbingStair(steps, curr, memo):
    if steps in memo:
        return memo[steps]
    if curr > steps:
        return 0
    if curr == steps:
        return 1 # found one way to climb to the top
    
    count = climbingStair(steps, curr + 1, memo) + climbingStair(steps, curr + 2, memo)
    memo[curr] = count

    return count;

# bottom up dynamic programming
def climbingBackCount(steps):
    one, two = 1, 1
    while steps > 1:
        temp = one
        one = two + one
        two = temp

        steps -= 1
    return one
        
def caseTest(steps, expect, func):
    actual = func(steps)
    if actual == expect:
        print("pass")
    else:
        print(f"failed, expect {expect} actual {actual}")

caseTest(2, 2, climbingStairRecursion)
caseTest(3, 3, climbingStairRecursion)
caseTest(2, 2, climbingBackCount)
caseTest(3, 3, climbingBackCount)