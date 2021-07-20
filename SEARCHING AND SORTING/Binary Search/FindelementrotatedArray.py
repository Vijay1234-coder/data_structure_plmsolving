''' Find an element in rotated sorted array    we have origional  sorted array and we have rotated it '''
''' arr: [15,16,18,2,3,4,5,6]
    target: 16
    o/p: 1    '''

def rotatedArray(arr,target):
    n = len(arr)
    start = 0
    end = n-1
    while(start<=end):
        mid = start + (end-start)//2
        prev = (mid+n-1) % n
        next = (mid+1) % n
        if arr[mid]<=arr[prev] and arr[mid]<=arr[next]:

            index = mid    # mid is index of min element in rotated sorted array  because after searching it will obtained
            result1= leftSortedArray(arr,index,target) # searching in leftsorted array (input array is sepatrated by min element)
            result2= rightSortedArray(arr,index,target)
            if result1==None and result2==None: # if both return -1 then not present
                return "Target Not present in Array"
            elif(result1==None):  # if not found in leftside it means it will obtain from right side
                return result2
            else:   # if not found in right side its means target on left side
                return result1

        elif(arr[start]<arr[mid]):
            start = mid+1
        elif(arr[mid]<arr[end]):
            end = mid - 1
def leftSortedArray(arr,index,target):
    start=0
    end = index -1

    while(start<=end):
        mid = (start+end)//2
        if arr[mid]==target:
            return mid
        elif(target > arr[mid]):
            start = mid+1
        else:
            end = mid-1


def rightSortedArray(arr,index,target):
    start = index
    end = len(arr)-1
    while (start <= end):
        mid = (start + end) // 2
        if arr[mid] == target:
            return mid
        elif (target > arr[mid]):
            start = mid + 1
        else:
            end = mid - 1


print(rotatedArray([15,16,18,2,3,4,5,6],18))