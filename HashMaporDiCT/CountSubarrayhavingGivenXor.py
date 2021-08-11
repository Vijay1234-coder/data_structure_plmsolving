arr =[4,2,2,6,4]
k = 6
dict1 ={}
count = 0
xorr = 0
for num in arr:
    xorr = xorr^num
    if xorr==k:
        count+=1
    if xorr^k in dict1:
        count+=dict1[xorr^k]
    else:
        if xorr not in dict1:
            dict1[xorr]=1
        else:
            dict1[xorr]+=1



print(count)




