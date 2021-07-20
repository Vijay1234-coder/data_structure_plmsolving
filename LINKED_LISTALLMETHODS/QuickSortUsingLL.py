class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class LL:
    def __init__(self):
        self.head = None
    def Print_LL(self):
        if self.head == None:
            print("LL is empty")
        else:
            n = self.head
            while n!= None:
                print(n.data,"-->",end=" ")
                n = n.next
    def insert_end(self,data):
        new_node  =Node(data)
        if self.head == None:
            self.head = new_node
        else:
            n = self.head
            while n.next!=None:
                n = n.next
            n.next = new_node


    def quickSort(self,start,end):
        if start == end:
            return
        p_prev = self.partition(start,end)   # return previous node of partision node
        self.quickSort(start,p_prev)
        if p_prev!=None and p_prev == start: # if only one element left of partion node
            self.quickSort(p_prev.next,end)

        elif (p_prev!=None and p_prev.next !=None): # if partition node is not last and its prev is separating element to right side
            self.quickSort(p_prev.next.next,end)



    def partition(self,start,end):
        if start == end or start==None or end == None:
            return start
        part_node = start
        part_prev = start
        pivot = end.data

        while start!=end:
            if(start.data < pivot):
                part_prev = part_node
                temp  = part_node.data
                part_node.data = start.data
                start.data = temp
                part_node = part_node.next
            start =start.next

        temp = part_node.data
        part_node.data = pivot
        end.data = temp
        return part_prev













l = LL()
l.insert_end(10)
l.insert_end(100)
l.insert_end(40)
l.insert_end(20)
l.insert_end(50)
l.Print_LL()
print("")
n = l.head
while n.next != None:
    n = n.next
l.quickSort(l.head,n)

print("sorted array:--------")

l.Print_LL()






