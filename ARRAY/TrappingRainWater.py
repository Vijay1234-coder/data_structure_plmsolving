#https://practice.geeksforgeeks.org/problems/trapping-rain-water-1587115621/1#


'''brute Force'''
'''res 0
   for loop (1,n-1)
      lmax =arr[i]
      for j in rnage(0,i)
           lmax =max(lmax,arr[j])
      rmax =arr[i]
      for j in range(i+1,n):
         rmax = rmax(rmax,arr[j])
     for i in range(1, n - 1):
            res += min(lmax[i], rmax[i]) - arr[i]
    return res
      '''

'''the optimal solution is prefix max count and suffix righmax count'''
class Solution:
    def trappingWater(self, arr, n):
        lmax = [1] * n
        rmax = [1] * n
        lmax[0] = arr[0]
        rmax[n - 1] = arr[n - 1]

        res = 0

        for i in range(1, n):
            lmax[i] = max(lmax[i - 1], arr[i])
        for i in range(n - 2, -1, -1):
            rmax[i] = max(rmax[i + 1], arr[i])
        for i in range(1, n - 1):
            res += min(lmax[i], rmax[i]) - arr[i]
        return res
