class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LL:
    def __init__(self):
        self.head =None
    def insert(self,data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        else:
            n =self.head
            while n.next!=None:
                n = n.next
            n.next = new_node
    def display(self):
        if self.head==None:
            print("LL is empty")
        else:
            n = self.head
            while n!=None:
                print(n.data,"-->",end="")
                n = n.next
    def remove_duplicate(self):
        if self.head==None or self.head.next==None:
            return
        n =self.head
        while n.next!=None:
            if n.data == n.next.data:
                n.next=n.next.next
            else:
                n = n.next









l =LL()
l.insert(2)
l.insert(2)
l.insert(5)
l.insert(6)
l.insert(7)
l.insert(7)
l.display()
print(" ")
l.remove_duplicate()
l.display()

