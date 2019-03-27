""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""
def checkBST(root):
    if not root:
        return True
        
    stack = [(root, None, None), ] 
    while stack:
        root, lower_limit, upper_limit = stack.pop()
        if root.right:
            if root.right.data > root.data:
                if upper_limit and root.right.data >= upper_limit:
                    return False
                stack.append((root.right, root.data, upper_limit))
            else:
                return False
        if root.left:
            if root.left.data < root.data:
                if lower_limit and root.left.data <= lower_limit:
                    return False
                stack.append((root.left, lower_limit, root.data))
            else:
                return False
    return True

