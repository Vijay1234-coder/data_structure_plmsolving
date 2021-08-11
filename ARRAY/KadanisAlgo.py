def maxSubArraySum(self, a, size):
    cur = a[0]
    maxsum = a[0]
    for i in range(1, size):
        if cur >= 0:
            cur += a[i]

        else:
            cur = a[i]
        maxsum = max(cur, maxsum)
    return maxsum
