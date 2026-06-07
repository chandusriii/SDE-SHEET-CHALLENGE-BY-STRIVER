from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """Return the length of the longest consecutive sequence."""
        num_set = set(nums)
        longest = 0

        for num in num_set:
            if num - 1 not in num_set:
                current = num
                length = 1

                while current + 1 in num_set:
                    current += 1
                    length += 1

                longest = max(longest, length)

        return longest


if __name__ == "__main__":
    solution = Solution()

    nums1 = [100, 4, 200, 1, 3, 2]
    print(f"Input: {nums1}")
    print(f"Output: {solution.longestConsecutive(nums1)}")
    print("Expected: 4\n")

    nums2 = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
    print(f"Input: {nums2}")
    print(f"Output: {solution.longestConsecutive(nums2)}")
    print("Expected: 9\n")

    nums3 = [1, 9, 3, 10, 4, 20, 2]
    print(f"Input: {nums3}")
    print(f"Output: {solution.longestConsecutive(nums3)}")
    print("Expected: 4\n")
