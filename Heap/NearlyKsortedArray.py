'''important'''
'''Given an array of n elements, where each element is at most k away from its target position, devise an algorithm that sorts in O(n log k) time. For example, let us consider k is 2, an element at index 7 in the sorted array, can be at indexes 5, 6, 7, 8, 9 in the given array.

Example:
Input : arr[] = [6, 5, 3, 2, 8, 10, 9]
k = 3 
Output : arr[] = {2, 3, 5, 6, 8, 9, 10}

here you have to use complexity O(NlogK)
you have to use min Heap so that if if we push element at the or at front of min heap min element will be present
and when you pop it when size greater than k it will give mini element '''


from heapq import heappop, heappush,heapify

arr =[6, 5, 3, 2, 8, 10, 9]
k = 3
min_heap = []
sorted_lis = []
for i in range(len(arr)):
    heappush(min_heap,arr[i])
    if len(min_heap)>k:
        res =heappop(min_heap)
        sorted_lis.append(res)
while min_heap!=[]:
    sorted_lis.append(heappop(min_heap))
print(sorted_lis)






