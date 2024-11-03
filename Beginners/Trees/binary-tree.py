# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

def searchBST(self, root, val):
    if not root:
        return None
    elif val > root.val:
        return self.searchBST(root.right, val)
    elif val < root.val:
        return self.searchBST(root.left, val)

    return root

# nsert a new node as a child of the leaf.
def insertBST(self, root, val):
    if not root:
        return TreeNode(val)
    # insert into the right subtree
    elif val > root.val:
        root.right = self.insertBST(root.right, val)
    # insert into the left subtree
    elif val < root.val:
        root.left =  self.insertBST(root.left, val)
    
    return root

#Iteration
def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
    node = root
    while node:
        # insert into the right subtree
        if val > node.val:
             # insert right now
            if not node.right:
                node.right = TreeNode(val)
                return root
            else:
                node = node.right
        # insert into the left subtree
        else:
            # insert right now
            if not node.left:
                node.left = TreeNode(val)
                return root
            else:
                node = node.left
    return TreeNode(val)  

def minValueNode(root):
    curr = root
    while curr and curr.left:
        curr = curr.left
    return curr

def removeValueNode(root, val):
    if not root:
        return None
    elif val > root.val:
        root.right = removeValueNode(root.right, val)
    elif val < root.val:
        root.left = removeValueNode(root.left, val)
    else:
        # found it
        if not root.left and not root.right:
            return None
        elif not root.left:
            return root.right
        elif not root.right:
            return root.left
        else:
            # has two children
            minNode = minValueNode(root.right) 
            # minNode at most has one child to the right. simple case.
            root.val = minNode.val
            # everything to left is already smaller 
            # root.left do nothing
            root.right = removeValueNode(root.right, minNode.val)
    return root