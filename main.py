class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

root = TreeNode(1)
root.right = TreeNode(6)
root.right.left = TreeNode(3)

def nodeSumI(root):
    return root.val == (root.left.val + root.right.val)

def nodeSumII(root):
    #ternary conditional operator 
    left = root.left.val if root.left else 0 
    #value is true if condition else false value 
    right = root.right.val if root.right else 0

    return root.val == (left + right)
def leftMost(root):
    #Base case if there is no tree 
    if not root:
        return None
    
    while root.left:
        root = root.left
    return root.val

def leftMostRecursive(root):
    if not root:
        return None
    
    if not root.left:
        return root.val
        
    return leftMostRecursive(root.left)

def inorderTraversal(root):
    values = []
    return inorderHelper(root, values)

def inorderHelper(currerntNode, values):
    if not currerntNode:
        return values
    inorderHelper(currerntNode.left, values)
    values.append(currerntNode.val)
    inorderHelper(currerntNode.right, values)
    return values
        
print(nodeSumII(root))
print(leftMostRecursive(root))
print(inorderTraversal(root))

