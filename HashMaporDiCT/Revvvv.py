def subarray(arr,k):
    count =0
    sum1 =0
    dict1 ={0:1}
    for num in arr:
        sum1 +=num
        rem = sum1%k
        if rem<0:
            rem+=k
        if rem not in dict1:
            dict1[rem]=1
        else:
            count+=dict1[rem]
            dict1[rem]+=1
    return count







arr = [2,-6,3,1,2,8,2,1]
k =7
print(subarray(arr,k))