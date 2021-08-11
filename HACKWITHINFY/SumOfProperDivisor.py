'''Write a program to determine whether a number N is equal to the sum of its
proper positive divisors (excluding the number itself)  since here number is excluded so base case is 1 for 1 NO will be printed
you have to solve it in O(n) complexity'''

'''6: 1+2+3'''
'''N=36
   1 x 36
   2 x 18
   3 x 12
   4 x 9
   6 X 6 
   after this it will repeat  eg:
   9 x 4
  12 x 3
  18 X 2
  36 X 1
           '''


# from math import sqrt
#
# def SumPropDiv(n):
#     l=int(sqrt(n))
#     if n==1:
#         return 'NO'
#     set = {1}
#     for i in range(2,l+1):
#         if n%i==0:
#             set.add(i)
#             set.add(n//i)
#     if n==sum(set):
#         return 'YES'
#     else:
#         return 'NO'





#
# t=int(input("Enter number of test cases"))
# for i in range(t):
#     print(SumPropDiv(int(input("enter number"))))


from math import sqrt
def pp(n):
    root  = int(sqrt(n))
    set = {1}
    print(len(set))


    if n==1:   # edge case is 1 because we have to eliminate number itself
        return "NO"
    for div in range(2,root+1):
        if n % div ==0:
            set.add(div)
            set.add(n//div)
    s = sum(set)
    if s ==n:
        return "YES"
    else:
        return "NO"



print(pp(1))