def MaxLenArr(arr,k):
    l=[]
    sum1=0
    i=-1
    Max=0
    dict1={sum1:i}       # Here i is index of current element and Sum is Corresponding Sum till that element
    Max_arr_len=0
    for i in range(len(arr)):
        sum1+=arr[i]
        if sum1 == k:
            Max=max(Max,i+1)   # if first element is equal to to sum then length of sub array will be i+1  ie. 0+1=1
        if (sum1-k) in dict1:
            Max = max(Max, i-dict1.get(sum1-k))   #  i-dict1.get(sum1-k)  will give length of array having sum equal to k
            if Max == (i-dict1.get(sum1-k)):
                l.append(arr[dict1.get(sum1-k)+1:i+1])



        dict1[sum1]=i
    for lis in l:
        Max_arr_len=max(Max_arr_len,len(lis))
        if len(lis)==Max_arr_len:
            Max_array=lis
    return Max_array








print(MaxLenArr([3,9,-2,4,1,-7,2,6,-5,8,-3,-7,6,2,1],3))