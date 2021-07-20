class Node(object):
    def __init__(self,data):         #https://www.geeksforgeeks.org/reverse-a-linked-list/
        self.data=data
        self.nextnode= None
def reverse(head):
    current=head
    nextnode = None
    previous = None
    while current!=None:
        nextnode = current.nextnode
        current.nextnode = previous
        previous = current
        current=nextnode

    return previous

a=Node(1)
b=Node(2)
c=Node(3)
d=Node(4)

a.nextnode=b
b.nextnode=c
c.nextnode=d

print(a.data,"-->",a.nextnode.data,"-->",b.nextnode.data,"-->",c.nextnode.data)
reverse(a)
print(d.data,d.nextnode.data ,c.nextnode.data,b.nextnode.data)
