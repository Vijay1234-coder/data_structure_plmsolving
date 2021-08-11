def partioning(arr,start,end):
    pivot = arr[end]
    pindex = start  # partion index
    for i in range(start,end):
        if arr[i] <= pivot:
            arr[i],arr[pindex] = arr[pindex],arr[i]
            pindex+=1

    arr[end], arr[pindex] = arr[pindex],arr[end]
    return pindex





def quickSort(arr,start,end):
    if start< end:
        pindex = partioning(arr,start,end)
        quickSort(arr,start,pindex-1)
        quickSort(arr,pindex+1,end)



arr = [ 5, 7, 8, 9, 1, 10 ]
n = len(arr)

quickSort(arr,0,n-1)
print(arr)