# a = "10"
# b= "11"
# a =list(a)
# b= list(b)
# val1,val2 = 0 ,0
# for i in range(len(a)):
#     d = a.pop()
#     if d=='1':
#         val1+=2**i
# for i in range(len(b)):
#     d = b.pop()
#     if d=='1':
#         val2+=2**i
# print(val1,val2)
#
#
#
# res = val1^val2
# res_binary = bin(res).replace('0b',"0")
# print(res_binary)
# print(res)
# l = len(res_binary)
#

import sys
sts = set()
stq = set()
global Max

Max = - sys.maxsize
def helper(s,q):
    if (s not in sts and q not in stq and len(s)==0 and len(q)==0):
        return
    if len(s)==len(q):
        sts.add(s)
        stq.add(q)

        a = int(s)
        b = int(q)

        xor = a^b
        xxor = ""
        i =0
        while(i<len(s)):
            if s[i] == q[i]:
                xxor+="0"
            else:
                xxor+="1"
            i+=1
        length = len(xxor)
        poww = 2**xor
        res = length//poww
        Max = max(Max,res)

    helper(s[1:],q[1:])
    helper(s[0:len(s)-1],q[0:len(s)-1])
    helper(s[0:len(s)-1],q[1:])
    helper(s[1:],q[0:len(s)-1])
    return Max



def MaxProfit(M,S,Q):

    return helper(S,Q)





print(MaxProfit(5,"11001","10101"))