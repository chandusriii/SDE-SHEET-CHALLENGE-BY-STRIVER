from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        """Return the longest run of consecutive 1s."""
        count = 0
        maximum = 0

        for num in nums:
            if num == 1:
                count += 1
                maximum = max(maximum, count)
            else:
                count = 0

        return maximum


if __name__ == "__main__":
    solution = Solution()

    nums1 = [1, 1, 0, 0, 1, 1, 1, 0]
    print(f"Input: nums = {nums1}")
    print(f"Output: {solution.findMaxConsecutiveOnes(nums1)}")
    print("Expected: 3\n")

    nums2 = [0, 0, 0, 0, 0, 0, 0, 0]
    print(f"Input: nums = {nums2}")
    print(f"Output: {solution.findMaxConsecutiveOnes(nums2)}")
    print("Expected: 0\n")

    nums3 = [1, 0, 1, 1, 1, 0, 1, 1, 1]
    print(f"Input: nums = {nums3}")
    print(f"Output: {solution.findMaxConsecutiveOnes(nums3)}")
    print("Expected: 3\n")
