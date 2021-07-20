
'''ddd'''
'''     HACKER RANK QUESTION  seems like equal sum patision but NOt         Nikita just came up with a new array game. The rules are as follows:

Initially, Nikita has an array of integers.

In each move, Nikita must partition the array into  non-empty contiguous parts such that the sum of the elements in the left partition is equal to the sum of the elements in the right partition. If Nikita can make such a move, she gets  point; otherwise, the game ends.

After each successful move, Nikita discards either the left partition or the right partition and continues playing by using the remaining partition as array .

Nikita loves this game and wants your help getting the best score possible. Given , can you find and print the maximum number of points she can score?

For example, Nikita starts with the array . She first splits it into  and , then discards . . Discard  leaving . This cannot be further split, so Nikita scored .

Function Description

Complete the arraySplitting function in the editor below. It should return an integer that reperesents the number of times Nikita can split the array.

arraySplitting has the following parameter(s):

arr: an array of integers'''


'''array		a1	a2
[4,1,0,1,1,0,1]	[4]	[1,0,1,1,0,1]      [1,5,5,11]
[1,0,1,1,0,1]	[1,0,1]	[1,0,1]
[1,0,1]		[1,0]	[1]'''
#

def bb(a):
    a.sort()
    if (len(a) < 2):
        return 0
    s = sum(a)
    x = 0
    for i in range(len(a) - 1):
        x += a[i]
        if x == s / 2:
            return 1 + max(bb(a[:i + 1]), bb(a[i + 1:]))
    return 0




for _ in range(int(input("enter number of test cases"))):
    n = int(input("enter length of array "))
    a = list(map(int, input("enter elements in single line with space").split()))
    if sum(a) == 0:
        print(n - 1)
    else:
        print(bb(a))


