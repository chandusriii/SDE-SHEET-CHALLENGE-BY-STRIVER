# #45DaysSDEChallenge - Day 18

**Date:** June 18, 2026  
**Problems Solved Today:** 3  
**Sheet:** [Striver SDE Sheet](https://takeuforward.org/dsa/strivers-sde-sheet-top-coding-interview-problems)

---

## 1) Combination Sum II

- **TUF Problem:** [Combination Sum II](https://takeuforward.org/plus/dsa/problems/combination-sum-ii)
- **Striver Video:** [Combination Sum II | Recursion](https://www.youtube.com/watch?v=G1fRTGRxXU8)
- **LeetCode:** [Combination Sum II (LC 40)](https://leetcode.com/problems/combination-sum-ii/)

### Problem Statement
Given a collection of candidate numbers and an integer `target`, return all unique combinations where the chosen numbers sum to `target`. Each number can be used only once in a combination.

### What Striver Discussed
- Sort the candidates first so duplicate values stay together.
- Use recursion to try candidates from the current index onward.
- Move to `i + 1` after choosing a number because each element can be used only once.
- Skip duplicate candidates at the same recursion level to avoid repeated combinations.
- Stop early when the current candidate is greater than the remaining target.

### Clean Python Solution
```python
class Solution:
    def combinationSum2(self, candidates, target):
        candidates.sort()
        result = []

        def backtrack(start, remaining, path):
            if remaining == 0:
                result.append(path[:])
                return

            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                if candidates[i] > remaining:
                    break

                path.append(candidates[i])
                backtrack(i + 1, remaining - candidates[i], path)
                path.pop()

        backtrack(0, target, [])
        return result
```

### Test Cases
- **Input:** `candidates = [2, 1, 2, 7, 6, 1, 5]`, `target = 8`  
  **Output:** `[[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]`

- **Input:** `candidates = [2, 5, 2, 1, 2]`, `target = 5`  
  **Output:** `[[1, 2, 2], [5]]`

- **Now Your Turn:** `candidates = [2, 1, 2]`, `target = 5`  
  **Output:** `[[1, 2, 2]]`

### Complexity
- **Time:** O(2^n * k) - Each candidate can be picked or skipped, and copying a valid combination costs `k`
- **Space:** O(n) - Recursion depth and current path storage

---

## 2) Palindrome Partitioning

- **TUF Problem:** [Palindrome partitioning](https://takeuforward.org/plus/dsa/problems/palindrome-partitioning)
- **Striver Video:** [Palindrome Partitioning | Recursion](https://www.youtube.com/watch?v=WBgsABoClE0)
- **LeetCode:** [Palindrome Partitioning (LC 131)](https://leetcode.com/problems/palindrome-partitioning/)

### Problem Statement
Given a string `s`, partition it so that every substring in the partition is a palindrome. Return all possible palindrome partitions.

### What Striver Discussed
- Try every possible substring starting from the current index.
- Only choose the substring if it is a palindrome.
- Once a valid substring is chosen, recursively partition the remaining string.
- When the start index reaches the end of the string, store the current partition.

### Clean Python Solution
```python
class Solution:
    def partition(self, s):
        result = []

        def is_palindrome(left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        def backtrack(start, path):
            if start == len(s):
                result.append(path[:])
                return

            for end in range(start, len(s)):
                if is_palindrome(start, end):
                    path.append(s[start : end + 1])
                    backtrack(end + 1, path)
                    path.pop()

        backtrack(0, [])
        return result
```

### Test Cases
- **Input:** `s = "aabaa"`  
  **Output:** `[["a", "a", "b", "a", "a"], ["a", "a", "b", "aa"], ["a", "aba", "a"], ["aa", "b", "a", "a"], ["aa", "b", "aa"], ["aabaa"]]`

- **Input:** `s = "baa"`  
  **Output:** `[["b", "a", "a"], ["b", "aa"]]`

- **Now Your Turn:** `s = "ab"`  
  **Output:** `[["a", "b"]]`

### Complexity
- **Time:** O(2^n * n) - There can be many partitions, and palindrome checks/copying add up to `n`
- **Space:** O(n) - Recursion depth and current partition storage

---

## 3) Permutation Sequence

- **TUF Problem:** [Permutation Sequence](https://takeuforward.org/plus/dsa/problems/permutation-sequence)
- **Striver Video:** [K-th Permutation Sequence](https://www.youtube.com/watch?v=wT7gcXLYoao)
- **LeetCode:** [Permutation Sequence (LC 60)](https://leetcode.com/problems/permutation-sequence/)

### Problem Statement
Given integers `n` and `k`, return the `k`th permutation sequence of the numbers `[1, 2, 3, ..., n]` in lexicographic order without generating all permutations explicitly.

### What Striver Discussed
- There are `(n - 1)!` permutations starting with each fixed first digit.
- Convert `k` to zero-based indexing to make division easier.
- Use `k // factorial` to decide which number belongs at the current position.
- Remove the chosen number and reduce the factorial for the next position.

### Clean Python Solution
```python
class Solution:
    def getPermutation(self, n, k):
        numbers = list(range(1, n + 1))

        factorial = 1
        for value in range(1, n):
            factorial *= value

        k -= 1
        result = []

        while numbers:
            index = k // factorial
            result.append(str(numbers.pop(index)))

            if not numbers:
                break

            k %= factorial
            factorial //= len(numbers)

        return "".join(result)
```

### Test Cases
- **Input:** `n = 3`, `k = 3`  
  **Output:** `"213"`

- **Input:** `n = 3`, `k = 5`  
  **Output:** `"312"`

### Complexity
- **Time:** O(n^2) - Removing from the list costs O(n) for each position
- **Space:** O(n) - The remaining numbers and result are stored

---

## Key Learnings From Today

### Combination Sum II
- Sorting helps both duplicate skipping and pruning.
- Each candidate is used once, so recursion moves to the next index after a pick.
- Skipping duplicates at the same level keeps the answer unique.

### Palindrome Partitioning
- Backtracking explores all possible partition points.
- A substring should be chosen only if it is a palindrome.
- Reaching the end of the string means one complete valid partition is ready.

### Permutation Sequence
- Factorials help jump directly to the required lexicographic block.
- Zero-based indexing makes the math cleaner.
- The sequence can be built without generating all permutations.
