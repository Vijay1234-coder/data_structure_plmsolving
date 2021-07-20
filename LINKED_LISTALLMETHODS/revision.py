class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None

    def print_ll(self):
        if self.head == None:
            print("Linked list is empty ")
        else:
            n = self.head
            while(n != None):
                print(n.data,"-->", end =" ")
                n = n.next

    def insert_end(self,data):
        new_node = Node(data)
        if self.head ==None:
            self.head = new_node
        else:
            n = self.head
            while n.next!=None:
                n=n.next
            n.next = new_node
    def mergesort(self,head):
        if head == None or head.next==None:
            return head
        mid = self.findmid(head)
        nexttomid  = mid.next
        mid.next = None
        left =  self.mergesort(head)
        right =  self.mergesort(nexttomid)

        sorted_lis = self.merge(left,right)
        return sorted_lis




    def merge(self,l,r):
        if l==None:
            return r
        if r==None:
            return l
        result =None
        if l.data<=r.data:
            result =l
            result.next = self.merge(l.next,r)
        else:
            result = r
            result.next = self.merge(l, r.next)
        return result




    def findmid(self,head):
        if head==None:
            return head
        fast =head
        slow =head
        while fast.next!=None and fast.next.next!=None:
            fast= fast.next.next
            slow = slow.next
        return slow





# def printList(head):
#     if head is None:
#         print(' ')
#         return
#     curr_node = head
#     while curr_node:
#         print(curr_node.data, end = " ")
#         curr_node = curr_node.next
#     print(' ')


l = LinkedList()
l.insert_end(30)
l.insert_end(100)
l.insert_end(10000)
l.insert_end(20)
l.head = l.mergesort(l.head)
# printList(l.head)
l.print_ll()


























