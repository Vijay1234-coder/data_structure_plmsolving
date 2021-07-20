def Bsearch(arr):
    start = 0
    end = len(arr) - 1

    mid = (start + end) // 2
    if len(arr) % 2 != 0:
        return float(arr[mid])
    else:
        median = (arr[mid] + arr[mid + 1]) / 2
        return median


def findMedianSortedArrays(arr1,arr2):
    n = len(arr1)

    m = len(arr2)

    if m < n:
        arr2 = arr1
        arr1 = arr2

    if n == 0:
        if m == 1:
            return float(arr2[0])
        if m == 2:
            return (arr2[0] + arr2[1]) / 2
        else:
            return Bsearch(arr2)

    if m == 0:
        if n == 1:
            return float(arr1[0])
        if n == 2:
            return (arr1[0] + arr1[1]) / 2
        else:
            return Bsearch(arr1)



    start1 = 0
    end1 = len(arr1)
    total =(m + n + 1) // 2

    while (start1 <= end1):

        i1 = (start1 + end1) // 2

        i2 = total - i1

        max1 = arr1[i1 - 1] if i1 != 0 else -float('inf')
        min1 = arr1[i1] if i1 != n else float('inf')
        max2 = arr2[i2 - 1] if i2 != 0 else -float('inf')
        min2 = arr2[i2] if i2 != m else float('inf')

        # if max2 <= min1 and max1 <= min2:
        #     if (m + n) % 2 == 0:
        #         median = (max(max1, max2) + min(min1, min2)) / 2
        #         return median
        #     else:
        #         median = (max(max1, max2)) / 2
        #         return median
        if (max1 > min2):
            end1 = i1 - 1

        elif (max2 > min1):
            start1 = i1 + 1
        else:

            if (m + n) % 2 == 0:
                median = (max(max1, max2) + min(min1, min2)) / 2
                return median
            else:
                median = (max(max1,max2)) / 2
                return median

arr1 = [3]
arr2 = [-2,-1]
print(findMedianSortedArrays(arr1,arr2))