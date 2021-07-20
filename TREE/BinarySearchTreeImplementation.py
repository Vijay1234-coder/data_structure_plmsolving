
'''"""
              50
           /     \
          30      70
         /  \    /  \
       20   40  60   80 """'''





class Node:
    def __init__(self,key):
        self.key   = key
        self.left  = None
        self.right = None

# Below Function Find the Minimum key of the tree
def minOfrightPart(root):
    curr =root
    while curr.left != None: # we are chceking in right side only because we want minimum key
        curr = curr.left
    return curr






def search(root,key):
    if root==None:
        return "Not Found"
    if root.key ==key:
        return "Found"
    if key>root.key:
        return search(root.right,key)
    return search(root.left,key)










def insert(root,key):
    if root == None:#tree is empty make first inserted node as root node
        return Node(key)
    if key < root.key:
        root.left = insert(root.left,key)
    else:
        root.right = insert(root.right,key)
    return root


def delete(root,key):
    if root == None: # when Root is empty this is Base Case
        return root
    if key > root.key:
        root.right = delete(root.right,key)
    elif key < root.key:
        root.left = delete(root.left,key)
    else:# when our tareget key is root.key
        # there may be 3 cases
        # case 1. root has 0 child
        # case 2.  root has 1 child

        if root.left==None: # this two if statement will take care two cases
            temp = root.right
            root = None
            return temp
        elif root.right == None:
            temp = root.left
            root =None
            return temp
        # case 3. root has 2 child
        # Case 3.1:after deleting the root node we have to set the smallest key of right part  as ROOT and then remove that from that right position
        temp = minOfrightPart(root.right) # temp = minimum key in  right subtree or child
        root.key = temp.key
        root.right = delete(root.right,temp.key)
    return root







def inorder(root):
    stack =[]
    result =[]
    while root!=None or stack!=[]:
        while root!=None:
            stack.append(root)
            root =root.left
        root = stack.pop()
        result.append(root.key)
        root =root.right
    return result






















root = None

root = insert(root, 50)
root = insert(root, 30)
root = insert(root, 20)
root = insert(root, 40)
root = insert(root, 70)
root = insert(root, 60)
root = insert(root, 80)
print(inorder(root))
print("-------------------AFTER DELETE OPERATION PERFORMED--------------------")
print(search(root,100))
print(delete(root,100))
print(inorder(root))


