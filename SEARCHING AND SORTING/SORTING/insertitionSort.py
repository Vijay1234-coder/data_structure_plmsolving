def insertitionSort(arr,n):
    for index in range(1,n):
        current_element = arr[index]
        pos = index
        while current_element < arr[pos-1] and pos>0:
            arr[pos] = arr[pos-1]
            pos = pos -1
        arr[pos]  = current_element









arr = [7,2,4,1,5,3]  # [2,4,7,1,5,3]
n = len(arr)
insertitionSort(arr,n)
print(arr)