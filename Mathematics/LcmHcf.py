'''  GCD  Euclidean Algorithm '''

def gcd(a,b):
    # base case
    if b == 0:
        return a
    else:
        return gcd(b,a%b)





print(gcd(98,56))