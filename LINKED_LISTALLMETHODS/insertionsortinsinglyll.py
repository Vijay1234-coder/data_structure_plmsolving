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
            while n!= None:   # we keep traverse till last
                print(n.data,"--->",end="")
                n = n.next_node



    def insert_atEnd(self,data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node


        else:
            n = self.head
            while n.next_node!=None:
                n = n.next_node
            n.next_node = new_node

    # def insertionSort(self,head):
    #     start = Node(0)
    #     start.next_node = head
    #     curr = head
    #     prev = start
    #     while curr != None:
    #         if curr.next_node != None and curr.next_node.data <curr.data:
    #             while prev.next_node != None and prev.next_node.data<curr.next_node.data:
    #                 prev = prev.next_node
    #             temp = prev.next_node
    #             prev.next_node = curr.next_node
    #             curr.next_node = curr.next_node.next_node
    #             prev.next_node.next_node = temp
    #             prev = start
    #         else:
    #             curr = curr.next_node
    #     return start.next_node


    def sort(self,head):
        dummy = Node(0)


        curr = head

        while curr != None:
            prev = dummy
            next = dummy.next_node
            temp = curr.next_node

            while next!=None:
                if next.data > curr.data:
                    break
                prev = next
                next = next.next_node
            curr.next_node = next
            prev.next_node = curr
            curr = temp


        return dummy.next_node





























l = LinkedList()
l.insert_atEnd(100)
l.insert_atEnd(40)
l.insert_atEnd(50)
l.insert_atEnd(2)
l.display()
print("   ")
l.head = l.sort(l.head)
l.display()




