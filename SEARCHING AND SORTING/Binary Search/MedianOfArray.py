
def findMedianSortedArrays( nums1, nums2):
    # We optimize this to run binary search on the smaller array
    if len(nums1) > len(nums2):
        return findMedianSortedArrays(nums2, nums1)

    end = len(nums1)
    n = len(nums1)   # [3] [-2,-1]
    m = len(nums2)
    start = 0
    idx_middle = (m + n + 1) // 2  # Center index of final merged array

    while start <= end:
        i1 = (start + end) // 2
        i2 = idx_middle - i1

        max1 = nums1[i1 - 1] if i1 != 0 else -float('inf')
        min1 = nums1[i1] if i1 != n else float('inf')
        max2 = nums2[i2 - 1] if i2 != 0 else -float('inf')
        min2 = nums2[i2] if i2 != m else float('inf')

        if max1 > min2:
            # move nums1 end to before partition
            end = i1 - 1
        elif max2 > min1:
            # move nums1 start to after partition
            start = i1 + 1
        else:
            # Found the right partition!
            # if odd, ans is max(maxleft1, maxleft2)
            # if even, ans is avg of max(maxleft1, maxleft2) and min(minright1, minright2)
            max_of_left = max(max1, max2)
            if (m + n) % 2 == 0:
                min_of_right = min(min1, min2)
                return (max_of_left + min_of_right) / 2
            else:
                return max_of_left



nums1=[3]
nums2=[-2,-1]

print(findMedianSortedArrays( nums1, nums2))



