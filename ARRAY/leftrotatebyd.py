#Left Rotate an Array d times


def reverse(arr,low,high):
    while low<high:
        arr[low],arr[high] = arr[high],arr[low]
        low+=1
        high-=1

def leftRotate(arr,n,d):
    reverse(arr,0,d-1)
    reverse(arr,d,n-1)
    reverse(arr,0,n-1)
    print(arr)







arr = [1, 2, 3, 4, 5]
d = 2
n =len(arr)
leftRotate(arr,n,d)


# O(DN) approch......................................


def rotate(arr,n,d):
    for i in range(d):

        first=arr[0]
        for i in range(1,n):
            arr[i-1] = arr[i]
        arr[n-1] = first
    print(arr)









arr = [1, 2, 3, 4, 5]
d = 2
n =len(arr)
rotate(arr,n,d)