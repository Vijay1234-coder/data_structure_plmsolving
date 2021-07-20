''' Find the index of first 1 in an infinite sorted array of 0s and 1s '''

''' Given an infinite sorted array consisting 0s and 1s. The problem is to find the index of first ‘1’ in that array. 
As the array is infinite, therefore it is guaranteed that number ‘1’ will be present in the array.

Examples:

Input : arr[] = {0, 0, 1, 1, 1, 1} 
Output : 2

Input : arr[] = {1, 1, 1, 1, 1, 1}
Output : 0 '''

# This question is mix of infinite array + first occurance

def index(arr,start,end,target):
    result =-1
    while(start<=end):
        mid =start+(end-start)//2
        if arr[mid] == target: # if mid is target it means it can be our and so store it in result but
            result = mid  # may be it must first ocurrance will be left side of mid it must be if mid is not fisrtocurrance
            end = mid-1
        elif(arr[mid]<target): # binary search condition
            start =mid+1
        elif(arr[mid]>target): # binary search condition
            end =mid-1
    return result






arr = [0, 0, 0, 1, 1, 1]
target=1
start = 0
end = 1
while(target>arr[end]):  # we have write the logic for infinte array modifies binary search for finding tha start and end
    start =end
    end = 2 * end
print(index(arr,start,end,target)) # we got the start and end index in which target lies so we can simply apply Bsearch

