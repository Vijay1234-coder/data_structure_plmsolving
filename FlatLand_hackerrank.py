def flatlandSpaceStations(n, c):
    if m == n:
        return 0
    else:
        c.sort()
        Max = max(c[0], (n - 1) - c[-1])
        for i in range(1, m):
            d = (c[i] - c[i - 1]) // 2
            Max = max(Max, d)
    return Max


if __name__ == '__main__':


    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    c = list(map(int, input().rstrip().split()))

    result = flatlandSpaceStations(n, c)

