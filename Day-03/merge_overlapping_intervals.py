"""
Day 3 - Problem 2: Merge Overlapping Subintervals
Link: https://takeuforward.org/dsa/merge-overlapping-subintervals
LeetCode: https://leetcode.com/problems/merge-intervals/
"""

class Solution:
    def mergeOverlap(self, intervals):
        """
        Merge all overlapping intervals.
        
        Args:
            intervals: List of [start, end] intervals
        
        Returns:
            List of merged non-overlapping intervals
        
        Time Complexity: O(n log n) due to sorting
        Space Complexity: O(1) if output space not counted
        
        Approach: Sort + Greedy Merge
        1. Sort intervals by start time
        2. Iterate through sorted intervals
        3. If overlaps with last merged interval, extend the end
        4. If no overlap, add current interval to result
        """
        # Sort intervals by start time
        intervals.sort()

        merged = []

        for interval in intervals:
            # No overlap: current interval starts after previous ends
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            # Overlap: extend the end point of last merged interval
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged


# Test cases
if __name__ == "__main__":
    sol = Solution()
    
    # Test case 1
    intervals1 = [[1, 5], [3, 6], [8, 10], [15, 18]]
    result1 = sol.mergeOverlap(intervals1)
    print("Test 1:", result1)  # Expected: [[1, 6], [8, 10], [15, 18]]
    
    # Test case 2
    intervals2 = [[5, 7], [1, 3], [4, 6], [8, 10]]
    result2 = sol.mergeOverlap(intervals2)
    print("Test 2:", result2)  # Expected: [[1, 3], [4, 7], [8, 10]]
    
    # Test case 3: Single interval
    intervals3 = [[1, 3]]
    result3 = sol.mergeOverlap(intervals3)
    print("Test 3:", result3)  # Expected: [[1, 3]]
    
    # Test case 4: No overlapping
    intervals4 = [[1, 2], [3, 4], [5, 6]]
    result4 = sol.mergeOverlap(intervals4)
    print("Test 4:", result4)  # Expected: [[1, 2], [3, 4], [5, 6]]
    
    # Test case 5: All overlapping
    intervals5 = [[1, 5], [2, 6], [3, 7]]
    result5 = sol.mergeOverlap(intervals5)
    print("Test 5:", result5)  # Expected: [[1, 7]]
