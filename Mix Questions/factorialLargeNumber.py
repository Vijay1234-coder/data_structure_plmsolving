def display(arr):
    for i in arr:
        print(i,end="")




def extraLongFactorials(n):
    a = 1
    while n:
        a = a * n
        n -= 1
    arr = []
    a=str(a)
    for char in a:
        arr.append(int(char))

    display(arr)
    return

if __name__ == '__main__':
    n = int(input("eneter number"))

    print(extraLongFactorials(n))
