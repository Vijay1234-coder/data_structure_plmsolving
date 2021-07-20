def check(str1,str2):
    count ={}
    for char in str1:
        if char not in count:
            count[char]=1
        else:
            count[char]+=1
    for char in str2:
        if char in count:
            count[char]-=1
        else:
            count[char]=1
    for k in count:
        if count[k]!=0:
            return "str2 is NOT anagram"
    return "YES Str2 is an Anagram"


str1 ="vijay"
str2 ="jivya"

if len(str1)==len(str2):
    print(check(str1,str2))
else:
    print("str2 is not anagram")