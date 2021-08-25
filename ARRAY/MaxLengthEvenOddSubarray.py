def maxLen(arr,n):
    count =1
    Max =1
    for i in range(1,n):
        if arr[i]%2==0 and arr[i-1]%2!=0:
            count+=1
        elif arr[i]%2!=0 and arr[i-1]%2==0:
            count+=1
        else:
            count =1
        Max = max(Max,count)
    return Max

arr1 =[7,10,13,15,10,17,20,21]






arr = [7,10,13,14]
n =len(arr)
print(maxLen(arr,n))