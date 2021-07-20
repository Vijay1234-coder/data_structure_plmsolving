def removeDuplicates(head):
    if head == None and head.next == None:
        return
    n = head
    while n.next != None:
        if n.data == n.next.data:
            n.next = n.next.next
        else:
            n = n.next
    return
