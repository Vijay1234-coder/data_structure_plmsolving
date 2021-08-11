''' Important '''
'''   Whenever you have to find kth largest element use min Heap   
Time Compexity  O(nlogk)  '''
from heapq import heappop, heappush,heapify
a =[ 7, 10, 4, 3, 20, 15 ] #[3,4,7,10,15,20]
k=4

# find kth largest element

minheap =[]

for i in a:
    heappush(minheap,i)  # this will create a min heap store the min value at top  as k len got completed it will pop remaining smallest element
    if len(minheap) > k:
        minheap.pop(0)
print(minheap[0])

