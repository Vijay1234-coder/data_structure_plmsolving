from heapq import heappop,heappush


class Node:
    def __init__(self,data):
        self.data = data
        self.next  =  None
        self.prnext = None
class LL:
    def __init__(self):
        self.head = None
    def insert(self,data):
        new_node  =Node(data)
        if self.head == None:
            self.head = new_node
        else:
            n = self.head
            while n.next!=None:
                n = n.next
            n.next = new_node

    def display(self):
        if self.head == None:
            print("LL is empty")
        else:
            n = self.head
            while n!=None:
                print(n.data,"-->",end="")
                n =n.next
    def sort(self,k):
        min_heap =[]
        prev = None
        n = self.head
        while n!=None:
            heappush(min_heap,n.data)
            if len(min_heap)>k:
                val = heappop(min_heap)
                if prev==None:
                    prev = Node(val)
                    self.head = prev
                else:
                    prev.next = Node(val)
                    prev = prev.next

            n = n.next
        while min_heap!=[]:
            prev.next = Node(heappop(min_heap))
            prev= prev.next
        prev.next =None
l = LL()
l.insert(3)
l.insert(6)
l.insert(2)
l.insert(12)
l.insert(56)
l.insert(8)
l.display()
print("")
l.sort(2)
l.display()
