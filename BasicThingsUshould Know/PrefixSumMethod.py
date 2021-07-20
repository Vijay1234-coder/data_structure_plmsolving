''' Given an array arr[] of size n, its prefix sum array is another array prefixSum[]
    of same size such that the value of
    prefixSum[i] is arr[0] + arr[1] + arr[2] … arr[i]     '''

arr= [10,20,10,5,15]
# o/p: prefixSum = [10,30,40,45,60]

n  =len(arr)
prefix_Sum =[0]*n
prefix_Sum[0] = arr[0]  #[10,0,0,0,0]

for i in range(1,n):
    prefix_Sum[i] = prefix_Sum[i-1] +arr[i]
print(prefix_Sum)

'''Findind suffix sum'''
# arr = [1,2,4,1,2]  #    sufiix sum  == [10, 9, 7, 3, 2]
# index=[0,1,2,3,4]
#
# n = len(arr)
# suffix_sum = [0 for x in range(n)]
# suffix_sum[n-1] = arr[n-1]
#
# for i in range(n-2,-1,-1):
#     suffix_sum[i] = suffix_sum[i+1] + arr[i]
# print(suffix_sum)
#
