# 112. Path Sum
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def hasPathSum(self, root, targetSum: int) -> bool:
        curr_sum = 0
        def leafHasPathSum(root):
            nonlocal curr_sum, targetSum
            if not root:
                return False

            curr_sum += root.val
            if not root.left and not root.right and curr_sum == targetSum:
                return True
            if leafHasPathSum(root.left):
                return True
            if leafHasPathSum(root.right):
                return True
            
            curr_sum -= root.val
            return False

        return leafHasPathSum(root)



        