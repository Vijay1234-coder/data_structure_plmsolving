''' split the array into 3 equl parts how many ways possible     '''



def splitCount(arr,n):
    count= 0
    tempSuffixCount = [0]*n
    total_sum = sum(arr)
    if total_sum%3 !=0:
        return "not Possible"
    partision_sum = total_sum//3
    prefix_Sum = [0] * n
    prefix_Sum[0] = arr[0]

    for i in range(1, n):
        prefix_Sum[i] = prefix_Sum[i - 1] + arr[i]



    suffix_sum =[0]*n

    suffix_sum[n-1] = arr[n-1]
    if suffix_sum[n-1] == partision_sum:
        tempSuffixCount[n-1] = 1

    for i in range(n-2,-1,-1):
        suffix_sum[i] = suffix_sum[i+1] + arr[i]
        if suffix_sum[i] == partision_sum:
            tempSuffixCount[i] = tempSuffixCount[i+1] + 1




    for i in range(0,n-1):
        if prefix_Sum[i] == partision_sum:
            count  +=  tempSuffixCount[i+2]
            return count


    return "Not Posssible"

arr = [ 1,2,3,0,3 ]  # [1 2] [3] [0 3],    [1 2] [3 0] [3]
n = len(arr)
print(splitCount(arr,n))