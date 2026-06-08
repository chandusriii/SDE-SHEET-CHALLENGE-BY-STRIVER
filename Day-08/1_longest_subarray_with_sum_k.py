from typing import List


class Solution:
    def longestSubarray(self, nums: List[int], k: int) -> int:
        """Return the longest subarray length with sum equal to k."""
        prefix_sum = 0
        longest = 0
        first_seen = {}

        for index, num in enumerate(nums):
            prefix_sum += num

            if prefix_sum == k:
                longest = index + 1

            remaining = prefix_sum - k
            if remaining in first_seen:
                longest = max(longest, index - first_seen[remaining])

            if prefix_sum not in first_seen:
                first_seen[prefix_sum] = index

        return longest


if __name__ == "__main__":
    solution = Solution()

    nums1 = [10, 5, 2, 7, 1, 9]
    k1 = 15
    print(f"Input: nums = {nums1}, k = {k1}")
    print(f"Output: {solution.longestSubarray(nums1, k1)}")
    print("Expected: 4\n")

    nums2 = [-3, 2, 1]
    k2 = 6
    print(f"Input: nums = {nums2}, k = {k2}")
    print(f"Output: {solution.longestSubarray(nums2, k2)}")
    print("Expected: 0\n")

    nums3 = [-1, 1, 1]
    k3 = 1
    print(f"Input: nums = {nums3}, k = {k3}")
    print(f"Output: {solution.longestSubarray(nums3, k3)}")
    print("Expected: 3\n")
