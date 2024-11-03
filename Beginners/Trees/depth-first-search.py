class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

# insert a new node as a child of the leaf.
def insertBST(root, val):
    if not root:
        return TreeNode(val)
    # insert into the right subtree
    elif val > root.val:
        root.right = insertBST(root.right, val)
    # insert into the left subtree
    elif val < root.val:
        root.left =  insertBST(root.left, val)
    
    return root
    
def inorder(root):
    if not root:
        return
    inorder(root.left)
    print(root.val)
    inorder(root.right)

def reverseorder(root):
    if not root:
        return
    reverseorder(root.right)
    print(root.val)
    reverseorder(root.left)

def preorder(root):
    if not root:
        return
    print(root.val)
    preorder(root.left)
    preorder(root.right)

def postorder(root):
    if not root:
        return
    preorder(root.left)
    preorder(root.right)    
    print(root.val)

root = TreeNode(4) 
insertBST(root, 3)
insertBST(root, 2)
insertBST(root, 6)
insertBST(root, 5)
insertBST(root, 7)

print("inorder")
inorder(root)
print("preorder")
preorder(root)
print("postorder")
postorder(root)
print("reverseorder")
reverseorder(root)