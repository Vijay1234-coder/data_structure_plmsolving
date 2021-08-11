'''  Important '''
'''Given an unsorted array and two numbers x and k, find k closest values to x.
Input : arr[] = {10, 2, 14, 4, 7, 6}, x = 5, k = 3   
Output : 4 6 7   '''

from heapq import heappop,heappush,heapify

arr =[10,2,14,4,7,6 ]
k=3
x =5
n =len(arr)

max_heap = []
for i in range(n):
    heappush(max_heap,(-abs(arr[i]-x),arr[i]))
    if len(max_heap)>k:
        heappop(max_heap)
while max_heap!=[]:
    res = heappop(max_heap)
    print(res[1],end=" ")



