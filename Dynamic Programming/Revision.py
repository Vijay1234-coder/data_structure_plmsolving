# arr =[1,2,-1,3,4,10,10,-10,-1]
#
# curr_sum = arr[0]
# Best_sum = arr[0]
#
# for i in range(1,len(arr)):
#     if curr_sum > 0:
#         curr_sum+=arr[i]
#     else:
#         curr_sum = arr[i]
#
#     if curr_sum > Best_sum:
#         Best_sum =curr_sum
# print(Best_sum)
# # Max =-10000
# # sum1=0
# # for i in range(len(arr)):
# #     sum1 = 0
# #     for j in range(i,len(arr)):
# #         sum1+=arr[j]
# #         Max =max(Max,sum1)
# # print(Max)
#
#
#
#
arr =[[0,0],[0,0]]

for i in range(len(arr)):
    idx =arr.index([0,0])
    print(idx)
