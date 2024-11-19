#https://leetcode.com/problems/subsets/
class Solution:
         # [1,2,3]
        #                []
       #       [1]                    []
     #   [1,2]       [1]        [2]      []
   # [1,2,3] [1,2] [1,3] [1] [2,3]  [2] [3] []
    def subsets(self, nums):
        subsets = []
        curr_subset = []
        def helper(i):
            if i >= len(nums):
                subsets.append(curr_subset[:])
                return
            curr_subset.append(nums[i])
            helper(i + 1)
            curr_subset.pop()
            helper(i + 1)

        helper(0)
        return subsets
