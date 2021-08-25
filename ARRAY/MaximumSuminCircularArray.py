''' Circular array is such type of array in which
last element's next is first elements and its subset is subsets of normal array + subsets of cirscular '''


def maxSum(arr,n):
    res =arr[0]
    for i in range(n):
        curSum = arr[i]
        cur_max =arr[i]
        for j in range(1,n):
            index =(i+j)%n
            curSum+=arr[index]
            cur_max =max(cur_max,curSum)
        res= max(res,cur_max)


    return res










arr =[5,-2,3,4]
n =len(arr)
print(maxSum(arr,n))
