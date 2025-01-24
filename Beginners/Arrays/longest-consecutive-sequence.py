class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        cache = set(nums)
        res = 0
        for num in nums:
            if num - 1 not in cache:
                lenght = 0 
                while num + lenght in cache:
                    lenght += 1 
                res = max(lenght, res)
        return res
    
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if len(nums) < 2:
            return len(nums)

        nums = sorted(set(nums))
        longest = 0
        curr = 1

        for i in range(1, len(nums)):
            if nums[i] - 1 == nums[i - 1]:
                curr +=1
            else:
                longest = max(curr, longest)
                curr = 1
        
        return max(curr, longest)





        