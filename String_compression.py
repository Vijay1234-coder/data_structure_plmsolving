''' If Input=AAAAaaaBBB output=A4a3B3      if input=AAB   op=A2B1'''


#
# def compress(s):
#     count={}
#     empty_lis=[]
#     for i in range(len(s)):
#         if s[i] in count:
#             count[s[i]]+=1
#         else:
#             count[s[i]]=1
#
#     for char in count:
#         empty_lis.append(char)
#         empty_lis.append(str(count[char]))
#     return "".join(empty_lis)
#
# print(compress(input("enter string")))     <----- this solution is not efficient becauuze If ABBAA o/p =A1B2A2 but a/c prev o/p : A3B2

def compress(s):
    l=len(s)
    r=""
    if l==0:
        return ""
    if l==1:
        return s+"1"
    last = s[0]
    i=1
    count=1
    while i<l:
        if s[i]==s[i-1]:
            count+=1
        else:
            r = r+s[i-1]+str(count)
            count=1
        i=i+1
    r=r+s[i-1]+str(count)
    return r

print(compress("AAAABBBBbbbaaaAA"))




