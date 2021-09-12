



def selectionSort(arr):
    n= len(arr)
    for i in range(n):
        min  =i
        for j in range(i+1,n):
            if arr[i]>arr[j]:
                arr[i],arr[j] = arr[j],arr[i]
    return arr




arr =[3,3,5,4,2,1,5]
res = selectionSort(arr)
print(res)