class Solution:
    def canPlace(self, nums, k, dist):
        count = 1
        last = nums[0]

        for i in range(1, len(nums)):
            if nums[i] - last >= dist:
                count += 1
                last = nums[i]

                if count >= k:
                    return True

        return False

    def aggressiveCows(self, nums, k):
        nums.sort()

        low = 1
        high = nums[-1] - nums[0]
        ans = 0

        while low <= high:
            mid = (low + high) // 2

            if self.canPlace(nums, k, mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1

        return ans


# Driver Code
nums = [10, 1, 2, 7, 5]
k = 3

obj = Solution()
print(obj.aggressiveCows(nums, k))
