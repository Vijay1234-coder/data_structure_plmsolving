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
    def print_LL_reverse(self): # Backward Traversal
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
    def insert_empty(self,data):
        if self.head == None:
            new_node = Node(data)
            self.head = new_node
        else:
            print("Linker List is not empty")

    def insert_front(self,data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        else:
            new_node.nref = self.head
            self.head.pref = new_node
            self.head = new_node

    def insert_end(self, data):
        new_node = Node(data)
        if self.head == None:
            print("Linked list is empty")
            return
        else:
            n = self.head
            while n.nref != None:
                n = n.nref
            n.nref = new_node
            new_node.pref = n


    def insert_after(self,data,x):

        new_node = Node(data)
        if self.head == None:
            print("LL is empty")
            return
        else:
            n = self.head
            while n!=None:
                if n.data == x:
                    break
                n= n.nref
            if n == None:# above while loop will be false due to 2 reason n==None means did't find x
                print("Given node is not Present is Linked List")
            else:# we got the x

                # 1.  if n is last node we have to add after last node
                if n.nref == None:
                    n.nref = new_node
                    new_node.pref = n
                else: # when adding rather than last element
                    new_node.nref = n.nref
                    n.nref.pref =new_node
                    n.nref = new_node
                    new_node.pref = n

    def insert_before(self, data, x):
        new_node = Node(data)

        if self.head == None:
            print("Linked List is empty")
            return
        else:

            if self.head.data == x:
                new_node.nref = self.head
                self.head.pref = new_node
                self.head = new_node

            else:
                n=self.head
                while n.nref != None:
                    if n.nref.data == x:
                        break
                    n = n.nref
                # n.nref ===None
                if n.nref==None:
                    print("node not present in ll")
                    return
                else:
                    new_node.nref = n.nref
                    n.nref.pref = new_node
                    new_node.pref =n
                    n.nref  = new_node


















l = DoublyLL()
l.insert_front(10)
l.insert_front(20)
l.insert_front(30)
l.insert_front(40)
l.insert_end(1000)
l.insert_after(2000,40)
l.insert_after(500,1000)
l.insert_before(400,20)
l.insert_before(3100,40)
l.print_LL()
print(" " )
print("printing Reverse order")
l.print_LL_reverse()



