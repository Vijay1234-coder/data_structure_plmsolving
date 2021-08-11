def mergeList(arr,L,R):
    nL = len(L)
    nR = len(R)
    i = 0
    j = 0
    k = 0

    while i< nL and j< nR:
        if L[i]<=R[j]:
            arr[k] = L[i]
            k+=1
            i+=1
        else:
            arr[k] = R[j]
            k+=1
            j+=1
    if i == nL:     # while loop false becz of Left array
        while j< nR: # then remaining left in Right store in arr at k th position
            arr[k] = R[j]
            j+=1
            k+=1
    if j == nR: # while loop false becz of Right array
        while i<nL: # then remaining left in Left array elements  store in arr at k th position
            arr[k]= L[i]
            i+=1
            k+=1











def mergeSort(arr):
    mid = len(arr)//2
    if len(arr)<2:
        return arr
    leftarr =arr[:mid]
    rightarr =arr[mid:]
    mergeSort(leftarr)
    mergeSort(rightarr)
    mergeList(arr,leftarr,rightarr)



arr = [12,11,13,5,6,7]
mergeSort(arr)
print(arr)