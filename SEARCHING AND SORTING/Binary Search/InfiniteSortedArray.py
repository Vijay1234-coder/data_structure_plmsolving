''' Find Position of an Array in infinite Sorted Array '''
'''Find position of an element in a sorted array of infinite numbers
Difficulty Level : Medium
Last Updated : 07 May, 2021
Suppose you have a sorted array of infinite numbers, how would you search an element in the array?
Source: Amazon Interview Experience. 
Since array is sorted, the first thing clicks into mind is binary search, but the problem here is that we don’t know size of array. 
If the array is infinite, that means we don’t have proper bounds to apply binary search. So in order to find position of key, first we find bounds and then apply binary search algorithm.
Let low be pointing to 1st element and high pointing to 2nd element of array, Now compare key with high index element, 
->if it is greater than high index element then copy high index in low index and double the high index. 
->if it is smaller, then apply binary search on high and low indices found. 
 arr = [3, 5, 7, 9, 10, 90, 100, 130, 140, 160, 170]
ans = findPos(arr,10) 
Element found at index 4'''



def binarySearch(arr,start,end,target):
    while start<=end:
        mid = start+(end-start)//2
        if arr[mid]==target:
            return "target found at: {}".format(mid)
        elif(arr[mid] > target):
            end = mid-1
        elif(target>arr[mid]):
            start = mid +1
    return "Target NOT PRESENT IN ARRAY PLEASE INPUT VALID TARGET"



arr = [3, 5, 7, 9, 10, 90, 100, 130, 140, 160, 170]   # suppose this is infinite array which is given in the question
target = 170


start = 0
end = 1


while(target > arr[end]):
    start = end
    end = end * 2


print(binarySearch(arr,start,end,target))

