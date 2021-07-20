'''Binary Search on unsorted Array problem  '''
'''A peak element is an element that is strictly greater than its neighbors.

Given an integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.

You may imagine that nums[-1] = nums[n] = -∞.

You must write an algorithm that runs in O(log n) time.

 

Example 1:

Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.
Example 2:

Input: nums = [1,2,1,3,5,6,4]
Output: 5
Explanation: Your function can return either index number 1 where the peak element is 2, or index number 5 where the peak element is 6.
 

Constraints:

1 <= nums.length <= 1000
-231 <= nums[i] <= 231 - 1
nums[i] != nums[i + 1] for all valid i.'''



def peak(arr):
    n=len(arr)
    start = 0
    end = n-1
    while(start<=end):
        mid = start+(end-start)//2
        if (mid>0 and mid<n-1):
            if(arr[mid]>arr[mid-1] and arr[mid]>arr[mid+1]):
                return mid
            elif(arr[mid-1]>arr[mid]):
                end = mid-1
            else:
                start = mid+1
        elif(mid==0):
            if(arr[0]>arr[1]):
                return 0
            else:
                return 1
        elif(mid==n-1):
            if(arr[n-1]>arr[n-2]):
                return n-1
            else:
                return n-2
print(peak([1,2,1,3,5,6,4]))