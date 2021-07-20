'''Given a sorted array and a value x, the Ceil of x : is the smallest element in array greater than or equal to x.
Write efficient functions to find Ceil of x.
Examples:


Input : arr[] = {1, 2, 8, 10, 10, 12, 19}, x = 5
Output : 8
8 is the smallest element in
arr[] greater than 5.



Input : arr[] = {1, 2, 8, 10, 10, 12, 19}, x = 0
Output : -1
Since ceil doesn't exist,
output is -1.'''


def ceilValue(arr,x):
    result = -1
    start = 0
    end = len(arr)-1
    while(start<=end):
        mid = start+(end-start)//2

        if arr[mid]== x:
            return arr[mid]
        elif(arr[mid]>x):
            result = arr[mid]
            end = mid-1
        elif(arr[mid]<x):
            start =mid + 1
    return result






arr= [1, 2, 8, 10, 10, 12, 19]
x = 19
print(ceilValue(arr,x))