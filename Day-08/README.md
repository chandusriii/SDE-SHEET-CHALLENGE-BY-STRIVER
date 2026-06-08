# #45DaysSDEChallenge - Day 8

**Date:** June 8, 2026  
**Problems Solved Today:** 3  
**Sheet:** [Striver SDE Sheet](https://takeuforward.org/dsa/strivers-sde-sheet-top-coding-interview-problems)

---

## 1) Longest Subarray With Sum K

- **TUF Problem:** [Longest Subarray With Sum K](https://takeuforward.org/plus/dsa/problems/longest-subarray-with-sum-k)

### Problem Statement
Given an array `nums` of size `n` and an integer `k`, find the length of the longest subarray that sums to `k`.

If no such subarray exists, return `0`.

### What Striver Discussed
- Brute force: Check every subarray and calculate its sum. This can go up to O(n^2) or O(n^3), depending on how the sum is computed.
- Optimal approach: Use prefix sum with a hash map.
  1. Keep a running `prefix_sum`.
  2. If `prefix_sum == k`, the whole subarray from index `0` to current index is valid.
  3. Otherwise, check whether `prefix_sum - k` appeared earlier.
  4. Store only the first occurrence of each prefix sum to maximize the subarray length.

### Clean Python Solution
```python
class Solution:
    def longestSubarray(self, nums, k):
        prefix_sum = 0
        longest = 0
        first_seen = {}

        for index, num in enumerate(nums):
            prefix_sum += num

            if prefix_sum == k:
                longest = index + 1

            remaining = prefix_sum - k
            if remaining in first_seen:
                longest = max(longest, index - first_seen[remaining])

            if prefix_sum not in first_seen:
                first_seen[prefix_sum] = index

        return longest
```

### Test Cases
- **Input:** `nums = [10, 5, 2, 7, 1, 9], k = 15`
  - **Output:** `4`
  - **Explanation:** The longest valid subarray is `[5, 2, 7, 1]`

- **Input:** `nums = [-3, 2, 1], k = 6`
  - **Output:** `0`

- **Now Your Turn:** `nums = [-1, 1, 1], k = 1`
  - **Output:** `3`
  - **Explanation:** The full subarray `[-1, 1, 1]` sums to `1`

### Complexity
- **Time:** O(n) - Single pass through the array
- **Space:** O(n) - Hash map stores prefix sums

---

## 2) Count Subarrays With Given XOR K

- **TUF Problem:** [Count Subarrays With Given XOR K](https://takeuforward.org/plus/dsa/problems/count-subarrays-with-given-xor-k)

### Problem Statement
Given an array of integers `nums` and an integer `k`, return the total number of subarrays whose XOR equals `k`.

### What Striver Discussed
- Brute force: Generate every subarray and calculate XOR. This takes O(n^2).
- Optimal approach: Use prefix XOR with a hash map.
  1. Maintain the XOR from the start to the current index.
  2. If `current_xor ^ previous_xor == k`, then `previous_xor = current_xor ^ k`.
  3. Count how many times the needed previous XOR has appeared.
  4. Store frequencies of prefix XOR values.

### Clean Python Solution
```python
class Solution:
    def subarraysWithXorK(self, nums, k):
        prefix_count = {0: 1}
        current_xor = 0
        count = 0

        for num in nums:
            current_xor ^= num
            target = current_xor ^ k

            count += prefix_count.get(target, 0)
            prefix_count[current_xor] = prefix_count.get(current_xor, 0) + 1

        return count
```

### Test Cases
- **Input:** `nums = [4, 2, 2, 6, 4], k = 6`
  - **Output:** `4`

- **Input:** `nums = [5, 6, 7, 8, 9], k = 5`
  - **Output:** `2`

- **Now Your Turn:** `nums = [5, 2, 9], k = 7`
  - **Output:** `1`
  - **Explanation:** The subarray `[5, 2]` has XOR `7`

### Complexity
- **Time:** O(n) - Single pass through the array
- **Space:** O(n) - Hash map stores prefix XOR frequencies

---

## 3) Longest Substring Without Repeating Characters

- **TUF Problem:** [Longest Substring Without Repeating Characters](https://takeuforward.org/plus/dsa/problems/longest-substring-without-repeating-characters)
- **LeetCode:** [Longest Substring Without Repeating Characters (LC 3)](https://leetcode.com/problems/longest-substring-without-repeating-characters/)

### Problem Statement
Given a string `S`, find the length of the longest substring without repeating characters.

### What Striver Discussed
- Brute force: Generate all substrings and check whether each substring has duplicate characters.
- Optimal approach: Use sliding window with a hash map.
  1. Expand the right pointer character by character.
  2. If the current character was already seen inside the active window, move `left` after its previous index.
  3. Update the last seen index of the current character.
  4. Track the maximum window length.

### Clean Python Solution
```python
class Solution:
    def longestNonRepeatingSubstring(self, s):
        last_seen = {}
        left = 0
        longest = 0

        for right, char in enumerate(s):
            if char in last_seen and last_seen[char] >= left:
                left = last_seen[char] + 1

            last_seen[char] = right
            longest = max(longest, right - left + 1)

        return longest
```

### Test Cases
- **Input:** `S = "abcddabac"`
  - **Output:** `4`
  - **Explanation:** The answer is `"abcd"`

- **Input:** `S = "aaabbbccc"`
  - **Output:** `2`
  - **Explanation:** The answers include `"ab"` and `"bc"`

- **Now Your Turn:** `S = "aaaa"`
  - **Output:** `1`

### Complexity
- **Time:** O(n) - Each character is processed once
- **Space:** O(min(n, charset)) - Hash map stores last seen character positions

---

## Key Learnings From Today

### Longest Subarray With Sum K
- Prefix sums help convert subarray sum checks into fast lookups.
- Storing the earliest prefix sum index is important for maximizing length.
- This approach works even when the array contains negative numbers.

### Count Subarrays With Given XOR K
- Prefix XOR follows the same idea as prefix sum, but uses XOR properties.
- The key relation is `previous_xor = current_xor ^ k`.
- Frequency maps are useful when the task asks for count instead of longest length.

### Longest Substring Without Repeating Characters
- Sliding window is ideal for contiguous substring problems.
- The left pointer should only move forward.
- Last seen indices avoid repeatedly scanning the same characters.
