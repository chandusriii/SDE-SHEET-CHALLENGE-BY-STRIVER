class Solution:
    def nextPermutation(self, nums):
        n = len(nums)

        # Step 1: Find the breakpoint
        ind = -1
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                ind = i
                break

        # Step 2: If no breakpoint exists, reverse the whole array
        if ind == -1:
            nums.reverse()
            return nums

        # Step 3: Find the next greater element and swap
        for i in range(n - 1, ind, -1):
            if nums[i] > nums[ind]:
                nums[i], nums[ind] = nums[ind], nums[i]
                break

        # Step 4: Reverse the suffix
        left, right = ind + 1, n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

        return nums
