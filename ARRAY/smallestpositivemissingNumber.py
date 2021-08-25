# https://www.geeksforgeeks.org/find-the-smallest-positive-number-missing-from-an-unsorted-array/


def shiftnegative(arr):
    n =len(arr)
    j =0
    for i in range(n):
        if arr[i]<0:
            arr[i],arr[j] = arr[j],arr[i]
            j+=1


    i=0
    for i in range(n):
        if arr[i]>0:
            break
    if i==n-1:
        return 1
    else:
        return arr[i:]


def smallestPositiveNum(arr):


    arr = shiftnegative(arr)


    for i in range(len(arr)):
        idx = abs(arr[i])-1
        if idx < len(arr)  and arr[idx]>0:
            arr[idx] = - arr[idx]
    for i in range(len(arr)):
        if arr[i]>0:
            return i+1
    return len(arr)+1












arr =[1, 1, 0, -1, -2]

print(smallestPositiveNum(arr))