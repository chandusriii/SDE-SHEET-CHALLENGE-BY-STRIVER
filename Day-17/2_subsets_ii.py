from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        """Return all unique subsets when nums may contain duplicates."""
        nums.sort()
        result = []

        def backtrack(start: int, subset: List[int]) -> None:
            result.append(subset[:])

            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue

                subset.append(nums[i])
                backtrack(i + 1, subset)
                subset.pop()

        backtrack(0, [])
        return result


if __name__ == "__main__":
    solution = Solution()

    nums1 = [1, 2, 2]
    print(f"Input: nums = {nums1}")
    print(f"Output: {solution.subsetsWithDup(nums1)}")
    print("Expected: [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]\n")

    nums2 = [1, 2]
    print(f"Input: nums = {nums2}")
    print(f"Output: {solution.subsetsWithDup(nums2)}")
    print("Expected: [[], [1], [1, 2], [2]]\n")

    nums3 = [1, 3, 3]
    print(f"Input: nums = {nums3}")
    print(f"Output: {solution.subsetsWithDup(nums3)}")
    print("Expected: [[], [1], [1, 3], [1, 3, 3], [3], [3, 3]]")
