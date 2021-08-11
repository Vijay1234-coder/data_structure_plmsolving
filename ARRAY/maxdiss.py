import sys

n =int(input())
arr = list(map(int,input().split()))
ans =0
#
# for i in range(n):
#     Max = -sys.maxsize
#     Min = sys.maxsize
#     for j in range(i,n):
#         Max = max(Max,arr[j])
#         Min = min(Min,arr[j])
#         cur_ans = Max-Min
#         ans +=cur_ans
# print(ans)

# 4
# 1 3 2 4

i =0
j =0
while i<n:
    Max =max(Max,arr[j])
    Min =min(Min,arr[j])
    cur_ans =Max-Min
    ans+=cur_ans
