#https://www.geeksforgeeks.org/stock-buy-sell/
def maxProfit(price,start,end):
    profit =0
    for i in range(1,n):
        if price[i]>price[i-1]:
            profit+=(price[i]-price[i-1])
    return profit



price = [100, 180, 260, 310, 40, 535, 695]
n = len(price)

print(maxProfit(price,0,n-1))