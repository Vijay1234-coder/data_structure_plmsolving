







class Solution:
    def lengthOfLIS(self, nums):
        n = len(nums)
        tail = []
        tail.append(nums[0])
        for i in range(1, n):
            if nums[i] > tail[-1]:
                tail.append(nums[i])
            else:
                ceil_idx = self.findceil(tail, nums[i])
                tail[ceil_idx] = nums[i]
        print(len(tail))

    def findceil(self, arr, key):
        start = 0
        end = len(arr) - 1
        res = 0

        while start <= end:
            mid = (start + end) // 2
            if arr[mid] == key:
                return mid
            elif arr[mid] > key:
                res = mid
                end = mid - 1
            else:
                start = mid + 1
        return res






nums =[10,9,2,5,3,7,101,18]
s =Solution()
s.lengthOfLIS(nums)