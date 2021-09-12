class Node:
    def __init__(self,data):
        self.data=data
        self.left= None
        self.right  = None
def ChildrenSum(root):
    if root==None: return True # NUll node is also a childsum
    if root.left==None and root.right==None: return True #leaf node is also a children sum

    sum =0
    if root.left!=None:sum+=root.left.data
    if root.right!=None: sum+=root.right.data

    return sum==root.data and ChildrenSum(root.left) and ChildrenSum(root.right)
root = Node(2)
root.left = Node(3)
root.right = Node(4)
root.left.left = Node(5)

print(ChildrenSum(root))