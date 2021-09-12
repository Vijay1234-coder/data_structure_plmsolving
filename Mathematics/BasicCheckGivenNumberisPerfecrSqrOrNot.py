import math


def isperfectSqr(num):
    root =int(math.sqrt(num))
    if root*root == num:
        return True
    return False


n =int(input())
print(isperfectSqr(n))