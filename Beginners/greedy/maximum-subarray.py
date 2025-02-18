class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        curr_best = 0
        res = min(nums) -1
        for num in nums:
            curr_best = max(num, num + curr_best )
            res = max(curr_best, res)
        
        return res


            



        