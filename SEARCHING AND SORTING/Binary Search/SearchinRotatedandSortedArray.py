
def solve(arr, target):
    start = 0
    end = len(arr)-1
    while start <= end:
        mid = start+end//2
        if arr[mid]==target:
            return mid
        else:
            if arr[mid]>arr[start]:
                if target>=arr[start] and target<arr[mid]:
                    end =mid-1
                else:
                    start=mid+1
            else:
                if target>arr[mid+1] and target<=arr[end]:
                    start =mid+1
                else:
                    end =mid-1
    return -1








print(solve([ 3, 3, 3, 1, 2, 3 ],3))
