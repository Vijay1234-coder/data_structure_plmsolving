def isPalindrome(self, head):
    if head.next == None:
        return True
    fast = head
    slow = head
    while fast != None and fast.next != None:
        fast = fast.next.next
        slow = slow.next
    curr = slow
    prev = None
    while curr != None:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    fast = head

    while prev != None:
        if fast.data != prev.data:
            return False
        else:
            fast = fast.next
            prev = prev.next
    return True