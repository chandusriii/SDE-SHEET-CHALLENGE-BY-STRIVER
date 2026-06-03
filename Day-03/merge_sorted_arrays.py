"""
Day 3 - Problem 1: Merge Two Sorted Arrays Without Extra Space
Link: https://takeuforward.org/dsa/merge-two-sorted-arrays-without-extra-space/
LeetCode: https://leetcode.com/problems/merge-sorted-array/
"""

class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        Merge nums2 into nums1 as one sorted array in-place.
        
        Args:
            nums1: First sorted array with enough space
            m: Number of valid elements in nums1
            nums2: Second sorted array
            n: Number of elements in nums2
        
        Time Complexity: O(m + n)
        Space Complexity: O(1)
        
        Approach: Two pointers from the end
        - Start with pointers at end of both arrays
        - Place larger element at the end of nums1
        - Move corresponding pointer backward
        """
        i = m - 1          # Pointer for nums1
        j = n - 1          # Pointer for nums2
        k = m + n - 1      # Pointer for nums1 end position

        # Compare and place elements from both arrays
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

        # If nums2 has remaining elements, copy them
        # (nums1 elements already in place if nums1 has remaining)
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1


# Test cases
if __name__ == "__main__":
    sol = Solution()
    
    # Test case 1
    nums1 = [-5, -2, 4, 5, 0, 0, 0]
    nums2 = [-3, 1, 8]
    sol.merge(nums1, 4, nums2, 3)
    print("Test 1:", nums1)  # Expected: [-5, -3, -2, 1, 4, 5, 8]
    
    # Test case 2
    nums1 = [0, 2, 7, 8, 0, 0, 0]
    nums2 = [-7, -3, -1]
    sol.merge(nums1, 4, nums2, 3)
    print("Test 2:", nums1)  # Expected: [-7, -3, -1, 0, 2, 7, 8]
    
    # Test case 3
    nums1 = [1, 3, 5, 0, 0, 0, 0]
    nums2 = [2, 4, 6, 7]
    sol.merge(nums1, 3, nums2, 4)
    print("Test 3:", nums1)  # Expected: [1, 2, 3, 4, 5, 6, 7]
