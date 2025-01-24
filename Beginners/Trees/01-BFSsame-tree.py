# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        Aqueue = deque([p])
        Bqueue = deque([q])

        while Aqueue and Bqueue:
            if len(Aqueue) != len(Bqueue):
                return False

            for _ in range(len(Aqueue)):
                a = Aqueue.popleft()
                b = Bqueue.popleft()

                if not a and not b:
                    continue 
                if not a or not b:
                    return False
                if a.val != b.val:
                    return False
                
                Aqueue.extend([a.left, a.right])
                Bqueue.extend([b.left, b.right])
        
        return True