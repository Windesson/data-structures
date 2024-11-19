#https://leetcode.com/problems/combination-sum/
class Solution:
    def combinationSum(self, candidates, target: int):
        subsets = []
        curr_subset = []
        def helper(i):
            if i >= len(candidates) or sum(curr_subset) > target:
                return
            if sum(curr_subset) == target:
                subsets.append(curr_subset[:])
                return 

            curr_subset.append(candidates[i])
            helper(i)
            curr_subset.pop()
            helper(i + 1)

        helper(0)
        return subsets
        


        