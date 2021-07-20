class Node:
    def __init__(self,data):
        self.data = data
        self.nref = None
        self.pref = None
class DoublyLL:
    def __init__(self):
        self.head = None

    def print_LL(self):    # Forward Direction Traversal
        if self.head ==None:
            print("Empty LL")
        else:
            n = self.head
            while(n != None):
                print(n.data,"-->",end =" ")
                n = n.nref

    def print_LL_reverse(self): #Backward Traversal
        if self.head == None:
            print("Linked list is empty")
        else:
            n = self.head
            while n.nref !=None:
                n = n.nref
            # we come out loop  now we are at last node

            while n!=None :
                print(n.data, "-->",end = " ")
                n = n.pref




    def insert_end(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        else:
            n = self.head
            while n.nref != None:
                n = n.nref
            n.nref = new_node
            new_node.pref = n

    def insertionSort(self,head):
        n = head
        n = n.nref
        while n!=None:
            curr = n
            while curr.data < n.pref.data and n!= None:
                temp = n.data
                n.data = n.pref.data
                n.pref.data = temp
                n = n.pref








            n = n.nref










l = DoublyLL()

l.insert_end(40)
l.insert_end(10)
l.insert_end(20)
l.insert_end(110)
l.insertionSort(l.head)
l.print_LL()




















