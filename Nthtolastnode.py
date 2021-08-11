'''Write a fnc that takes a head node and an integer value n and returns the nth to last node in the linked List '''

class Node(object):
    def __init__(self,value):
        self.value=value
        self.nextnode=None

def nth_to_last_node(n,head):
    left_pointer=head
    right_pointer=head
    # now we set distance betweeen these two pointer equal to n so that when right pointer reaches to end  of linked_list
    # the left_Pointer will be at the distance of n from right pointer and value of left_pointer will be answer
    # for that we will start a for loop which run n no. of times and during each iteration it will increase the right_pointer
    #and keep checking the base case
    for i in range(n-1):
        if right_pointer.nextnode==None:
            raise LookupError("Error: n is larger than linked list")
        right_pointer=right_pointer.nextnode

    #now we run the loop untile the right_pointer reaches end
    while right_pointer.nextnode!=None:
        left_pointer=left_pointer.nextnode
        right_pointer=right_pointer.nextnode

    return left_pointer

a=Node(1)
b=Node(2)
c=Node(3)
d=Node(4)
a.nextnode=b
b.nextnode=c
c.nextnode=d

print("{}-->{}-->{}-->{}".format(a.value,a.nextnode.value,b.nextnode.value,c.nextnode.value))
nth_address=nth_to_last_node(2,a)
print("nth elemnent from last is : {}".format(nth_address.value))


