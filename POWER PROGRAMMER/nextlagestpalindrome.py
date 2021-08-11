'''IMPORTANT'''
'''Below Not a Good Aproach Beacauze it takes '''
# def reverse(n):
#     rev = 0
#     while n > 0 :
#
#         rev =  rev*10 + n%10
#         n =  n//10
#     return rev
#
#
#
# def palindrome(n):
#     ori = reverse(n)
#     if ori == n:  # i have checked here if origional number is pallindrome then increase its value
#         n+=1
#
#     x = 0
#     while(x==0):
#         rev = reverse(n)
#         if rev==n:
#             x =1
#
#
#         n+=1
#     return rev
#
# print(palindrome(0))
# #
# # lis=[1,2,3,4,5]
# # number = 0
# # for i in lis:
# #     number = number*10+i
# # print(number)

'''Best aproach Below'''

# def inc(left):
#     leftlis = list(left)
#     lastindex =len(leftlis)-1
#     while leftlis[lastindex]=="9":
#         leftlis[lastindex]="0"
#         lastindex-=1
#     leftlis[lastindex]=str(int(leftlis[lastindex])+1)
#     left = "".join(leftlis)
#     return left









def all_nine(num):
    if num == len(num)*"9":
        return True

def otherPosi(num,n):
    mid = n // 2
    if n % 2 == 0:
        i = mid - 1
        j = mid
    else:
        i = mid - 1
        j = mid + 1
    while (i > 0 and num[i] == num[j]):
        i -= 1
        j += 1

    if int(num[i]) > int(num[j]):
        if n % 2 == 0:
            left = num[:mid]
            num = left + left[::-1]
            return num
        else:
            left = num[:mid]
            num = left + num[mid] + left[::-1]
            return num
    else:  # int(num[i]) <= int(num[j])
        if n % 2 == 0:

            num = num = num[:mid - 1] + str(int(num[mid - 1]) + 1) + num[mid + 1:]
            left = num[:mid]
            num = left + left[::-1]
            return num
        else:
            if num[mid] != "9":

                left = num[:mid]
                num = left + str(int(num[mid]) + 1) + left[::-1]
                return num
            else:
                carry = 1
                num = num[:mid - 1] + str(int(num[mid - 1]) + 1) + num[mid + 1:]
                # num = num.replace(num[mid-1],str(int(num[mid-1])+carry))
                left = num[:mid]
                num = left + "0" + left[::-1]
                return num


def solve(num,n):
    if all_nine(num)==True:
        print("1"+(len(num)-1)*"0"+"1")

        return
    elif n==1 and num[n-1]!="9":
        num = str(int(num[n-1])+1)
        print(num)


    else:
        otherPosi(num,n)


















num = "827215382284471224462941655268"
n = len(num)
print(num)
solve(num,n)



