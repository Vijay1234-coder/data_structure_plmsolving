class Node:
    def __init__(self,val):
        self.left = None
        self.right = None
        self.val = val

def inorder_recurr(root):
    if root==None:
        return []
    else:
        return inorder_recurr(root.left)+[root.val]+inorder_recurr(root.right)
def inorderIter(root):
    stack =[]
    result=[]
    while root!=None or stack!=[]:
        while root!=None:
            stack.append(root)
            root = root.left
        root = stack.pop()
        result.append(root.val)
        root = root.right
    return result
def postorder_rec(root):
    if root==None:
        return []
    else:
        return postorder_rec(root.left)+postorder_rec(root.right)+[root.val]
def postorder_iter(root):
    stack =[]
    result =[]
    while root!=None or stack!=[]:
        while root!=None:
            stack.append(root)
            root =root.left
        temp = stack[-1].right  # here it store the right of current root
        if temp!=None: # if current root's right exist then we make it as a root
            root =temp
        else: # if not exist then there are two cases arrise 1. is okaay that root is ans 2. if it is right child of it s parent then after printing it we need to priont its parent also becaouse  left right root
            temp = stack.pop()
            result.append(temp.val)
            while stack!=[] and temp == stack[-1].right: # after poping current left next which left in stack is its parent node
                temp = stack.pop() # we checked if temp which is current left is right of its parent then we need to print its parent also
                result.append(temp.val)
    return result

def preorder_recur(root):# ROOT LEFT RIGHT
    if root==None:
        return []
    else:
        return [root.val]+preorder_recur(root.left)+preorder_recur(root.right)
def preorder_iter(root):
    if root==None:
        return []

    result =[]
    stack = [root]

    while stack!=[]:

        root =stack.pop()
        result.append(root.val)

        if root.right!=None:  # first we are checking right because while poping from stack left come first
            stack.append(root.right)
        if root.left!=None:
            stack.append(root.left)
    return result

def leve_order(root):
    queue =[root]
    next_queue = []
    result =[]
    level  =[]

    while queue!=[]:
        for root in queue:
            level.append(root.val)
            if root.left!=None:
                next_queue.append(root.left)
            if root.right!=None:
                next_queue.append(root.right)
        result.append(level)
        level =[]
        queue = next_queue
        next_queue=[]
    return result


def Zigzag(root):
    if root==None:
        return []
    queue =[root]
    next_queue =[]
    level =[]
    result =[]
    count =0
    while queue!=[]:
        count+=1
        for root in queue:
            level.append(root.val)
            if root.left != None:
                next_queue.append(root.left)
            if root.right != None:
                next_queue.append(root.right)


        if count%2==0:
            level.reverse()
        result.append(level)
        level = []
        queue = next_queue
        next_queue = []
    return result




root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.right.left = Node(6)
root.right.right = Node(7)
root.left.left = Node(4)
root.left.right = Node(5)
print(inorder_recurr(root))
print("-------------iterativeway----------------")
print(inorderIter(root))
print("-----------POST ORDER RECURRSIVE_________________")
print(postorder_rec(root))
print("-----------POST ORDER iterative_________________")
print(postorder_iter(root))
print("-----------PRE ORDER recurrsive_________________")
print(preorder_recur(root))
print("-----------PRE ORDER ITERATIVE_________________")
print(preorder_iter(root))
print("-----------LEVEL ORDER TRAVERSAL________________")
print(leve_order(root))
print("-----------Zig Zag ORDER TRAVERSAL________________")
print(Zigzag(root))




