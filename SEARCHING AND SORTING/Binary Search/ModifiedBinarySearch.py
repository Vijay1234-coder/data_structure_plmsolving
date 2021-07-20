'''Search in an almost sorted array'''
'''
Given an array which is sorted, but after sorting some elements are moved to either of the adjacent positions, i.e.,
 arr[i] may be present at arr[i+1] or arr[i-1]. Write an efficient function to search an element in this array. 
 Basically the element arr[i] can only be swapped with either arr[i+1] or arr[i-1].

For example consider the array {2, 3, 10, 4, 40}, 4 is moved to next position and 10 is moved to previous position.

Example :

Input: arr[] =  {10, 3, 40, 20, 50, 80, 70}, key = 40
Output: 2 
Output is index of 40 in given array

Input: arr[] =  {10, 3, 40, 20, 50, 80, 70}, key = 90
Output: -1
-1  is returned to indicate element is not present '''


def modifiedBinarySearch(arr,target):
    n = len(arr)
    start = 0
    end = n-1
    found = False
    while(start<=end and found == False):
        mid =start+(end-start)//2
        if target==arr[mid]:
            found =True
            return mid
        if(mid-1>=start and  target == arr[mid-1]):
            found = True
            return mid-1
        if(mid+1 <= end and target == arr[mid+1]):
            found = True
            return mid+1
        elif(target>arr[mid]):
            start = mid+2
        else:
            end =mid-2
    return found



arr = [10, 3, 40, 20, 50, 80, 70]
target = 3
print(modifiedBinarySearch(arr,target))