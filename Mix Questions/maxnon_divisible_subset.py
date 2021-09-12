def maxnonDiv(s,k):
    rem_dic={}
    Max=0
    count=0

    for i in range(k):
        rem_dic[i]=0



    for num in s:
        rem=num % k
        if rem in rem_dic:
            rem_dic[rem] += 1
        else:
            rem_dic[rem] = 1
    print(rem_dic)


    for num in rem_dic:
        if num==0 and rem_dic[num]>0:
            count+=1
        if k%2==0:
            if num==k//2 and rem_dic[num]>0:
                count+=1
    if k//2==1:
        Max = max(rem_dic[1], rem_dic[k -1])
        count += Max
    else:
        for i in range(1, k//2+1):
            Max= max(rem_dic[i],rem_dic[k-i])
            count += Max


    return count









k=int(input("enter number"))
print(maxnonDiv([278,576,496,727,410,124,338,149,209,702,282,718,771,575,436],k))