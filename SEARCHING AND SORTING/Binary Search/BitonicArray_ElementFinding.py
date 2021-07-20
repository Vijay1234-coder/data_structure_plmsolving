'''Find an element in Bitonic array
Difficulty Level : Medium
Last Updated : 22 Jan, 2021 '''
'''  Given a bitonic sequence of n distinct elements, write a program to find a given element x in
     the bitonic sequence in O(log n) time. A Bitonic Sequence is a sequence of numbers that is first 
     strictly increasing then after a point strictly decreasing.

Examples: 

Input :  arr[] =  {-3, 9, 18, 20, 17, 5, 1}
         key = 20
Output : Found at index 3

Input :  arr[] = {5, 6, 7, 8, 9, 10, 3, 2, 1};
         key = 30
Output : Not Found  '''

''' if you notice in bitonic array peak element is present and before at peak half of element of array left side is 
 sorted in accending order and right half elements are sorted into decending order we will apply BSearch both side  '''

''' 
'''

def findPeak(arr,target):
    n=len(arr)-1
    start = 0
    end = n-1
    while(start<=end):
        mid = start + (end - start) // 2
        if(arr[mid]>arr[mid-1] and arr[mid] > arr[mid+1]):
            peak = mid
            if target == arr[peak]:
                return peak
            else:
                result1 = leftArray(arr,0,peak-1,target)
                result2 = rightArray(arr,peak+1,n-1,target)
                if result1 is not None and result2 is None:
                    return  result1
                elif(result2 is not None and result1 is None):
                    return result2
                else:
                    return "Target is not Found"


        elif(arr[mid-1]>arr[mid]):
            end = mid-1
        else:
            start = mid+1

def leftArray(arr,start,end,target): # [1,3,8]  left Sub Array will be sorted in accending order applying Bsearh
    while start<=end:
        mid = start+(end-start)//2
        if arr[mid]==target:

            return mid
        elif(target>arr[mid]):
            start = mid+1
        else:
            end =mid-1


def rightArray(arr,start,end,target): # [4,2,0] right side SubArray will be sorted in deccending order mean greater element come first
    end = len(arr)-1
    while start <= end:
        mid = start + (end - start) // 2

        if arr[mid] == target:
            return mid

        elif(target > arr[mid]):
            end = mid-1
        else:
            start = mid +1


arr= [1,3,8,12,4,2,0]
target = 12

print(findPeak(arr,target))











