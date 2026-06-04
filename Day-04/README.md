# #45DaysSDEChallenge - Day 4

**Date:** June 4, 2026  
**Problems Solved Today:** 3  
**Sheet:** [Striver SDE Sheet](https://takeuforward.org/dsa/strivers-sde-sheet-top-coding-interview-problems)

---

## 1) Find the Duplicate Number

- **TUF Problem:** [Find the Duplicate Number](https://takeuforward.org/problems/find-the-duplicate-number)
- **LeetCode:** [Find the Duplicate Number (LC 287)](https://leetcode.com/problems/find-the-duplicate-number/)
- **Striver Video:** [Watch](https://youtu.be/wjYnzkAXYSw)

### Problem Statement
Given an array of integers `nums` containing `n + 1` integers where each integer is in the range `[1, n]` inclusive, there is only one repeated number in `nums` (but it can be repeated more than once). Return this duplicate number.

**Constraints:**
- You must not modify the array (assume it is read-only)
- You must use only constant extra space
- Your algorithm should run in less than O(n²) time

### What Striver Discussed
- **Brute force:** Use HashSet to track seen numbers - O(n) time but O(n) space.
- **Better approach:** Sort and compare adjacent elements - O(n log n) time but O(1) space.
- **Optimal approach (used):** Floyd's Cycle Detection (Tortoise & Hare).
  1. Treat the array as a linked list where `arr[i]` is the next pointer.
  2. Find the cycle intersection point using slow and fast pointers.
  3. The entrance to the cycle is the duplicate number.

### Clean Python Solution
```python
class Solution:
    def findDuplicate(self, nums):
        slow = nums[0]
        fast = nums[0]

        # Phase 1: Find intersection point
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
```

### Complexity
- **Time:** O(n)
- **Space:** O(1)

### Example
```
Input: nums = [1,3,4,2,2]
Output: 2

Input: nums = [3,1,3,4,2]
Output: 3

Input: nums = [1,1]
Output: 1
```

### Key Insight
This problem is analogous to finding the cycle start in a linked list. By treating indices as pointers and values as references, we can apply cycle detection techniques.

---

## 2) Find the Repeating and Missing Number

- **TUF Problem:** [Find the Repeating and Missing Number](https://takeuforward.org/problems/find-the-repeating-and-missing-number)
- **LeetCode:** [Find the Repeating and Missing Number](https://takeuforward.org/problems/find-the-repeating-and-missing-number)
- **Striver Video:** [Watch](https://youtu.be/2JzRBUi1nC0)

### Problem Statement
Given an integer array `nums` of size `n` containing values from `[1, n]` where each value appears exactly once, except for value `A` which appears twice and value `B` which is missing. Return the values `[A, B]` as an array of size 2.

**Constraints:**
- You are not allowed to modify the original array
- 1 ≤ n ≤ 10^5

### What Striver Discussed
- **Brute force:** Use HashSet to identify repeating and missing - O(n) time, O(n) space.
- **Better approach:** Count frequencies and compare - O(n) time, O(n) space.
- **Optimal approach (used):** Mathematical approach using Sum and Sum of Squares.
  1. Calculate expected sum: SN = n(n+1)/2
  2. Calculate expected sum of squares: S2N = n(n+1)(2n+1)/6
  3. Calculate actual sum and sum of squares
  4. Use algebra to find repeating (X) and missing (Y) numbers

### Clean Python Solution
```python
class Solution:
    def findMissingRepeatingNumbers(self, nums):
        n = len(nums)

        # Expected sum and sum of squares
        SN = n * (n + 1) // 2
        S2N = n * (n + 1) * (2 * n + 1) // 6

        # Actual sum and sum of squares
        S = sum(nums)
        S2 = sum(x * x for x in nums)

        # X - Y (repeating - missing)
        val1 = S - SN

        # X² - Y²
        val2 = S2 - S2N

        # X + Y
        val2 = val2 // val1

        # Repeating number (X)
        x = (val1 + val2) // 2

        # Missing number (Y)
        y = x - val1

        return [x, y]
```

### Complexity
- **Time:** O(n)
- **Space:** O(1)

### Example
```
Input: nums = [3, 5, 4, 1, 1]
Output: [1, 2]
Explanation: 1 appears twice, 2 is missing

Input: nums = [1, 2, 3, 6, 7, 5, 7]
Output: [7, 4]
Explanation: 7 appears twice, 4 is missing

Input: nums = [6, 5, 7, 1, 8, 6, 4, 3, 2]
Output: [6, 9]
Explanation: 6 appears twice, 9 is missing
```

### Mathematical Approach
Given:
- X - Y = S - SN (difference in sums)
- X² - Y² = S2 - S2N (difference in sum of squares)

From these: X + Y = (X² - Y²) / (X - Y)

Then: X = ((X-Y) + (X+Y)) / 2 and Y = X - (X-Y)

---

## 3) Count Inversions

- **TUF Problem:** [Count Inversions](https://takeuforward.org/problems/count-inversions)
- **LeetCode:** [Count of Smaller Numbers After Self (LC 315)](https://leetcode.com/problems/count-of-smaller-numbers-after-self/)
- **Striver Video:** [Watch](https://youtu.be/kQ1mJlwW-c0)

### Problem Statement
Given an integer array `nums`. Return the number of inversions in the array.

An inversion is formed when two elements `a[i]` and `a[j]` satisfy:
- `a[i] > a[j]` AND `i < j`

Inversions indicate how close an array is to being sorted.

### What Striver Discussed
- **Brute force:** Check all pairs with nested loops - O(n²) time.
- **Optimal approach (used):** Merge Sort with inversion counting.
  1. Divide array into halves recursively
  2. Count inversions in left half
  3. Count inversions in right half
  4. Count split inversions during merge phase
  5. When an element from right subarray is smaller than left, it forms inversions with all remaining elements in left

### Clean Python Solution
```python
class Solution:
    def merge(self, arr, low, mid, high):
        temp = []
        left = low
        right = mid + 1
        cnt = 0

        while left <= mid and right <= high:
            if arr[left] <= arr[right]:
                temp.append(arr[left])
                left += 1
            else:
                temp.append(arr[right])
                cnt += (mid - left + 1)  # Count inversions
                right += 1

        while left <= mid:
            temp.append(arr[left])
            left += 1

        while right <= high:
            temp.append(arr[right])
            right += 1

        for i in range(low, high + 1):
            arr[i] = temp[i - low]

        return cnt

    def mergeSort(self, arr, low, high):
        cnt = 0

        if low >= high:
            return cnt

        mid = (low + high) // 2

        cnt += self.mergeSort(arr, low, mid)
        cnt += self.mergeSort(arr, mid + 1, high)
        cnt += self.merge(arr, low, mid, high)

        return cnt

    def numberOfInversions(self, nums):
        return self.mergeSort(nums, 0, len(nums) - 1)
```

### Complexity
- **Time:** O(n log n)
- **Space:** O(n) for the temporary array

### Example
```
Input: nums = [2, 3, 7, 1, 3, 5]
Output: 5
Explanation:
- (2, 1) at indices (0, 3)
- (3, 1) at indices (1, 3)
- (7, 1) at indices (2, 3)
- (7, 3) at indices (2, 4)
- (7, 5) at indices (2, 5)

Input: nums = [-10, -5, 6, 11, 15, 17]
Output: 0
Explanation: Array is already sorted, no inversions

Input: nums = [9, 5, 4, 2]
Output: 6
Explanation: All pairs form inversions
```

---

## Key Learnings From Today

### Find the Duplicate Number
- Learned how to apply Floyd's Cycle Detection to array problems by treating indices as linked list pointers.
- Understood that this clever approach avoids the need for extra space while maintaining O(n) time complexity.

### Find Repeating and Missing Number
- Mastered the mathematical approach using sum and sum of squares equations.
- Realized how algebraic manipulation can reduce space complexity from O(n) to O(1).

### Count Inversions
- Discovered how Merge Sort can be adapted to count inversions during the merge phase.
- Understood that inversions are counted when an element from the right subarray is smaller than elements from the left subarray.

---

## Summary Statistics

| Problem | Time | Space | Approach | Difficulty |
|---------|------|-------|----------|------------|
| Find the Duplicate Number | O(n) | O(1) | Floyd's Cycle Detection | Medium |
| Find Repeating and Missing Number | O(n) | O(1) | Mathematical (Sum & Squares) | Medium |
| Count Inversions | O(n log n) | O(n) | Merge Sort with Counting | Hard |

---

## Progress Notes
- ✅ Successfully solved all 3 problems
- ✅ Optimized all solutions to use minimal space
- ✅ Understood advanced techniques: cycle detection, mathematical equations, merge sort optimization
- 🎯 **4 Days Completed | 41 Days Remaining**
