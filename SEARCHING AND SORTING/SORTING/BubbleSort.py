def bubbleSort(arr,n):
    for j in range(n-1):

    #     for i in range(n-1):
    #         if arr[i]>arr[i+1]:
    #             arr[i],arr[i+1]= arr[i+1],arr[i]  # swap smalest ele with largest
        # we can do some optimization like if each itration resulto sort max element at end so no need to run each loop n-1 time s
        for i in range(n-(j+1)):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1],arr[i]









arr = [30,4,2,5,6,1,7]
n = len(arr)
bubbleSort(arr,n)
print(arr)