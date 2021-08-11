'''Given an array and a positive integer k, find the first negative integer for each window(contiguous subarray) of size k. If a window does not contain a negative integer, then print 0 for that window.

Examples:

Input : arr[] = {-8, 2, 3, -6, 10}, k = 2
Output : -8 0 -6 -6
First negative integer for each window of size k
{-8, 2} = -8
{2, 3} = 0 (does not contain a negative integer)
{3, -6} = -6
{-6, 10} = -6

Input : arr[] = {12, -1, -7, 8, -15, 30, 16, 28} , k = 3
Output : -1 -1 -7 -15 -15 0'''
#this is O(N**2)solution
# def solve(arr,k,n):
#     lis =[]
#     result=[]
#     for i in range(n-k+1):
#         for j in range(i,i+k):
#             if arr[j]<0:
#                 lis.append(arr[j])
#
#         if len(lis)==0:
#             result.append(0)
#         else:
#             result.append(lis[0])
#             lis=[]
#     return result
def solve(arr,k,n):
    lis =[]
    result =[]
    i =0
    j =0
    while j<n:
        if arr[j]<0:
            lis.append(arr[j])
        if j-i+1<k:
            j+=1
        elif j-i+1==k:
            if len(lis)==0:
                result.append(0)
            else:
                result.append(lis[0])
                if arr[i]==lis[0]:
                    lis.pop(0)
            i+=1
            j+=1
    return result












arr =[12, -1, -7, 8, -15, 30, 16, 28]
k =3
n =len(arr)
print(solve(arr,k,n))
