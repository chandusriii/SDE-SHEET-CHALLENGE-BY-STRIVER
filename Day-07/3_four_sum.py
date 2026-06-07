from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        """Return all unique quadruplets that sum to target."""
        nums.sort()
        n = len(nums)
        ans = []

        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            for j in range(i + 1, n):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                left = j + 1
                right = n - 1

                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]

                    if total == target:
                        ans.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                        right -= 1

                        while left < right and nums[left] == nums[left - 1]:
                            left += 1

                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
                    elif total < target:
                        left += 1
                    else:
                        right -= 1

        return ans


if __name__ == "__main__":
    solution = Solution()

    nums1 = [1, -2, 3, 5, 7, 9]
    target1 = 7
    print(f"Input: nums = {nums1}, target = {target1}")
    print(f"Output: {solution.fourSum(nums1, target1)}")
    print("Expected: [[-2, 1, 3, 5]]\n")

    nums2 = [7, -7, 1, 2, 14, 3]
    target2 = 9
    print(f"Input: nums = {nums2}, target = {target2}")
    print(f"Output: {solution.fourSum(nums2, target2)}")
    print("Expected: []\n")

    nums3 = [1, 1, 3, 4, -3]
    target3 = 5
    print(f"Input: nums = {nums3}, target = {target3}")
    print(f"Output: {solution.fourSum(nums3, target3)}")
    print("Expected: [[-3, 1, 3, 4]]\n")
