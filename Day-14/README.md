# #45DaysSDEChallenge - Day 14

**Date:** June 14, 2026  
**Problems Solved Today:** 3  
**Sheet:** [Striver SDE Sheet](https://takeuforward.org/dsa/strivers-sde-sheet-top-coding-interview-problems)

---

## 1) Trapping Rainwater

- **TUF Problem:** [Trapping Rainwater](https://takeuforward.org/plus/dsa/problems/trapping-rainwater)

### Problem Statement
Given an array `height` of non-negative integers representing ground elevation, calculate how much water can be trapped after rain.

### What Striver Discussed
- Water above any index depends on the smaller of the highest wall on the left and the highest wall on the right.
- Instead of storing prefix and suffix maximum arrays, use two pointers.
- Move the pointer with the smaller current height because that side decides the water level.
- Track `max_left` and `max_right` while shrinking the search space.

### Clean Python Solution
```python
class Solution:
    def trap(self, height):
        n = len(height)
        left = 0
        right = n - 1
        max_left = 0
        max_right = 0
        total_water = 0

        while left <= right:
            if height[left] <= height[right]:
                if height[left] >= max_left:
                    max_left = height[left]
                else:
                    total_water += max_left - height[left]
                left += 1
            else:
                if height[right] >= max_right:
                    max_right = height[right]
                else:
                    total_water += max_right - height[right]
                right -= 1

        return total_water
```

### Test Cases
- **Input:** `height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]`  
  **Output:** `6`

- **Input:** `height = [4, 2, 0, 3, 2, 5]`  
  **Output:** `9`

- **Now Your Turn:** `height = [7, 4, 0, 9]`  
  **Output:** `10`

### Complexity
- **Time:** O(n) - Each index is processed once
- **Space:** O(1) - Only pointers and maximum values are used

---

## 2) Remove Duplicates from Sorted Array

- **TUF Problem:** [Remove duplicates from sorted array](https://takeuforward.org/plus/dsa/problems/remove-duplicates-from-sorted-array)

### Problem Statement
Given a sorted array `nums`, remove duplicates in-place so each unique element appears only once. Return the number of unique elements.

### What Striver Discussed
- Since the array is sorted, equal values appear together.
- Keep one pointer at the position of the last unique element.
- Scan the array with another pointer.
- Whenever a new value is found, move it to the next unique position.

### Clean Python Solution
```python
class Solution:
    def removeDuplicates(self, nums):
        if len(nums) == 0:
            return 0

        i = 0

        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]

        return i + 1
```

### Test Cases
- **Input:** `nums = [0, 0, 3, 3, 5, 6]`  
  **Output:** `4`  
  **Resulting array:** `[0, 3, 5, 6, _, _]`

- **Input:** `nums = [-2, 2, 4, 4, 4, 4, 5, 5]`  
  **Output:** `4`  
  **Resulting array:** `[-2, 2, 4, 5, _, _, _, _]`

- **Now Your Turn:** `nums = [-30, -30, 0, 0, 10, 20, 30, 30]`  
  **Output:** `5`  
  **Resulting array:** `[-30, 0, 10, 20, 30, _, _, _]`

### Complexity
- **Time:** O(n) - One pass through the array
- **Space:** O(1) - Changes are made in-place

---

## 3) Maximum Consecutive Ones

- **TUF Problem:** [Maximum Consecutive Ones](https://takeuforward.org/plus/dsa/problems/maximum-consecutive-ones)

### Problem Statement
Given a binary array `nums`, return the maximum number of consecutive `1`s in the array.

### What Striver Discussed
- Maintain a running count of consecutive ones.
- Increase the count when the current number is `1`.
- Reset the count to zero when the current number is `0`.
- Track the maximum count seen so far.

### Clean Python Solution
```python
class Solution:
    def findMaxConsecutiveOnes(self, nums):
        count = 0
        maximum = 0

        for num in nums:
            if num == 1:
                count += 1
                maximum = max(maximum, count)
            else:
                count = 0

        return maximum
```

### Test Cases
- **Input:** `nums = [1, 1, 0, 0, 1, 1, 1, 0]`  
  **Output:** `3`

- **Input:** `nums = [0, 0, 0, 0, 0, 0, 0, 0]`  
  **Output:** `0`

- **Now Your Turn:** `nums = [1, 0, 1, 1, 1, 0, 1, 1, 1]`  
  **Output:** `3`

### Complexity
- **Time:** O(n) - Each element is visited once
- **Space:** O(1) - Only counters are used

---

## Key Learnings From Today

### Trapping Rainwater
- The water trapped at a position depends on the smaller side boundary.
- Two pointers avoid extra prefix and suffix arrays.
- Updating the side with the smaller height keeps the calculation valid.

### Remove Duplicates from Sorted Array
- Sorted order allows duplicate detection by comparing with the last unique value.
- The first `k` positions are the only part of the array that matters.
- Two pointers are enough to solve the problem in-place.

### Maximum Consecutive Ones
- A running counter captures the current streak.
- A zero breaks the streak and resets the counter.
- Tracking the maximum during traversal keeps the solution simple and linear.
