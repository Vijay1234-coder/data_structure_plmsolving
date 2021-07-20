def play_the_game(target):
    n =len(target)

    res = 0


    while (True):


        z_c = 0


        i = 0
        while (i < n):


            if ((target[i] & 1) > 0):
                break


            elif (target[i] == 0):
                z_c += 1
            i += 1


        if (z_c == n):
            return res


        if (i == n):


            for j in range(n):
                target[j] = target[j] // 2
            res += 1


        for j in range(i, n):
            if (target[j] & 1):
                target[j] -= 1
                res += 1



arr = list(map(int,input().split()))

print(play_the_game(arr))