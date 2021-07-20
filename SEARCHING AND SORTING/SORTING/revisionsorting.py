

def selection(arr,n):
    for i in range(n):
        minVal = min(arr[i:])
        indexx = arr.index(minVal)
        arr[i],arr[indexx] =arr[indexx],arr[i]
arr = [7,2,4,1,5,3]
n =len(arr)
selection(arr,n)
print(arr)