"""
Find the Repeating and Missing Number

Problem: Given an integer array of size n containing values from [1, n] where 
each value appears exactly once, except for value A which appears twice and 
value B which is missing. Return [A, B].

Constraints:
- You are not allowed to modify the original array
- 1 ≤ n ≤ 10^5

Approach: Mathematical approach using Sum and Sum of Squares
Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def findMissingRepeatingNumbers(self, nums):
        """
        Find the repeating and missing numbers using mathematical equations.
        
        Let X = repeating number, Y = missing number
        
        We know:
        - X - Y = S - SN (difference of actual vs expected sum)
        - X² - Y² = S2 - S2N (difference of actual vs expected sum of squares)
        
        From these equations:
        - X + Y = (X² - Y²) / (X - Y)
        - X = ((X-Y) + (X+Y)) / 2
        - Y = X - (X-Y)
        
        Args:
            nums: List of integers with one repeating and one missing
            
        Returns:
            List [repeating_number, missing_number]
        """
        n = len(nums)

        # Expected sum: n(n+1)/2
        SN = n * (n + 1) // 2
        
        # Expected sum of squares: n(n+1)(2n+1)/6
        S2N = n * (n + 1) * (2 * n + 1) // 6

        # Actual sum
        S = sum(nums)
        
        # Actual sum of squares
        S2 = sum(x * x for x in nums)

        # X - Y (repeating - missing)
        val1 = S - SN

        # X² - Y² = (X-Y)(X+Y)
        val2 = S2 - S2N

        # X + Y = (X² - Y²) / (X - Y)
        val2 = val2 // val1

        # Repeating number (X) = ((X-Y) + (X+Y)) / 2
        x = (val1 + val2) // 2

        # Missing number (Y) = X - (X-Y)
        y = x - val1

        return [x, y]


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    nums1 = [3, 5, 4, 1, 1]
    print(f"Input: {nums1}")
    print(f"Output: {solution.findMissingRepeatingNumbers(nums1)}")  # Expected: [1, 2]
    print()
    
    # Test case 2
    nums2 = [1, 2, 3, 6, 7, 5, 7]
    print(f"Input: {nums2}")
    print(f"Output: {solution.findMissingRepeatingNumbers(nums2)}")  # Expected: [7, 4]
    print()
    
    # Test case 3
    nums3 = [6, 5, 7, 1, 8, 6, 4, 3, 2]
    print(f"Input: {nums3}")
    print(f"Output: {solution.findMissingRepeatingNumbers(nums3)}")  # Expected: [6, 9]
