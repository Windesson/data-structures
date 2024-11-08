# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.
# Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.
# Example 1:
# Input: nums = [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
# Total amount you can rob = 1 + 3 = 4.
# Example 2:
# Input: nums = [2,7,9,3,1]
# Output: 12
# Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
# Total amount you can rob = 2 + 9 + 1 = 12.

def rob(self, nums):
    rob1, rob2 = 0, 0 

    for num in nums:
        temp = max(num + rob1, rob2)
        rob1= rob2
        rob2= temp

    return rob2

def rob(self, nums):
    if len(nums) < 2:
        return nums[0]

    loot = [[0] * len(nums)]
    loot[0] = nums[0] 
    loot[1] = max(nums[0],nums[1]) 

    for i in range(2, len(nums)):
        loot[i] = max(nums[i] + loot[i-2], loot[i-1])

    return loot[-1]

def rob(self, nums):
    if len(nums) < 2:
        return nums[0]

    dp = [0,0]
    dp[0] = nums[0] 
    dp[1] = max(nums[0],nums[1]) 

    for i in range(2, len(nums)):
        temp = max(nums[i] + dp[0], dp[1])
        dp[0] = dp[1]
        dp[1] = temp

    return dp[1]