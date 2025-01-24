# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        q = deque([root])
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                
                if node.val == subRoot.val:
                    same = self.isSame(node, subRoot)
                    if same:
                        return True #else keep looking in case duplicate values

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return False

    def isSame(self, p, q):
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        
        return self.isSame(p.left, q.left) and self.isSame(p.right, q.right)
        