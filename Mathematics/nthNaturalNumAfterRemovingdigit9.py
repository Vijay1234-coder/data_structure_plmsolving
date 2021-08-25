# n=20
# IntMax =10000000
# count =0
#
#
#
# def notNine(n):
#     while n>0:
#         rem =n%10
#         n =n//10
#         if rem==9:
#             return False
#     return True
#
#
#
# for i in range(1,IntMax):
#     if notNine(i)==True:
#         count+=1
#     if count==n:
#         print(i)
#         break



'''above Approach will take O(N^2) if N will Large then plm willl increase Time'''

'''best Approach is Basic we need to Chance That number into Base 9 and after that Base 9 number is ans
eg: n=10 we Convert it in to bAse 9 :   11 which our ans'''




n =20
ans=0
i=0
while n>0:
    rem = n%9
    n =n//9
    ans+= rem* (10**i)
    i+=1
print(ans)



