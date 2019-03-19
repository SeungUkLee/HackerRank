

"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""
def levelOrder(root):
    q = [root]
    while q:
        size = len(q)
        for _ in range(size):
            cur_node = q.pop(0)
            print(cur_node.info, end=" ")
            if cur_node.left:
                q.append(cur_node.left)
            if cur_node.right:
                q.append(cur_node.right)

