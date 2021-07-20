'''Given a sorted array and a value x, the floor of x : is the largest element in array smaller than or equal to x. Write efficient functions to find floor of x.
Examples:


Input : arr[] = {1, 2, 8, 10, 10, 12, 19}, x = 5
Output : 2
2 is the largest element in
arr[] smaller than 5.

Input : arr[] = {1, 2, 8, 10, 10, 12, 19}, x = 20
Output : 19
19 is the largest element in
arr[] smaller than 20.

Input : arr[] = {1, 2, 8, 10, 10, 12, 19}, x = 0
Output : -1
Since floor doesn't exist,
output is -1.'''


def floorVal(arr,x):
    result = -1
    n = len(arr)
    start = 0
    end = n-1
    while(start<=end):
        mid = start + (end-start)//2
        if arr[mid]== x:
            return arr[mid]
        elif(arr[mid]>x):

            end = mid-1

        elif(arr[mid]<x):
            result = arr[mid]
            start = mid+1
    return result


print(floorVal([1, 2, 8, 10, 10, 12, 19],5))