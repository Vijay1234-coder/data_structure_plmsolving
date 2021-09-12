#https://www.geeksforgeeks.org/removing-string-that-is-an-anagram-of-an-earlier-string/


#op =["geeks",'code']

def solve(arr,n):
    mp={}
    for x in range(len(arr)):
        sum=0
        for i in arr[x]:
            sum+=ord(i)
        if sum not in mp:
            mp[sum]=1
        else:

            arr[x]=False
    res = [i for i in arr if i!=False]
    return res







arr= ["geeks", 'keegs', 'code', 'doce']



n= 4
print(solve(arr,n))

