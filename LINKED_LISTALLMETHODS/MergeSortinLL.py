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

    def mergeSort(self,head):
        if head == None or head.next ==None:
            return head
        mid  = self.findMid(head)
        nexttomid = mid.next
        mid.next = None
        left = self.mergeSort(head)
        right = self.mergeSort(nexttomid)
        sortedlist = self.mergingLR(left,right)

        return sortedlist


    def findMid(self,head):
        if head == None:
            return head

        slow = head
        fast = head

        while (fast.next != None and
               fast.next.next != None):
            slow = slow.next
            fast = fast.next.next

        return slow
    def mergingLR(self,l,r):
        if l==None:
            return r
        if r == None:
            return l
        result = None
        if l.data<=r.data:
            result = l
            result.next = self.mergingLR(l.next,r)
        else:
            result = r
            result.next = self.mergingLR(l,r.next)
        return result
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

l.head = l.mergeSort(l.head)
# printList(l.head)
l.print_ll()


























