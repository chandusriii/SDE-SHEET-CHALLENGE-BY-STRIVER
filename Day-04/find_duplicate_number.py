"""
Find the Duplicate Number

Problem: Given an array of integers containing n + 1 integers where each integer 
is in the range [1, n] inclusive, there is only one repeated number. Return this 
duplicate number.

Constraints:
- You must not modify the array (assume it is read-only)
- You must use only constant extra space
- Your algorithm should run in less than O(n²) time

Approach: Floyd's Cycle Detection (Tortoise & Hare)
Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def findDuplicate(self, nums):
        """
        Find the duplicate number using Floyd's Cycle Detection.
        
        The idea is to treat the array as a linked list where arr[i] is the 
        next pointer. The duplicate number will be the entrance to the cycle.
        
        Args:
            nums: List of integers containing one duplicate
            
        Returns:
            The duplicate number
        """
        slow = nums[0]
        fast = nums[0]

        # Phase 1: Find intersection point in the cycle
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break

        # Phase 2: Find entrance to the cycle
        slow = nums[0]

        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    nums1 = [1, 3, 4, 2, 2]
    print(f"Input: {nums1}")
    print(f"Output: {solution.findDuplicate(nums1)}")  # Expected: 2
    print()
    
    # Test case 2
    nums2 = [3, 1, 3, 4, 2]
    print(f"Input: {nums2}")
    print(f"Output: {solution.findDuplicate(nums2)}")  # Expected: 3
    print()
    
    # Test case 3
    nums3 = [1, 1]
    print(f"Input: {nums3}")
    print(f"Output: {solution.findDuplicate(nums3)}")  # Expected: 1
