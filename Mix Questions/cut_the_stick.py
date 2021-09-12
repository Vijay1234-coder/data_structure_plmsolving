def cutTheSticks(arr):
    ls = []
    arr.sort()
    while len(arr) >= 1:
        ls.append(len(arr))
        minn = arr[0]
        arr=[x-minn for x in arr if x>minn]




    return ls


print(cutTheSticks([5,4,4,2,2,8]))    #2,2,4,4,5,8