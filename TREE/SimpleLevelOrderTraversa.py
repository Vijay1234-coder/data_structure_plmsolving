class Node:
    def __init__(self,val):
        self.left = None
        self.right = None
        self.val = val


def levelorder(root):
    if root==None:
        return
    queue = [root]
    level =[]
    nextqueue =[]
    res =[]

    while(queue!=[]):
        for cur in queue:
            level.append(cur.val)

            # cur = queue.pop(0)
            # print(cur.val,end=" ")
            # print(queue)

            if cur.left!=None:
                queue.append(cur.left)
            if cur.right!=None:
                queue.append(cur.right)







root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.right.left = Node(6)
root.right.right = Node(7)
root.left.left = Node(4)
root.left.right = Node(5)

levelorder(root)