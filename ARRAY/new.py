n, k = map(int, input().split())

arr = list(map(int, input().split()))

c = 0
i = 0
arr.sort()
while i < n:
    j = i + 1
    while (arr[i] + k >= arr[j]) and j < n:
        j += 1
    x = j
    j -= 1

    while (arr[j] + k >= arr[x]) and x < n:
        x += 1

    c += 1
    i = x

print(c)
