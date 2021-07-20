'''Find first and last positions of an element in a sorted array

Given a sorted array with possibly duplicate elements, the task is to find indexes of first and last occurrences of an element x in the given array.
Examples:

Input : arr[] = {1, 3, 5, 5, 5, 5, 67, 123, 125}
        x = 5
Output : First Occurrence = 2
         Last Occurrence = 5

Input : arr[] = {1, 3, 5, 5, 5, 5, 7, 123, 125 }
        x = 7
Output : First Occurrence = 6
         Last Occurrence = 6
'''

'''bruit force approach  O(N)  '''

# def firstLastOcurrance(arr,target):
#     start = -1
#     end = -1
#     n=len(arr)
#     for i in range(n):
#         if (target != arr[i]):
#             continue
#         elif(target == arr[i]):
#             if start==-1:
#                 start = i
#             end = i
#     if (start == -1):
#         return "TARGET IS NOT PRESENT IN THE LIST"
#
#
#     result = "starts at index: {0} and ending at index : {1}".format(start,end)
#     return result
#
#
#
#
# print(firstLastOcurrance([1,3,5,5,5,5,67,123,125],5))


'''Efficient and O(Log(n))   :     using Binary Search'''


def firstOcurrance(arr,target):
    firstResult = -1
    start = 0
    end = len(arr)-1

    while(start<=end):
        mid = start + (end-start)//2

        if arr[mid]==target:
            firstResult = mid
            end = mid - 1

        elif(target > arr[mid]):
            start = mid + 1
        else:
            end = mid-1
    return ( lastOcurrance(arr,target) - firstResult + 1)



def lastOcurrance(arr,target):
    lastResult = -1
    start = 0
    end = len(arr) - 1

    while (start <= end):
        mid = start + (end - start) // 2

        if arr[mid] == target:
            lastResult = mid
            start= mid + 1

        elif (target > arr[mid]):
            start = mid + 1
        else:
            end = mid - 1
    return lastResult


arr=[1,3,5,5,5,5,67,123,125]

print(firstOcurrance(arr,5))





