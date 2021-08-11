from math import sqrt


def encryption(s):
    l = s.strip().split()
    s = "".join(l)

    n = len(s)
    root = sqrt(n)
    if int(root) < root:
        row = int(root)
        col = int(root) + 1
    else:
        row = col = int(root)
    if row * col < n:
        row = max(row, col)

    i = 0
    l=[]

    while i < n-1:

        j = i+(col-1)

        l.append(s[i:j+1])

        i = j + 1
    print(l)
    r = ""
    for i in range(4):
        r = r +l

    # r=""
    # for i in range(col):
    #     j = i+(row)+1
    #     k = j+row+1
    #     if k>n-1:
    #         r = r+s[i]+s[j]+" "
    #         break
    #     else:
    #         r = r + s[i] + s[j] +s[k]+" "
    # print(r)






if __name__ == '__main__': # tij  hsj ivy si #thisisvijay  l[0][0]+l[1][0]+l[2][0]+ " " +l
    s = input("enter string")

    encryption(s)