

# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
class Node:
      def __init__(self,info): 
          self.info = info  
          self.left = None  
          self.right = None 
           

       // this is a node of the tree , which contains info as data, left , right
'''
def height(root):
    L = []
    def preorder(root, h):
        if root is None:
            L.append(h-1)
            return
        preorder(root.left, h + 1)
        preorder(root.right, h + 1)
    preorder(root, 0)
    return max(L)

