arr =    [1,1,2,3,3,3,4,4,4,7]

output = [1,2,1,1,2,3,1,2,3,1]   # this our expected output Here this is Indexing of blocks of same type
# i.e 1,1 is same block first 1 is at 1 positon second 1 is at 2nd position like that


n =len(arr)
op=[1]*n
for i in range(1,n):
    if arr[i]==arr[i-1]:
        op[i] = op[i-1]+1
print(op)













# n=len(arr)
# outpu1 =[0]*n
# outpu1[0]=1
# for i in range(1,n):
#     if arr[i] == arr[i-1]:
#         outpu1[i] =outpu1[i-1] + 1
#     else:
#         outpu1[i]= 1
# print(outpu1)










# n = len(arr)
#
# output1 = [0]*n
# output1[0]=1
#
#
#
# for i in range(1,n):
#     if arr[i-1]==arr[i]:
#         output1[i] = output1[i-1] + 1
#     else:
#         output1[i]=1
# print(output1)

