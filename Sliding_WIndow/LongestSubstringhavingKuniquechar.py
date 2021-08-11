def solve(str,k,n):
    maxlen =0
    for i in range(n):
        dict ={}

        for j in range(i,n):
            if str[j] not in dict:
                dict[str[j]]=1
            else:
                dict[str[j]] += 1
            if k==len(dict):
                maxlen = max(maxlen, j - i + 1)

    return maxlen


def solve2(str,k,n):
    i = 0
    j =0
    dict ={}

    maxlen =0
    while j< n:
        if str[j] not in dict:
            dict[str[j]]=1
        else:
            dict[str[j]]+=1


        if len(dict) < k:
            j+=1
        elif len(dict)==k:
            maxlen = max(maxlen,j-i+1)

            j+=1
        elif len(dict)>k:
            while len(dict)>k:
                dict[str[i]]-=1
                if dict[str[i]]==0:
                    dict.pop(str[i])
                i+=1
            j+=1
    return maxlen




str ="aabacbebebe"
k = 3

n =len(str)
print(solve(str,k,n))
print("Solution below is in O(N)")
print(solve2(str,k,n))