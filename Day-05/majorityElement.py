"""
Majority Element - Day 5 SDE Sheet Challenge

Problem: Given an integer array nums of size n, return the majority element of the array.
The majority element of an array is an element that appears more than n/2 times in the array.
The array is guaranteed to have a majority element.

Algorithm: Boyer-Moore Majority Vote Algorithm
Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def majorityElement(self, nums):
        """
        Find the majority element using Boyer-Moore Majority Vote Algorithm.
        
        The algorithm works on the principle that if an element occurs more than n/2 times,
        it will always be the last element standing after the cancellation process.
        
        Approach:
        1. Maintain a candidate and a count.
        2. For each number:
           - If count is 0, make current number as candidate.
           - If current number equals candidate, increment count.
           - Otherwise, decrement count.
        3. The remaining candidate is the majority element.
        
        Args:
            nums: List of integers
            
        Returns:
            The majority element that appears more than n/2 times
        """
        count = 0
        candidate = None

        for num in nums:
            # If count is 0, reset candidate to current number
            if count == 0:
                candidate = num

            # If current number matches candidate, increment count
            if num == candidate:
                count += 1
            # Otherwise, decrement count (it's like cancellation)
            else:
                count -= 1

        return candidate


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    nums1 = [7, 0, 0, 1, 7, 7, 2, 7, 7]
    print(f"Input: nums = {nums1}")
    print(f"Output: {solution.majorityElement(nums1)}")
    print(f"Explanation: The number 7 appears 5 times in the 9 sized array")
    print()
    
    # Test case 2
    nums2 = [1, 1, 1, 2, 1, 2]
    print(f"Input: nums = {nums2}")
    print(f"Output: {solution.majorityElement(nums2)}")
    print(f"Explanation: The number 1 appears 4 times in the 6 sized array")
    print()
    
    # Test case 3
    nums3 = [-1, -1, -1, -1]
    print(f"Input: nums = {nums3}")
    print(f"Output: {solution.majorityElement(nums3)}")
    print(f"Explanation: The number -1 appears 4 times in the 4 sized array")
    print()
    
    # Additional test cases
    nums4 = [1]
    print(f"Input: nums = {nums4}")
    print(f"Output: {solution.majorityElement(nums4)}")
    print()
    
    nums5 = [3, 2, 3]
    print(f"Input: nums = {nums5}")
    print(f"Output: {solution.majorityElement(nums5)}")
