class Solution:
    def search(self, nums, k):
        low, high = 0, len(nums) - 1

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] == k:
                return mid

            # Left half is sorted
            if nums[low] <= nums[mid]:
                if nums[low] <= k < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1

            # Right half is sorted
            else:
                if nums[mid] < k <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1

        return -1


# Driver Code
nums = [4, 5, 6, 7, 0, 1, 2]
k = 5

obj = Solution()
print(obj.search(nums, k))
