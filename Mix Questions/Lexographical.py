"""Important"""
'''Next largest lexographical string
eg: ab o/p =ba
eg eodigf  o/p eofdig'''

def Solve(w):
    n =len(w)
    word = list(w)
    endindex = 0
    c=0
    for endindex in range(n-1,0,-1):
        if word[endindex] > word[endindex-1]:
            c+=1
            break
    if c==0: # pura loop chala and ek bhi aisa element nahi mila jo agge waale se chhota ho
        return "no answer"
    else:
        smallestchar =  word[endindex-1]
        nextsmaller = endindex
        startindex   =  endindex+1
        for index in range(startindex,n):
            if word[index] > word[endindex-1] and word[index]<word[endindex]:
                nextsmaller = index
        word[endindex-1],word[nextsmaller]=word[nextsmaller],word[endindex-1]
        temp = word[endindex:]
        temp.sort()
        res = word[:endindex]+temp
        return "".join(res)



print(Solve("eodigf"))