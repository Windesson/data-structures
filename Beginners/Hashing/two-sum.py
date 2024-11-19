class Solution:
    def twoSum(self, nums, target):
        memo = dict()
        for index in range(len(nums)):
            num = nums[index]
            remainder = target - num
            if remainder in memo:
                return [memo[remainder], index]
            memo[num] = index
        return []