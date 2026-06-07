# #45DaysSDEChallenge - Day 7

**Date:** June 7, 2026  
**Problems Solved Today:** 3  
**Sheet:** [Striver SDE Sheet](https://takeuforward.org/dsa/strivers-sde-sheet-top-coding-interview-problems)

---

## 1) Longest Consecutive Sequence

- **TUF Problem:** [Longest Consecutive Sequence](https://takeuforward.org/plus/dsa/problems/longest-consecutive-sequence-in-an-array)
- **LeetCode:** [Longest Consecutive Sequence (LC 128)](https://leetcode.com/problems/longest-consecutive-sequence/)
- **Striver Video:** [Watch](https://youtu.be/oO5uLE7EUlM)

### Problem Statement
Given an array `nums` of `n` integers, return the length of the longest sequence of consecutive integers.

The integers in the sequence can appear in any order.

### What Striver Discussed
- Brute force: For every element, repeatedly search for the next consecutive number. This can go up to O(n^2).
- Better approach: Sort the array and count consecutive runs. This takes O(n log n).
- Optimal approach (used): Store all unique numbers in a hash set.
  1. Start counting only from numbers that do not have `num - 1` in the set.
  2. Keep moving forward while `current + 1` exists.
  3. Track the maximum sequence length found.

### Clean Python Solution
```python
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0

        for num in num_set:
            if num - 1 not in num_set:
                current = num
                length = 1

                while current + 1 in num_set:
                    current += 1
                    length += 1

                longest = max(longest, length)

        return longest
```

### Test Cases
- **Input:** `nums = [100, 4, 200, 1, 3, 2]`
  - **Output:** `4`
  - **Explanation:** Longest consecutive sequence is `[1, 2, 3, 4]`

- **Input:** `nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]`
  - **Output:** `9`

- **Now Your Turn:** `nums = [1, 9, 3, 10, 4, 20, 2]`
  - **Output:** `4`
  - **Sequence:** `[1, 2, 3, 4]`

### Complexity
- **Time:** O(n) - Each number is processed at most once
- **Space:** O(n) - Hash set stores unique numbers

---

## 2) Two Sum

- **TUF Problem:** [Two Sum](https://takeuforward.org/plus/dsa/problems/two-sum)
- **LeetCode:** [Two Sum (LC 1)](https://leetcode.com/problems/two-sum/)
- **Striver Video:** [Watch](https://youtu.be/UXDSeD9mN-k)

### Problem Statement
Given an array of integers `nums` and an integer `target`, return the 0-indexed indices of two elements such that they add up to `target`.

Each input has exactly one solution, and the same element cannot be used twice.

### What Striver Discussed
- Brute force: Check every pair. O(n^2) time.
- Better approach: Sort with original indices and use two pointers. O(n log n) time.
- Optimal approach: Use a hash map to store previously seen values and their indices in one pass.

### Clean Python Solution
```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for index, num in enumerate(nums):
            complement = target - num

            if complement in seen:
                return [seen[complement], index]

            seen[num] = index

        return [-1, -1]
```

### Test Cases
- **Input:** `nums = [1, 6, 2, 10, 3], target = 7`
  - **Output:** `[0, 1]`

- **Input:** `nums = [1, 3, 5, -7, 6, -3], target = 0`
  - **Output:** `[1, 5]`

- **Now Your Turn:** `nums = [-6, 7, 1, -7, 6, 2], target = 3`
  - **Output:** `[2, 5]`
  - **Explanation:** `nums[2] + nums[5] = 1 + 2 = 3`

### Complexity
- **Time:** O(n) - Single pass through the array
- **Space:** O(n) - Hash map stores seen elements

---

## 3) 4 Sum

- **TUF Problem:** [4 Sum](https://takeuforward.org/plus/dsa/problems/4-sum)
- **LeetCode:** [4Sum (LC 18)](https://leetcode.com/problems/4sum/)
- **Striver Video:** [Watch](https://youtu.be/eD33BUitrHE)

### Problem Statement
Given an integer array `nums` and an integer `target`, return all unique quadruplets `[nums[a], nums[b], nums[c], nums[d]]` such that:
- `a`, `b`, `c`, and `d` are distinct indices
- `nums[a] + nums[b] + nums[c] + nums[d] == target`

The solution set must not contain duplicate quadruplets.

### What Striver Discussed
- Brute force: Generate all quadruplets. O(n^4) time.
- Better approach: Use three loops and a hash set for the fourth number. O(n^3) time.
- Optimal approach (used): Sort the array, fix two numbers, then use two pointers for the remaining two.
  1. Sort `nums`.
  2. Fix `i` and `j`.
  3. Use `left` and `right` pointers to find pairs that complete the target.
  4. Skip duplicates for all fixed and pointer positions.

### Clean Python Solution
```python
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = []

        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            for j in range(i + 1, n):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                left = j + 1
                right = n - 1

                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]

                    if total == target:
                        ans.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                        right -= 1

                        while left < right and nums[left] == nums[left - 1]:
                            left += 1

                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
                    elif total < target:
                        left += 1
                    else:
                        right -= 1

        return ans
```

### Test Cases
- **Input:** `nums = [1, -2, 3, 5, 7, 9], target = 7`
  - **Output:** `[[-2, 1, 3, 5]]`

- **Input:** `nums = [7, -7, 1, 2, 14, 3], target = 9`
  - **Output:** `[]`

- **Now Your Turn:** `nums = [1, 1, 3, 4, -3], target = 5`
  - **Output:** `[[-3, 1, 3, 4]]`

### Complexity
- **Time:** O(n^3) - Two loops plus two-pointer traversal
- **Space:** O(1) - Ignoring output space

---

## Key Learnings From Today

### Longest Consecutive Sequence
- Hash sets are powerful when the problem asks for fast existence checks.
- Starting only from sequence beginnings avoids repeated counting.
- The optimal solution is linear because each element is visited in a controlled way.

### Two Sum
- A hash map can turn pair searching into a one-pass solution.
- Store indices, not just values, because the problem asks for positions.
- Checking the complement before inserting the current number prevents reusing the same element.

### 4 Sum
- Sorting makes duplicate handling and two-pointer movement much easier.
- Fixing two values reduces the problem into a classic two-sum search.
- Duplicate skipping is essential for returning a clean unique answer set.
