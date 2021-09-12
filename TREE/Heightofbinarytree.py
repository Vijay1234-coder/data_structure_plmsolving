class Node:
    def __init__(self,key):
        self.key  = key
        self.left = None
        self.right = None

def height(root):
    if root==None:
        return 0
    else:
        return max(height(root.left),height(root.right))+1


root = Node(2)
root.left = Node(3)
root.right = Node(4)
root.left.left = Node(5)

print(height(root))
