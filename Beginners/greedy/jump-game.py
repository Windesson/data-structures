class Solution:
    def canJump(self, nums: List[int]) -> bool:

        goal = len(nums) - 1

        for index in range(len(nums) - 2, -1, -1):
            if index + nums[index] >= goal:
                goal = index
        
        return goal == 0
    

class Solution:
    def canJump(self, nums: List[int]) -> bool:

        memo = {}
        def helper(index = 0):
            if index in memo:
                return memo[index]
            if index == len(nums) - 1:
                return True
            if index >= len(nums):
                return False
            if index < len(nums) and nums[index] == 0:
                return False
            steps = nums[index]

            while steps > 0:
                if (helper(index+steps)):
                    memo[index] = True
                    return True
                steps -= 1
            
            memo[index] = False
            return False
        
        return helper()