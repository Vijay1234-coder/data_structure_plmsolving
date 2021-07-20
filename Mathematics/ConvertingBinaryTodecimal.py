
'''IMPORTANT'''
'''101 ----  2^2 + 2^0     
[ 1,0,1 ]'''


a = list(input(" Enter Binary String "))
val =0
for i in range(len(a)):
    binary = a.pop()
    if binary=="1":
        val+=2**i
print(val)
























# a = list((input("enter binarry number")))
# val = 0
# for i in range(len(a)):
#     binary = a.pop()
#     if binary=='1':
#         val+=2**i
# print(val)


