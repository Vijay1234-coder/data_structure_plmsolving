class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LL:
    def __init__(self):
        self.head = None
    def display(self):
        if self.head == None:
            # when ll is empty
            print("ll is empty")
        else:
            n = self.head
            while n!=None:
                print(n.data,"-->",end="")
                n = n.next
    def insert_front(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    def insert_end(self,data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        else:
            n = self.head
            while n.next!=None:
                n = n.next
            n.next  = new_node
    def reverse(self,k):
        stack  = []
        n = self.head
        prev =None
        while n!=None:
            val =0
            while n!=None and val<k:
                stack.append(n.data)
                n = n.next
                val+=1
            while stack!=[]:
                if prev == None:
                    prev = Node(stack.pop())
                    self.head = prev
                else:
                    prev.next = Node(stack.pop())
                    prev = prev.next
            prev.next =None









l = LL()
l.insert_end(1)
l.insert_end(2)
l.insert_end(2)
l.insert_end(4)
l.insert_end(5)
l.insert_end(6)
l.insert_end(7)
l.insert_end(8)

l.display()
print(" ")
print("kk..")
l.reverse(4)

l.display()