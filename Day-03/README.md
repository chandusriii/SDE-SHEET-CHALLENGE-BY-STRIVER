# #45DaysSDEChallenge - Day 3

**Date:** June 3, 2026  
**Problems Solved Today:** 3  
**Sheet:** [Striver SDE Sheet](https://takeuforward.org/dsa/strivers-sde-sheet-top-coding-interview-problems)

---

## 1) Merge Two Sorted Arrays Without Extra Space

- **TUF Problem:** [Merge two sorted arrays without extra space](https://takeuforward.org/dsa/merge-two-sorted-arrays-without-extra-space/)
- **LeetCode:** [Merge Sorted Array (LC 88)](https://leetcode.com/problems/merge-sorted-array/)
- **Striver Video:** [Watch](https://youtu.be/hA2WZqKqk6I)

### Problem Statement
Given two integer arrays nums1 and nums2, both sorted in non-decreasing order.
Merge both arrays into a single array sorted in non-decreasing order.
The final sorted array should be stored inside the array nums1 and it should be done in-place.
nums1 has a length of m + n, where the first m elements denote the elements of nums1 and rest are 0s.

### What Striver Discussed
- **Brute force:** Use extra space to merge, then copy back.
- **Better approach:** Two-pointer approach from the start, but needs temp array.
- **Optimal approach (used):** Two-pointer approach from the end.
  1. Start with pointers at the end of both arrays and the end of nums1.
  2. Compare elements from both arrays and place the larger one at the current position in nums1.
  3. Move the corresponding pointer backward.
  4. If nums2 has remaining elements, copy them to nums1.

### Clean Python Solution
```python
class Solution:
    def merge(self, nums1, m, nums2, n):
        i = m - 1
        j = n - 1
        k = m + n - 1

        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1
```

### Complexity
- **Time:** O(m + n)
- **Space:** O(1)

### Example
```
Input: nums1 = [1, 3, 5], nums2 = [2, 4, 6, 7]
Output: [1, 2, 3, 4, 5, 6, 7]
```

---

## 2) Merge Overlapping Subintervals

- **TUF Problem:** [Merge Overlapping Subintervals](https://takeuforward.org/dsa/merge-overlapping-subintervals)
- **LeetCode:** [Merge Intervals (LC 56)](https://leetcode.com/problems/merge-intervals/)
- **Striver Video:** [Watch](https://youtu.be/2JzRBUi1nC0)

### Problem Statement
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals and return an array of the non-overlapping intervals that cover all the intervals in the input.

### What Striver Discussed
- **Brute force:** Compare each interval with every other interval (O(n²)).
- **Optimal approach (used):**
  1. Sort intervals by their start time.
  2. Iterate through sorted intervals.
  3. If the current interval overlaps with the last merged interval, extend the end point.
  4. If no overlap, add the current interval to the result.

### Clean Python Solution
```python
class Solution:
    def mergeOverlap(self, intervals):
        # Sort intervals by start time
        intervals.sort()

        merged = []

        for interval in intervals:
            # No overlap
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            # Overlap
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged
```

### Complexity
- **Time:** O(n log n) due to sorting
- **Space:** O(1) if we don't count output space

### Example
```
Input: intervals = [[1,5],[3,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Intervals [1,5] and [3,6] overlap, so they are merged into [1,6].
```

---

## 3) Rotate Matrix by 90 Degrees

- **TUF Problem:** [Rotate matrix by 90 degrees](https://takeuforward.org/dsa/rotate-matrix-by-90-degree)
- **LeetCode:** [Rotate Image (LC 48)](https://leetcode.com/problems/rotate-image/)
- **Striver Video:** [Watch](https://youtu.be/Y8QKJZR0gak)

### Problem Statement
Given an N × N 2D integer matrix, rotate the matrix by 90 degrees clockwise in place.
The rotation must be done in place, meaning the input 2D matrix must be modified directly.

### What Striver Discussed
- **Brute force:** Use extra space to create a new rotated matrix.
- **Better approach:** Rotate layer by layer using in-place swaps.
- **Optimal approach (used):** Two-step transformation.
  1. **Transpose:** Swap matrix[i][j] with matrix[j][i].
  2. **Reverse each row:** Reverse all elements in each row.

### Clean Python Solution
```python
class Solution:
    def rotateMatrix(self, matrix):
        n = len(matrix)

        # Transpose
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Reverse each row
        for i in range(n):
            matrix[i].reverse()

        return matrix
```

### Complexity
- **Time:** O(n²)
- **Space:** O(1)

### Example
```
Input: matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
Output: [[7, 4, 1], [8, 5, 2], [9, 6, 3]]

Visual transformation:
Original:     After Transpose:     After Row Reverse:
1 2 3         1 4 7                7 4 1
4 5 6    →    2 5 8            →   8 5 2
7 8 9         3 6 9                9 6 3
```

---

## Key Learnings From Today

### Merge Two Sorted Arrays
- Understood the importance of working from the end to avoid overwriting data in-place.
- Realized how two-pointer technique can be optimized by starting from both ends.

### Merge Overlapping Intervals
- Learned sorting as a preprocessing step can simplify problems dramatically.
- Understood how to identify and merge overlapping ranges efficiently.

### Rotate Matrix by 90 Degrees
- Discovered that rotation can be decomposed into transpose + row reversal operations.
- Appreciated the elegance of mathematical transformations for in-place operations.

---

## Summary Statistics

| Problem | Time | Space | Approach |
|---------|------|-------|----------|
| Merge Two Sorted Arrays | O(m + n) | O(1) | Two Pointers (from end) |
| Merge Overlapping Intervals | O(n log n) | O(1) | Sort + Greedy Merge |
| Rotate Matrix by 90 Degrees | O(n²) | O(1) | Transpose + Reverse |
