# insertion sort
def insertionSort(arr,n):
    for index in range(1,n):
        curr = arr[index]
        pos = index
        while pos > 0 and arr[pos-1]>curr:
            arr[pos]= arr[pos-1]
            pos-=1
        arr[pos] = curr










arr = [7,4,52,3,20,8]
n = len(arr)
insertionSort(arr,n)
print(arr)