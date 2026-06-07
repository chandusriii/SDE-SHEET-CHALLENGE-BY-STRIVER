from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """Return indices of two numbers that add up to target."""
        seen = {}

        for index, num in enumerate(nums):
            complement = target - num

            if complement in seen:
                return [seen[complement], index]

            seen[num] = index

        return [-1, -1]


if __name__ == "__main__":
    solution = Solution()

    nums1 = [1, 6, 2, 10, 3]
    target1 = 7
    print(f"Input: nums = {nums1}, target = {target1}")
    print(f"Output: {solution.twoSum(nums1, target1)}")
    print("Expected: [0, 1]\n")

    nums2 = [1, 3, 5, -7, 6, -3]
    target2 = 0
    print(f"Input: nums = {nums2}, target = {target2}")
    print(f"Output: {solution.twoSum(nums2, target2)}")
    print("Expected: [1, 5]\n")

    nums3 = [-6, 7, 1, -7, 6, 2]
    target3 = 3
    print(f"Input: nums = {nums3}, target = {target3}")
    print(f"Output: {solution.twoSum(nums3, target3)}")
    print("Expected: [2, 5]\n")
