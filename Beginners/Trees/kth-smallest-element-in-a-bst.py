# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        items = []
        self.helper(root, k, items)
        return items[k-1]

    def helper(self, root, k, items):
        if not root:
            return
        self.helper(root.left, k, items)
        items.append(root.val)
        if len(items) == k:
            return
        self.helper(root.right, k, items)

class Solution2:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = k
        res = -1

        def helper(root):
            nonlocal count, res
            if not root:
                return
            helper(root.left)
            count -= 1
            if count == 0:
                res = root.val
                return
            helper(root.right)
            
        helper(root)
        return res