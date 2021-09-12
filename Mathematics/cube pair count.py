import math
def pairCubeCount(N):
    croot = int(math.pow(N,1/3))
    print(croot)
    c = 0
    for i in range(1, croot + 1):
        x = i * i * i

        y = N - x
        print(y)
        m = int(math.pow(y,1/3))


        if m ** 3 == y:
            print(m)
            c += 1
    return c




print(pairCubeCount(1729))