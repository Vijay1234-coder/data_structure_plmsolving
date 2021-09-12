#https://www.geeksforgeeks.org/minimum-length-subarray-sum-greater-given-value/
'''but `below code is  o(n^2) which is not good'''
def solve(arr,k):
    n =len(arr)

    minlen = n+1
    ans =[]
    for i in range(n):
        curr = arr[i]
        if curr>k:
            return 1
        for j in range(i+1,n):
            curr+=arr[j]
            # below code is for minlen havin=g sum is greater than k
            if curr>k:
                minlen =min(minlen,j-i+1)



    print("minimum len having sum gteater than k: ",minlen)


    return





# below is O(n^2) solution


def slidingWindow(arr,k):
    n=len(arr)
    i = 0
    j = 0
    cur = 0
    minlen = n+1
    while j<n:
        cur += arr[j]

        if cur<=k:
            j+=1
        elif cur>k:
            minlen = min(minlen, j-i+1)
            while cur>k:
                cur-=arr[i]
                i+=1
                if cur>k:
                    minlen = min(minlen, j-i+1)
            j += 1
    print("Mini ler using sliding window algorith",minlen)
    return












arr = [1, 4, 45, 6, 0, 19]
k =51
solve(arr,k)
slidingWindow(arr,k)




