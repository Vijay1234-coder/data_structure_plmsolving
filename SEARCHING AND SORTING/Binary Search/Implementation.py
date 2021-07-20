def binary_search(arr,target):
    first = 0
    last = len(arr)-1
    found = False
    while (first <= last) and (found == False):
        mid = (first+last)//2
        if arr[mid] == target:
            print("found at index {0}".format(mid))
            found = True
        else:
            if target > arr[mid]:
                first = mid +1
            else:
                last = mid - 1

    return found



arr = [1,2,3,4,5,6,7,8,9,10]
print(binary_search(arr,15))


'''recursive Binary Search'''


# def rec_binary_search(arr,target):
#     mid = len(arr)//2
#     # Base Case
#     if len(arr)==0:
#         return False
#     else:
#         if arr[mid] == target:
#             return True
#         else:
#             if target < arr[mid]:
#                 return rec_binary_search(arr[:mid], target)
#             else:
#                 return rec_binary_search(arr[mid+1:], target)
#
#
#
#
#
# arr = [1,2,3,4,5,6,7,8,9,10]
# print(rec_binary_search(arr,1))