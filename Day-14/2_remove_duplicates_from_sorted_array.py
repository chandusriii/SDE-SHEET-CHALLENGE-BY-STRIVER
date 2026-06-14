from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """Move unique values to the front and return their count."""
        if not nums:
            return 0

        unique_index = 0

        for current in range(1, len(nums)):
            if nums[current] != nums[unique_index]:
                unique_index += 1
                nums[unique_index] = nums[current]

        return unique_index + 1


if __name__ == "__main__":
    solution = Solution()

    nums1 = [0, 0, 3, 3, 5, 6]
    print(f"Input: nums = {nums1}")
    k1 = solution.removeDuplicates(nums1)
    print(f"Output: {k1}")
    print(f"First {k1} elements: {nums1[:k1]}")
    print("Expected: 4, [0, 3, 5, 6]\n")

    nums2 = [-2, 2, 4, 4, 4, 4, 5, 5]
    print(f"Input: nums = {nums2}")
    k2 = solution.removeDuplicates(nums2)
    print(f"Output: {k2}")
    print(f"First {k2} elements: {nums2[:k2]}")
    print("Expected: 4, [-2, 2, 4, 5]\n")

    nums3 = [-30, -30, 0, 0, 10, 20, 30, 30]
    print(f"Input: nums = {nums3}")
    k3 = solution.removeDuplicates(nums3)
    print(f"Output: {k3}")
    print(f"First {k3} elements: {nums3[:k3]}")
    print("Expected: 5, [-30, 0, 10, 20, 30]\n")
