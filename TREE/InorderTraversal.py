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
    ''' 1. Push root  to stack 1
        2. run a while loop s1 is not empty
            pop top of stack 1  and push it to stack 2
           i) check left of poped element if its not none  then add to stack 1
           ii) push poped elements right to stack 1
        3. print elements of stack2 in reverse order '''

    if root==None:
        return []
    s1 =[root]
    s2 = []
    while s1!=[]:
        poped = s1.pop()
        s2.append(poped.data)
        if poped.left!=None:
            s1.append(poped.left)
        if poped.right!=None:
            s1.append(poped.right)
    s2.reverse()
    return s2
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
    queue = [root]
    next_queue = []
    result = []
    level  = []

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




