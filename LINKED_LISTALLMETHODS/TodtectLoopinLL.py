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


    def make_loop(self,x):
        if x==0:
            return
        n = self.head
        for i in range(1,x):
            n = n.next
        join_point = n
        while n.next!=None:
            n=n.next
        n.next = join_point

    def loop_usingdict(self):
        dict1 ={}
        n = self.head
        while n!=None:
            if n not in dict1:
                dict1[n]=1
                n = n.next
            else:
                return True
        return False
    def loop_fast_slow(self):
        fast = self.head
        slow = self.head
        while (fast!=None and fast.next!=None):
            slow = slow.next
            fast = fast.next.next
            if fast==slow:
                return True
        return False




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
print("  ")
l.make_loop(5)
print(l.loop_usingdict())
print(" ")
print("Loop using Fast slow method ")
print(l.loop_fast_slow())