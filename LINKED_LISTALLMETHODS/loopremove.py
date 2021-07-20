''' O(N) and space O(N)'''
def removeLoop(self, head):
    d = {}
    prev = None
    while head != None:
        if head not in d:
            d[head] = 1
            prev = head
            head = head.next
        else:
            prev.next = None
            break


'''O(N) and space is O(1)'''
# def removeLoop(self, head):
#     low = head
#     high = head
#     while low != None and high != None and high.next != None:
#         low = low.next
#         high = high.next.next
#         if high == low:
#             break
#
#     if low == head and high == head:
#         while (high.next != low):
#             high = high.next
#         high.next = None
#     elif (low == high):
#         low = head
#         while (low.next != high.next):
#             low = low.next
#             high = high.next
#         high.next = None
