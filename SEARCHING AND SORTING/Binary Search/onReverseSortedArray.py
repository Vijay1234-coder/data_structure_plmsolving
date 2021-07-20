'''Let's suppose that we have an array sorted in descending order and we want to find index of an element e within this array. Binary search in every step picks the middle element (m) of the array and compares it to e. If these elements are equal, than it returns the index of m. If e is greater than m, than e must be located in the left subarray. On the contrary, if m greater than e, e must be located in the right subarray. At this moment binary search repeats the step on the respective subrarray.

Because the algoritm splits in every step the array in half (and one half of the array is never processed) the input element must be located (or determined missing) in at most \\log_{2}{n} steps.'''




def binarySearch(arr,target):
    start =0
    end =len(arr)-1
    found = False
    while(start<=end) and found == False:
        mid = start + (end-start)//2
        if arr[mid]== target:
            found = True
            print("found at index : {}".format(mid))
        elif(target > arr[mid]):
            end = mid -1
        else:
            start = mid +1
    return found



arr = [10,9,8,7,6,5,4,3,2,1,0]
print(binarySearch(arr,0))