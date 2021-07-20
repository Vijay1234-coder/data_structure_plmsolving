''' '''
''' You have to travel to different villages to make some profit.
In each village, you gain some profit. But the catch is, from a particular village i,
you can only move to a village j if and only if  and the profit gain from village j is
 a multiple of the profit gain from village i.

You have to tell the maximum profit you can gain while traveling.

Input format:
The first line contains a single integer N denoting the total number of villages.
The second line contains N space-separated integers, each denoting the profit gain  from village i.
Output formate
Print the maximum profit you can gain.

Constraints:
1<=N<=1000
0<=pi<=100000

Sample Input
6
1 2 3 4 9 8       
Sample Output
15'''

n=int(input())     #1 2 3 4 5 3,4 23
arr = list(map(int, input().split()))
dp=[0]*n
for i in range(n):
    dp[i]=arr[i]
for i in range(1,n):
    for j in range(0,i):
        if arr[i]%arr[j]==0:
            dp[i] = max(dp[i],dp[j]+arr[i])
print(max(dp))