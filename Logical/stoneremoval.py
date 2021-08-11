import heapq


#https://leetcode.com/contest/weekly-contest-253/problems/remove-stones-to-minimize-the-total/

# class Solution:
#     def minStoneSum(self, piles: List[int], k: int) -> int:
#         while k > 0:
#             piles.sort(reverse=True)
#             temp = piles[0] - piles[0] // 2
#             for i in range(0, len(piles)):
#                 if k == 0:
#                     break
#                 if temp > piles[i]:
#                     break
#                 if piles[i] >= temp:
#                     piles[i] = piles[i] - piles[i] // 2
#                     k -= 1
#         return sum(piles)
k = 2
arr= [5]
heap =[]
for i in range(len(arr)):

    heapq.heappush(heap,-arr[i])
while k>0:
    x =- heapq.heappop(heap)
    x =x-x//2
    heapq.heappush(heap,-x)
    k-=1
print(heap)
