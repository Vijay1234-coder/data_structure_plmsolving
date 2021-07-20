class BinaryTree(object):
    def __init__(self,rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None
    def insertLeft(self,newNode):
        if self.leftChild==None:
            self.leftChild=BinaryTree(newNode)
        else:
            t=BinaryTree(newNode)
            t.leftChild=self.leftChild
            self.leftChild=t

    def insertRight(self,newNode):
        if self.rightChild==None:
            self.rightChild=BinaryTree(newNode)
        else:
            t=BinaryTree(newNode)
            t.rightChild=self.rightChild
            self.rightChild= t
    def getleftChild(self):
        return self.leftChild

    def getrightChild(self):
        return self.rightChild
    def setRootVal(self,obj):
        self.key=obj
    def getRootVal(self):
        return  self.key

r=BinaryTree('a')
r.insertLeft('b')
r.insertRight('c')
print(r.getleftChild()) # We will get the instance of binnary tree because getLeftChild return t which is object or instace of BinaryTree class
print(r.getleftChild().getRootVal()) # Here it will shows the root value of that leftChild which is our value of leftChild



