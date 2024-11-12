class TreeNode:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def insertBTS(val, root):
    if root == None:
        return TreeNode(val)
    
    if val > root.val:
        root.right = insertBTS(val, root.right )
    elif val < root.val:
        root.left = insertBTS(val, root.left )

    return root

def inorderBTS(root):
    if not root:
        return
    inorderBTS(root.left)
    print(root.val)
    inorderBTS(root.right)

# Determine if a path exist from the root of the tree
# to a leaf node. it may bit contain any zeroes.
def backtracking(root):
    stack = []
    def leafPath(root):
        if not root or root.val == 0:
            return False 
        stack.append(root.val)
        if not root.left and not root.right:
            return True
        if leafPath(root.left):
            return True
        if leafPath(root.right):
            return True     
        stack.pop()
        return False
    
    if leafPath(root):
        print(stack)
    else:
        print("No solution found!")
        print(stack)

# root = TreeNode(4)
# insertBTS(0,root)
# insertBTS(1,root)
# insertBTS(5,root)
# insertBTS(7,root)
# inorderBTS(root)

root = TreeNode(4)
root.left = TreeNode(0)
root.left.right = TreeNode(7)
root.right = TreeNode(1)
root.right.left = TreeNode(2)
root.right.right = TreeNode(0)
#inorderBTS(root)

backtracking(root)