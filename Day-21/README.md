#45DaysSDEChallenge - Day 21

Date: June 21, 2026
Problems Solved Today: 3
Sheet: Striver SDE Sheet

## 1) Find Nth Root of a Number

**TUF Problem:** The N-th Root of an Integer

### Problem Statement

Given two numbers N and M, find the Nth root of M. The Nth root of a number M is defined as a number X such that when X is raised to the power of N, it equals M. If the Nth root is not an integer, return -1.

### What Striver Discussed

* Use Binary Search on the answer space from 1 to M.
* Compute mid raised to the power N.
* If the value equals M, return mid.
* If the value is smaller than M, search the right half.
* Otherwise, search the left half.
* Stop early when the power exceeds M to avoid unnecessary calculations.

### Clean Python Solution

```python
class Solution:
    def NthRoot(self, N, M):
        low, high = 1, M

        while low <= high:
            mid = (low + high) // 2

            power = 1
            for _ in range(N):
                power *= mid
                if power > M:
                    break

            if power == M:
                return mid
            elif power < M:
                low = mid + 1
            else:
                high = mid - 1

        return -1
```

### Test Cases

Input: N = 3, M = 27
Output: 3

Input: N = 4, M = 69
Output: -1

### Now Your Turn

Input: N = 4, M = 81
Output: 3

### Complexity

Time: O(N × log M) - Binary Search with power computation at each step
Space: O(1)

---

## 2) Matrix Median

**TUF Problem:** Matrix Median

### Problem Statement

Given a row-wise sorted matrix, find the median of the matrix without flattening and sorting the entire matrix.

### What Striver Discussed

* Since each row is sorted, Binary Search can be applied on the value range.
* Find the minimum and maximum values in the matrix.
* For every middle value, count how many elements are less than or equal to it.
* Use bisect_right (upper bound) to efficiently count elements in each row.
* The first value whose count reaches the median position is the answer.

### Clean Python Solution

```python
import bisect

class Solution:
    def findMedian(self, matrix):
        n = len(matrix)
        m = len(matrix[0])

        low = min(row[0] for row in matrix)
        high = max(row[-1] for row in matrix)

        required = (n * m + 1) // 2

        while low < high:
            mid = (low + high) // 2

            count = 0
            for row in matrix:
                count += bisect.bisect_right(row, mid)

            if count < required:
                low = mid + 1
            else:
                high = mid

        return low
```

### Test Cases

Input: [[1,4,9],[2,5,6],[3,7,8]]
Output: 5

Input: [[1,3,8],[2,3,4],[1,2,5]]
Output: 3

### Now Your Turn

Input: [[1,4,15],[2,5,6],[3,8,11]]
Output: 5

### Complexity

Time: O(log(MaxValue) × N × log M)
Space: O(1)

---

## 3) Single Element in Sorted Array

**TUF Problem:** Single Element in Sorted Array

### Problem Statement

Given a sorted array where every element appears exactly twice except one element, find the element that appears only once.

### What Striver Discussed

* Use Binary Search instead of a linear scan.
* Before the single element, pairs start at even indices.
* After the single element, the pairing pattern shifts.
* Use index parity and neighboring elements to determine which side contains the answer.

### Clean Python Solution

```python
class Solution:
    def singleNonDuplicate(self, nums):
        n = len(nums)

        if n == 1:
            return nums[0]

        if nums[0] != nums[1]:
            return nums[0]

        if nums[n - 1] != nums[n - 2]:
            return nums[n - 1]

        low, high = 1, n - 2

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] != nums[mid - 1] and nums[mid] != nums[mid + 1]:
                return nums[mid]

            if (mid % 2 == 1 and nums[mid] == nums[mid - 1]) or \
               (mid % 2 == 0 and nums[mid] == nums[mid + 1]):
                low = mid + 1
            else:
                high = mid - 1

        return -1
```

### Test Cases

Input: [1,1,2,2,3,3,4,5,5,6,6]
Output: 4

Input: [1,1,3,5,5]
Output: 3

### Now Your Turn

Input: [1,1,2,2,3,3,4,4,5,5,6,6,7]
Output: 7

### Complexity

Time: O(log n) - Binary Search halves the search space at each step
Space: O(1)

---

## Key Learnings From Today

### Find Nth Root of a Number

* Binary Search can be applied on the answer space rather than array indices.
* Early stopping during power computation improves efficiency.
* Integer roots can be found without using floating-point operations.

### Matrix Median

* Binary Search on values is useful when direct indexing is difficult.
* Counting elements less than or equal to a value helps locate the median.
* bisect_right acts as an efficient upper bound operation in Python.

### Single Element in Sorted Array

* Observing index parity reveals the location of the unique element.
* Pair patterns before and after the single element are different.
* Binary Search reduces the complexity from O(n) to O(log n).
