# #45DaysSDEChallenge - Day 6

**Date:** June 6, 2026  
**Problems Solved Today:** 3  
**Sheet:** [Striver SDE Sheet](https://takeuforward.org/dsa/strivers-sde-sheet-top-coding-interview-problems)

---

## 1) Reverse Pairs

- **TUF Problem:** [Reverse Pairs](https://takeuforward.org/plus/dsa/problems/reverse-pairs?source=strivers-sde-sheet)
- **LeetCode:** [Reverse Pairs (LC 493)](https://leetcode.com/problems/reverse-pairs/)
- **Striver Video:** [Watch](https://youtu.be/7_ZvBFSqkKU?si=7_ZvBFSqkKU)

### Problem Statement
Given an integer array `nums`, return the number of reverse pairs in the array.

An index pair `(i, j)` is called a reverse pair if:
- `0 <= i < j < nums.length`
- `nums[i] > 2 * nums[j]`

### What Striver Discussed
- Brute force: Check all pairs and count those satisfying the condition. O(n²) approach.
- Better approach: Use sorting and binary search, but this doesn't maintain original order during modification.
- Optimal approach (used): Modified Merge Sort.
  1. During merge sort, while merging, count pairs where `nums[i] > 2 * nums[j]`.
  2. Use a two-pointer technique to efficiently count valid pairs without nested loops.
  3. The key insight: as we move from left to right in the left half, we move right pointer in the right half.

### Clean Python Solution
```python
class Solution:
    def merge(self, arr, low, mid, high):
        temp = []
        left = low
        right = mid + 1

        while left <= mid and right <= high:
            if arr[left] <= arr[right]:
                temp.append(arr[left])
                left += 1
            else:
                temp.append(arr[right])
                right += 1

        while left <= mid:
            temp.append(arr[left])
            left += 1

        while right <= high:
            temp.append(arr[right])
            right += 1

        for i in range(low, high + 1):
            arr[i] = temp[i - low]

    def countPairs(self, arr, low, mid, high):
        right = mid + 1
        cnt = 0

        for i in range(low, mid + 1):
            while right <= high and arr[i] > 2 * arr[right]:
                right += 1
            cnt += right - (mid + 1)

        return cnt

    def mergeSort(self, arr, low, high):
        if low >= high:
            return 0

        mid = (low + high) // 2

        cnt = self.mergeSort(arr, low, mid)
        cnt += self.mergeSort(arr, mid + 1, high)
        cnt += self.countPairs(arr, low, mid, high)

        self.merge(arr, low, mid, high)

        return cnt

    def reversePairs(self, nums: List[int]) -> int:
        return self.mergeSort(nums, 0, len(nums) - 1)
```

### Test Cases
- **Input:** `nums = [6, 4, 1, 2, 7]`
  - **Output:** `3`
  - **Pairs:** `(0, 2)`, `(0, 3)`, `(1, 2)`

- **Input:** `nums = [5, 4, 4, 3, 3]`
  - **Output:** `0`

- **Input:** `nums = [6, 4, 4, 2, 2]`
  - **Output:** `3`
  - **Pairs:** `(0, 2)`, `(0, 3)`, `(0, 4)`

### Complexity
- **Time:** O(n log n) - Merge sort complexity
- **Space:** O(n) - Temporary array in merge operation

---

## 2) Grid Unique Paths

- **TUF Problem:** [Grid Unique Paths](https://takeuforward.org/dsa/grid-unique-paths-dp-on-grids-dp33/)
- **LeetCode:** [Unique Paths (LC 62)](https://leetcode.com/problems/unique-paths/)
- **Striver Video:** [Watch](https://youtu.be/t_kPFVTVvKs?si=t_kPFVTVvKs)

### Problem Statement
Given two integers `m` and `n`, representing the number of rows and columns of a 2D grid. Return the number of unique ways to go from the top-left cell `(0, 0)` to the bottom-right cell `(m-1, n-1)`.

Movement is allowed only in two directions: **right** and **bottom**.

### What Striver Discussed
- Brute force: Generate all possible paths recursively. Exponential time complexity.
- Better approach: Use Dynamic Programming with memoization.
- Optimal approach (used): Mathematical combination formula.
  - To reach from `(0, 0)` to `(m-1, n-1)`, we need exactly `(m-1)` down moves and `(n-1)` right moves.
  - Total moves needed: `(m-1) + (n-1) = m + n - 2`
  - Number of unique paths = `C(m+n-2, m-1)` = `C(m+n-2, n-1)`
  - We compute this using iterative multiplication and division to avoid factorial overflow.

### Clean Python Solution
```python
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        N = m + n - 2
        r = min(m - 1, n - 1)

        result = 1
        for i in range(1, r + 1):
            result = result * (N - r + i) // i

        return result
```

### Test Cases
- **Input:** `m = 3, n = 2`
  - **Output:** `3`
  - **Paths:** `Right→Down→Down`, `Down→Right→Down`, `Down→Down→Right`

- **Input:** `m = 2, n = 4`
  - **Output:** `4`

- **Input:** `m = 3, n = 3`
  - **Output:** `6`
  - **Explanation:** Total moves = 4, need 2 downs and 2 rights = C(4,2) = 6

### Complexity
- **Time:** O(min(m-1, n-1)) - Loop runs for the smaller of the two
- **Space:** O(1) - Constant extra space

---

## 3) Majority Element II

- **TUF Problem:** [Majority Element II](https://takeuforward.org/dsa/majority-element-n-by-3/)
- **LeetCode:** [Majority Element II (LC 229)](https://leetcode.com/problems/majority-element-ii/)
- **Striver Video:** [Watch](https://youtu.be/vwZj1K0e9OM?si=vwZj1K0e9OM)

### Problem Statement
Given an integer array `nums` of size `n`, return all elements which appear more than `⌊n/3⌋` times in the array.

The output can be returned in any order.

### What Striver Discussed
- Brute force: Use a hash map to count all elements. O(n) time, O(n) space.
- Better approach: Sort the array and find elements with count > n/3. O(n log n) time.
- Optimal approach (used): **Boyer-Moore Voting Algorithm** (Extended for n/3).
  - There can be at most **2 elements** that appear more than n/3 times (mathematical fact).
  - Maintain two candidate elements and their counts.
  - In first pass, identify candidates by cancelling out votes.
  - In second pass, verify if candidates actually have count > n/3.

### Clean Python Solution
```python
class Solution:
    def majorityElementTwo(self, nums: List[int]) -> List[int]:
        n = len(nums)

        cnt1, cnt2 = 0, 0
        el1, el2 = float('-inf'), float('-inf')

        # Boyer-Moore Voting Algorithm
        for num in nums:
            if cnt1 == 0 and num != el2:
                el1 = num
                cnt1 = 1
            elif cnt2 == 0 and num != el1:
                el2 = num
                cnt2 = 1
            elif num == el1:
                cnt1 += 1
            elif num == el2:
                cnt2 += 1
            else:
                cnt1 -= 1
                cnt2 -= 1

        # Verify the candidates
        cnt1, cnt2 = 0, 0
        for num in nums:
            if num == el1:
                cnt1 += 1
            if num == el2:
                cnt2 += 1

        ans = []

        if cnt1 > n // 3:
            ans.append(el1)

        if cnt2 > n // 3 and el1 != el2:
            ans.append(el2)

        ans.sort()
        return ans
```

### Test Cases
- **Input:** `nums = [1, 2, 1, 1, 3, 2]`
  - **Output:** `[1]`
  - **Explanation:** n/3 = 2, only 1 appears 3 times

- **Input:** `nums = [1, 2, 1, 1, 3, 2, 2]`
  - **Output:** `[1, 2]`
  - **Explanation:** n/3 = 2, both 1 and 2 appear 3 times

- **Input:** `nums = [1, 2, 1, 1, 3, 2, 2, 3]`
  - **Output:** `[1, 2]`
  - **Explanation:** n/3 = 2, 1 appears 3 times, 2 appears 3 times

### Complexity
- **Time:** O(n) - Two passes through the array
- **Space:** O(1) - Only storing two candidate elements

---

## Key Learnings From Today

### Reverse Pairs
- Learned how to solve a counting problem efficiently using **Modified Merge Sort**.
- The key insight: during merge, use two pointers to count pairs instead of nested loops.
- This pattern applies to many counting-based array problems.

### Grid Unique Paths
- Understood that combinatorics can replace dynamic programming for this problem.
- Learned how to compute `C(n, r)` iteratively without computing factorials.
- The formula `C(m+n-2, min(m-1, n-1))` is elegant and optimal.

### Majority Element II
- Learned the **extended Boyer-Moore Voting Algorithm** for finding elements appearing > n/k times.
- For n/3, there can be at most 2 candidates, which is the key mathematical insight.
- The algorithm cleverly uses vote cancellation to identify candidates in linear time and constant space.
