# Given an integer array nums of length n, 
# you want to create an array ans of length 2n 
# where ans[i] == nums[i] and ans[i + n] == nums[i] 
# for 0 <= i < n (0-indexed).
# Specifically, ans is the concatenation of 
# two nums arrays. Return the array ans.

def getConcatenation(nums):
    n = len(nums)
    ans = [0] * 2 * n
    for i in range(n):
        ans[i] = nums[i]
        ans[i + n] = nums[i]
    return ans

def testCase1(): 
    nums = [1,2,1]
    ans = getConcatenation(nums)

    #assert
    if ans == [1,2,1,1,2,1]:
        print("pass")
    else:
        raise Exception("failed")

testCase1()