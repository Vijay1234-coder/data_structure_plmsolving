# def armStrong_number(n):
#     l=[]
#     s=str(n)
#     sum1=0
#     for strr in s:
#         intg=int(strr)
#         sum1+=intg**len(s)
#  #complexity O(N)
#
#     if sum1==n:
#         print("number is ARMSTRONG")
#     else:
#         print("not ARMSTRONG")
#
#
# armStrong_number(int(input("enter your number")))
#
#
#
#
# Python program to check if the number is an Armstrong number or not

# take input from the user
# num = int(input("Enter a number: "))
#
# # initialize sum
# sum = 0
#
# # find the sum of the cube of each digit
# temp = num
# while temp > 0:
#    digit = temp % 10
#    sum += digit ** 3
#    temp //= 10
#
# # display the result
# if num == sum:
#    print(num,"is an Armstrong number")
# else:
#    print(num,"is not an Armstrong number")

