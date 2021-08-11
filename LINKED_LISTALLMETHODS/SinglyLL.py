class Node:
    def __init__(self,data):
        self.data=data
        self.next_node=None


class LinkedList:
    def __init__(self):
        self.head=None

    def display(self):
        if self.head==None:
            print("Linked List is empty!")
        else:
            n = self.head
            while n!=None:   # we keep traverse till last
                print(n.data,"--->",end="")
                n = n.next_node

    def insert_front(self,data):
        new_node= Node(data)
        new_node.next_node = self.head
        self.head = new_node

    def insert_atEnd(self,data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        else:
            n = self.head
            while n.next_node!=None:
                n = n.next_node
            n.next_node = new_node


    def insert_after(self,data,x):
        n=self.head           # first node of ll
        while n is not None:   #we are traversing the ll to find x node  while loop can break in two condition
                                #1. if ll is empty or yoiu dont find x means you keep traversion till last,,2. if x is found
            if x == n.data:      #if we found x in ll then brek the loop no need to traverse
                break
            n = n.next_node      # if not found search to next node

        if n == None:
            print("node is not Found Plz enter valid node after which you wants to insert")
        else:
            new_node=Node(data)
            new_node.next_node=n.next_node
            n.next_node= new_node


    def insert_Before(self,data,x):
        if self.head is None:
            return

        if self.head.data==x:   # this is the case when elements x present at 1st postion similar to insert at front
            new_node = Node(data)
            new_node.next_node = self.head
            self.head = new_node
            return
        else:
            n = self.head
            while n.next_node != None:  # traversing list till before last element
                if n.next_node.data == x:  # found x
                    break
                n = n.next_node
            if n.next_node is None: # if did'nt find any such x
                return "not found any x"
            else:
                new_node = Node(data)
                new_node.next_node = n.next_node
                n.next_node = new_node













l = LinkedList()
l.insert_front(10)
l.insert_Before(20,10)
l.insert_Before(30,10)
l.insert_after(10000,30)
l.display()




