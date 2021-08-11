from collections import Counter
def pickingNumber(a):
    arr=Counter(a)
    print(arr)

    maximun = 0

    for i in range(100):
        arr[1]
        maximun= max(maximun,arr[i]+arr[i+1])
    print(maximun)

pickingNumber([5,5,0])