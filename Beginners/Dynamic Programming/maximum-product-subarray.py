class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        currMax, currMin = 1, 1

        for num in nums:
            if num == 0:
                currMax, currMin = 1, 1
            else:
                temp = currMax * num
                currMax = max(num, num*currMax, num*currMin)
                currMin = min(num, temp, num*currMin)
                res = max(res, currMax)
        return res


