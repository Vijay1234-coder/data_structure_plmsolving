

'''important:   '''

''' Consider an array of distinct numbers sorted in increasing order. The array has been rotated (clockwise) k number of times. Given such an array, find the value of k.
Examples:


Input : arr[] = {15, 18, 2, 3, 6, 12}
Output: 2
Explanation : Initial array must be {2, 3,
6, 12, 15, 18}. We get the given array after
rotating the initial array twice.

Input : arr[] = {7, 9, 11, 12, 5}
Output: 4

Input: arr[] = {7, 9, 11, 12, 15};
Output: 0'''


'''Note : you can check that number of rotation is equal to index of smallest element'''
'''because initially it is at 0th index but it moves slightly'''
'''bruit force approach is 1.we iterarte through the whole array find the minimum element and return its index '''
''' complexity of it will be O(N) '''

# def rotationCount(arr,n):
#     Min = arr[0]
#     for i in range(1,n):
#         if arr[i]<Min:
#             Min = arr[i]
#             result = i
#     if Min == arr[0]:
#         return "0 Rotation ocurred "
#     else:
#         return "NO of rotation : {}".format(result)
# print(rotationCount([15,18,2,3,6,12],6))

'''  EFFICIENT SOLUTION COMPLEXITY O(logN)  Using Binary Search '''
print("************************************ USING BINARY SEARCH *********************************************************")
'''NOTE: as we know [15,18,2,3,6,12] min of array having index is equak to number of rotation  '''
''' Our Aim is to find whether min element using Binnary search '''
''' 1. check whether mid element is less than previous as well as next element if it is then its min element if not step 2'''
''' 2. if mid is not min then search in that part which is not sorted part    '''

def rotationCount(arr,n):
    start = 0
    end = n-1

    while(start<=end):
        mid = start + (end-start)//2
        prev = (mid + n - 1) % n  # in order to prvent from index out of bond if mid is 0th index  -1 will lead to error so avoid error we do this it will take the prev to last elemnent
        next = (mid +1) % n  # if mid is last element  if add 1 it will throw error index out of bound so we did this it will take next to first element
        if arr[mid] <= arr[prev] and arr[mid]<=arr[next]:
            return mid
        elif(arr[start]< arr[mid]):  # it means this side is sorted so we find min on other side
            start = mid+1
        elif(arr[mid]<arr[end]): # it means this side is sorted so we find on the other side
            end = mid -1


arr = [15,18,19,2,3,6,12]
n=len(arr)
print(rotationCount(arr,n))





