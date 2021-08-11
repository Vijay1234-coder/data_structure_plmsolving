"""we have a string abc  find permutaion which doesnt contain ab as substr"""


# Below Solution Will Take n!*n complexity we can optimize using BACKTRACKING
# def permute(str,l,r):
#     if l == r:
#         res = "".join(str)
#         if "ab" not in res:
#             print("".join(str))
#
#
#
#
#     else:
#         for i in range(l,r+1):
#             str[l],str[i] = str[i],str[l]
#             permute(str,l+1,r)
#             str[l],str[i] = str[i],str[l]
#

# BELOW IS OPTIMIZE SOLUTION

def issafe(str,l,i,r):
    if (l!=0 and str[l-1]=="a" and str[i]=="b"):
        return False
    if(r == l+1 and str[i]=="a" and str[l]=="b"):
        return False
    return True

def permute(str,l,r):
    if l == r:
        res = "".join(str)
        if "ab" not in res:
            print("".join(str))




    else:

        for i in range(l,r+1):
            if issafe(str,l,i,r)==True:
                str[l],str[i] = str[i],str[l]
                permute(str,l+1,r)
                str[l],str[i] = str[i],str[l]


string = "abc"
l = 0
r = len(string)-1
str = list(string)

permute(str,l,r)