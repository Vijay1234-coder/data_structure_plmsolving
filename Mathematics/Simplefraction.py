#https://practice.geeksforgeeks.org/problems/a-simple-fraction0921/1#
def fractionToDecimal( n, d):
    ans = ""
    q = n // d
    rem = n % d
    ans += str(q)
    if rem == 0:
        return ans
    else:
        ans += "."

    dictt = {}

    while rem != 0:
        if rem not in dictt:
            dictt[rem] = len(ans)
            rem = rem * 10
            q = rem // d
            rem = rem % d
            ans = ans + str(q)
        else:
            l = dictt[rem]
            ans = ans[:l] + "(" + ans[l:] + ")"
            break


    return ans

res =fractionToDecimal(1,3)
print(res)