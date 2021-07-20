def selectionSort(arr,n):
    for i in range(n):
        minVal = min(arr[i:])
        index_min = arr.index(minVal)
        arr[i],arr[index_min] = arr[index_min],arr[i]








arr= [10,2,40,50,3,4,7]
n  = len(arr)
selectionSort(arr,n)
print(arr)