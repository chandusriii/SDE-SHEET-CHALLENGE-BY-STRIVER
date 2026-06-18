# #45DaysSDEChallenge - Day 17

**Date:** June 17, 2026  
**Problems Solved Today:** 3  
**Sheet:** [Striver SDE Sheet](https://takeuforward.org/dsa/strivers-sde-sheet-top-coding-interview-problems)

---

## 1) Subset Sum Equals to Target

- **TUF Problem:** [Subset sum equals to target](https://takeuforward.org/plus/dsa/problems/subset-sum-equals-to-target)
- **Striver Video:** [Subset Sum Equal To Target | DP on Subsequences](https://www.youtube.com/watch?v=fWX9xDmIzRI)
- **LeetCode:** No direct LeetCode equivalent

### Problem Statement
Given an array `arr` of `n` integers and an integer `target`, determine whether there is a subset of the array whose sum is exactly equal to `target`.

### What Striver Discussed
- This is a classic dynamic programming problem on subsequences.
- `dp[s]` tells whether a subset with sum `s` is possible.
- Sum `0` is always possible by choosing the empty subset.
- Iterate target sums in reverse so every array element is used at most once.

### Clean Python Solution
```python
class Solution:
    def isSubsetSum(self, arr, target):
        dp = [False] * (target + 1)
        dp[0] = True

        for num in arr:
            for current_sum in range(target, num - 1, -1):
                dp[current_sum] = dp[current_sum] or dp[current_sum - num]

        return dp[target]
```

### Test Cases
- **Input:** `arr = [1, 2, 7, 3]`, `target = 6`  
  **Output:** `True`

- **Input:** `arr = [2, 3, 5]`, `target = 6`  
  **Output:** `False`

- **Now Your Turn:** `arr = [7, 54, 4, 12, 15, 5]`, `target = 9`  
  **Output:** `True`

### Complexity
- **Time:** O(n * target) - Every element checks all reachable target sums
- **Space:** O(target) - A one-dimensional DP array is used

---

## 2) Subsets II

- **TUF Problem:** [Subsets II](https://takeuforward.org/plus/dsa/problems/subsets-ii)
- **Striver Video:** [Subsets II | Recursion](https://www.youtube.com/watch?v=RIn3gOkbhQE)
- **LeetCode:** [Subsets II (LC 90)](https://leetcode.com/problems/subsets-ii/)

### Problem Statement
Given an integer array `nums` that may contain duplicate values, return all unique subsets. Duplicate subsets must not appear in the answer.

### What Striver Discussed
- Sort the array first so duplicate values stay next to each other.
- Use backtracking to build each subset.
- At the same recursion level, skip an element if it is the same as the previous one.
- This avoids duplicate subsets while still allowing repeated values to be used when chosen from different levels.

### Clean Python Solution
```python
class Solution:
    def subsetsWithDup(self, nums):
        nums.sort()
        result = []

        def backtrack(start, subset):
            result.append(subset[:])

            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue

                subset.append(nums[i])
                backtrack(i + 1, subset)
                subset.pop()

        backtrack(0, [])
        return result
```

### Test Cases
- **Input:** `nums = [1, 2, 2]`  
  **Output:** `[[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]`

- **Input:** `nums = [1, 2]`  
  **Output:** `[[], [1], [1, 2], [2]]`

- **Now Your Turn:** `nums = [1, 3, 3]`  
  **Output:** `[[], [1], [1, 3], [1, 3, 3], [3], [3, 3]]`

### Complexity
- **Time:** O(2^n * n) - There can be up to `2^n` subsets and copying each subset costs up to `n`
- **Space:** O(n) - Recursion depth and temporary subset storage

---

## 3) Combination Sum

- **TUF Problem:** [Combination Sum](https://takeuforward.org/plus/dsa/problems/combination-sum)
- **Striver Video:** [Combination Sum | Recursion](https://www.youtube.com/watch?v=OyZFFqQtu98)
- **LeetCode:** [Combination Sum (LC 39)](https://leetcode.com/problems/combination-sum/)

### Problem Statement
Given an array of unique candidates and an integer `target`, return all unique combinations where the selected numbers sum to `target`. Each candidate can be selected unlimited times.

### What Striver Discussed
- At every index, either pick the current candidate or move to the next one.
- If a candidate is picked, stay at the same index because it can be reused.
- If the target becomes `0`, store the current combination.
- If all candidates are checked, return from recursion.

### Clean Python Solution
```python
class Solution:
    def combinationSum(self, candidates, target):
        answer = []

        def findCombination(index, remaining, combination):
            if index == len(candidates):
                if remaining == 0:
                    answer.append(combination[:])
                return

            if candidates[index] <= remaining:
                combination.append(candidates[index])
                findCombination(index, remaining - candidates[index], combination)
                combination.pop()

            findCombination(index + 1, remaining, combination)

        findCombination(0, target, [])
        return answer
```

### Test Cases
- **Input:** `candidates = [2, 3, 5, 4]`, `target = 7`  
  **Output:** `[[2, 2, 3], [2, 5], [3, 4]]`

- **Input:** `candidates = [2]`, `target = 1`  
  **Output:** `[]`

- **Now Your Turn:** `candidates = [3, 4, 5, 6]`, `target = 10`  
  **Output:** `[[3, 3, 4], [4, 6], [5, 5]]`

### Complexity
- **Time:** O(2^target * k) - Recursive combinations depend on target and candidates; copying a valid combination costs `k`
- **Space:** O(target) - Recursion depth can grow with repeated picks

---

## Key Learnings From Today

### Subset Sum Equals to Target
- A boolean DP array can track all possible subset sums.
- Reverse iteration prevents using the same element more than once.
- The answer is stored directly at `dp[target]`.

### Subsets II
- Sorting is the key step for handling duplicate values cleanly.
- Skipping duplicates at the same recursion level prevents repeated subsets.
- Backtracking naturally builds the complete power set.

### Combination Sum
- Staying at the same index allows unlimited reuse of a candidate.
- Moving to the next index explores combinations without reordering duplicates.
- Recursion cleanly models the pick and not-pick choices.
