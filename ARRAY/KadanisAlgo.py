def maxSubArraySum(self, a, size):
    cur = a[0]
    maxsum = a[0]
    for i in range(1, size):
        cur= max(a[i],cur+a[i])
        maxsum = max(maxsum,cur)
    return maxsum
