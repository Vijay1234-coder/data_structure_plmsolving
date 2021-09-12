'''Count pair of with given sum k'''
'''if they ask suh kind of plm then we will check the the ocuurance of k-arr[i] elment 
because that frequncy  will give us how many distint pair will form '''







def solve(arr,k):
    n =len(arr)
    dic ={}
    for i in range(n):
        if k -arr[i] in dic:
            return True
        dic[arr[i]]=1
    return False










arr = [3,2,8,15,-8]
sum=17
res = solve(arr,sum)
print(res)