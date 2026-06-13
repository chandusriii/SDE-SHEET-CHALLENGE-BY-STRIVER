class Solution:
    def threeSum(self, nums):
        """Return all unique triplets whose sum is zero."""
        nums.sort()
        n = len(nums)
        result = []

        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = n - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                elif total < 0:
                    left += 1
                else:
                    right -= 1

        return result


if __name__ == "__main__":
    solution = Solution()

    nums1 = [2, -2, 0, 3, -3, 5]
    print("Input: nums = [2, -2, 0, 3, -3, 5]")
    print(f"Output: {solution.threeSum(nums1)}")
    print("Expected: [[-3, -2, 5], [-3, 0, 3], [-2, 0, 2]]\n")

    nums2 = [2, -1, -1, 3, -1]
    print("Input: nums = [2, -1, -1, 3, -1]")
    print(f"Output: {solution.threeSum(nums2)}")
    print("Expected: [[-1, -1, 2]]\n")

    nums3 = [8, -6, 5, 4]
    print("Input: nums = [8, -6, 5, 4]")
    print(f"Output: {solution.threeSum(nums3)}")
    print("Expected: []\n")
