'''Important'''


'''Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

 

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].'''

# below is brute Force approach of O(N2)
# def merge(A,B):
#     if A[0] > B[1] or B[0] > A[1]:
#         return False
#     B[0] =min(A[0],B[0])
#     B[1] =max(B[1],A[1])
#     return True
#
#
# def mergeinterval(intervals):
#     result =[]
#     bmerge =[False]*len(intervals)
#     for i in range(len(intervals)-1):
#         for j in range(i+1,len(intervals)):
#             if merge(intervals[i],intervals[j])==True:
#                 bmerge[i]=True   # that element is now merged
#
#
#
#     for i in range(len(intervals)):
#         if bmerge[i]==False:
#             result.append(intervals[i])
#     return result
#
# intervals = [[1,4], [5,8], [8,10], [12,15]]
# print(mergeinterval(intervals))




