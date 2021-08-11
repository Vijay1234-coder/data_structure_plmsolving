def maxProfit(val,wt,w,n):
    pwratio = []  # pwration means profit//weight ratio
    for i in range(n):
        ratio = val[i]/wt[i]
        pwratio.append([ratio,i])   # here we are storing index of ratio bcz after sorting we should keep track of index from which it belongs

    pwratio.sort(reverse=True)
    s= 0
    ans = 0
    for i in range(len(pwratio)):
        if wt[pwratio[i][1]]<=w and w >0 :
            w = w-wt[pwratio[i][1]]
            ans = ans+val[pwratio[i][1]]
        else:
            if w>0:
                ans = ans+ pwratio[i][0]*w  #pi*w//wi==(pi/wi)*w(left)
                break
    return ans

















val = [60, 40, 100, 120]
wt = [10, 40, 20, 30]
n =len(wt)
w = 50
print(maxProfit(val,wt,w,n))
