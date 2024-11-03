# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]):
        queue = deque() 
        res = []

        if root:
            queue.append(root)

        while len(queue) > 0:
            rightSide = None
            for _ in range(len(queue)):
                node = queue.popleft()
                rightSide = node
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(rightSide)
        return res