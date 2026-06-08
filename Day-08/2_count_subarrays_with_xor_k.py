from typing import List


class Solution:
    def subarraysWithXorK(self, nums: List[int], k: int) -> int:
        """Return the number of subarrays with XOR equal to k."""
        prefix_count = {0: 1}
        current_xor = 0
        count = 0

        for num in nums:
            current_xor ^= num
            target = current_xor ^ k

            count += prefix_count.get(target, 0)
            prefix_count[current_xor] = prefix_count.get(current_xor, 0) + 1

        return count


if __name__ == "__main__":
    solution = Solution()

    nums1 = [4, 2, 2, 6, 4]
    k1 = 6
    print(f"Input: nums = {nums1}, k = {k1}")
    print(f"Output: {solution.subarraysWithXorK(nums1, k1)}")
    print("Expected: 4\n")

    nums2 = [5, 6, 7, 8, 9]
    k2 = 5
    print(f"Input: nums = {nums2}, k = {k2}")
    print(f"Output: {solution.subarraysWithXorK(nums2, k2)}")
    print("Expected: 2\n")

    nums3 = [5, 2, 9]
    k3 = 7
    print(f"Input: nums = {nums3}, k = {k3}")
    print(f"Output: {solution.subarraysWithXorK(nums3, k3)}")
    print("Expected: 1\n")
