# #45DaysSDEChallenge - Day 16

**Date:** June 16, 2026  
**Problems Solved Today:** 3  
**Sheet:** [Striver SDE Sheet](https://takeuforward.org/dsa/strivers-sde-sheet-top-coding-interview-problems)

---

## 1) Fractional Knapsack

- **TUF Problem:** [Fractional Knapsack](https://takeuforward.org/plus/dsa/problems/fractional-knapsack)
- **Striver Video:** [Fractional Knapsack | Greedy Algorithms](https://www.youtube.com/watch?v=F_DDzYnxO14)
- **LeetCode:** No direct LeetCode equivalent for the fractional version

### Problem Statement
Given `n` items where each item has a value and weight, and a knapsack with limited capacity, return the maximum total value that can be placed in the knapsack. Any fraction of an item can be taken.

### What Striver Discussed
- Since fractions are allowed, choose items by maximum value per unit weight.
- Store each item with its value-to-weight ratio.
- Sort items by ratio in descending order.
- Take full items while possible, then take the required fraction of the next best item.

### Clean Python Solution
```python
class Solution:
    def fractionalKnapsack(self, val, wt, capacity):
        n = len(val)
        items = []

        for i in range(n):
            items.append((val[i] / wt[i], val[i], wt[i]))

        items.sort(reverse=True)

        total_value = 0.0
        current_weight = 0

        for ratio, value, weight in items:
            if current_weight + weight <= capacity:
                current_weight += weight
                total_value += value
            else:
                remaining = capacity - current_weight
                total_value += ratio * remaining
                break

        return round(total_value, 6)
```

### Test Cases
- **Input:** `val = [60, 100, 120]`, `wt = [10, 20, 30]`, `capacity = 50`  
  **Output:** `240.000000`

- **Input:** `val = [60, 100]`, `wt = [10, 20]`, `capacity = 50`  
  **Output:** `160.000000`

### Complexity
- **Time:** O(n log n) - Items are sorted by value-to-weight ratio
- **Space:** O(n) - Ratio, value, and weight are stored for each item

---

## 2) Minimum Coins

- **TUF Problem:** [Minimum coins](https://takeuforward.org/plus/dsa/problems/minimum-coins)
- **Striver Video:** [Minimum Coins | DP on Subsequences](https://www.youtube.com/watch?v=myPeWb3Y68A)
- **LeetCode:** [Coin Change (LC 322)](https://leetcode.com/problems/coin-change/)

### Problem Statement
Given coin denominations and an amount, return the minimum number of coins needed to make that amount. If the amount cannot be formed, return `-1`. Each denomination can be used unlimited times.

### What Striver Discussed
- This is an unbounded knapsack style dynamic programming problem.
- At each coin, either do not take it or take it if it fits in the current target.
- Taking a coin keeps us on the same index because coins can be reused.
- Space can be optimized by keeping only previous and current rows.

### Clean Python Solution
```python
class Solution:
    def MinimumCoins(self, coins, amount):
        n = len(coins)
        INF = int(1e9)

        prev = [0] * (amount + 1)
        cur = [0] * (amount + 1)

        for target in range(amount + 1):
            if target % coins[0] == 0:
                prev[target] = target // coins[0]
            else:
                prev[target] = INF

        for ind in range(1, n):
            for target in range(amount + 1):
                notTake = prev[target]

                take = INF
                if coins[ind] <= target:
                    take = 1 + cur[target - coins[ind]]

                cur[target] = min(notTake, take)

            prev = cur[:]

        return -1 if prev[amount] >= INF else prev[amount]
```

### Test Cases
- **Input:** `coins = [1, 2, 5]`, `amount = 11`  
  **Output:** `3`

- **Input:** `coins = [2, 5]`, `amount = 3`  
  **Output:** `-1`

- **Now Your Turn:** `coins = [10]`, `amount = 5`  
  **Output:** `-1`

### Complexity
- **Time:** O(n * amount) - Every coin is checked for every target amount
- **Space:** O(amount) - Two one-dimensional DP arrays are used

---

## 3) Assign Cookies

- **TUF Problem:** [Assign Cookies](https://takeuforward.org/plus/dsa/problems/assign-cookies)
- **Striver Video:** [Assign Cookies | Greedy Algorithm Playlist](https://www.youtube.com/watch?v=DIX2p7vb9co)
- **LeetCode:** [Assign Cookies (LC 455)](https://leetcode.com/problems/assign-cookies/)

### Problem Statement
Given students' minimum cookie-size requirements and available cookie sizes, assign at most one cookie to each student and maximize the number of satisfied students.

### What Striver Discussed
- Sort both students and cookies.
- Try to satisfy the least demanding student first.
- Use the smallest cookie that can satisfy the current student.
- If a cookie is too small, move to the next cookie.

### Clean Python Solution
```python
class Solution:
    def findMaximumCookieStudents(self, Student, Cookie):
        Student.sort()
        Cookie.sort()

        i = 0
        j = 0

        while i < len(Student) and j < len(Cookie):
            if Cookie[j] >= Student[i]:
                i += 1
            j += 1

        return i
```

### Test Cases
- **Input:** `student = [1, 2, 3]`, `cookie = [1, 1]`  
  **Output:** `1`

- **Input:** `student = [1, 2]`, `cookie = [1, 2, 3]`  
  **Output:** `2`

- **Now Your Turn:** `student = [4, 5, 1]`, `cookie = [6, 4, 2]`  
  **Output:** `3`

### Complexity
- **Time:** O(n log n + m log m) - Both arrays are sorted
- **Space:** O(1) - Apart from sorting, only two pointers are used

---

## Key Learnings From Today

### Fractional Knapsack
- Value-to-weight ratio is the greedy sorting key.
- Fractional selection makes the greedy approach optimal.
- The last chosen item may be taken partially.

### Minimum Coins
- Greedy does not always work for arbitrary coin denominations.
- Dynamic programming handles the reusable coin choice correctly.
- Space optimization reduces the DP table to one-dimensional arrays.

### Assign Cookies
- Sorting both arrays makes the matching process simple.
- Satisfying smaller requirements first maximizes the final count.
- Two pointers are enough to build the greedy matching.

