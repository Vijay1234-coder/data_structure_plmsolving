
'''Important'''
'''      WhenEver u have to find kth  smallest --- Always use max heap  

  Time Complexity will be O(Nlogk)             '''
from heapq  import heappop,heappush,heapify


# by default heapq is min heap but if we push -ve of element its will be mini mum and it will be at to pop() it change the sign and becomes
# max heap
a =[7,10,4,3,20,15]
maxheap = []
k=3
# heapify(maxheap)


for i in a:
    heappush(maxheap,-i)
    if len(maxheap)>k:
        maxheap.pop(0)
print(-maxheap[0])





