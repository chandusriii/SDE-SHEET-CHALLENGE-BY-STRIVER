# #45DaysSDEChallenge - Day 5

**Date:** June 5, 2026  
**Problems Solved Today:** 3  
**Sheet:** [Striver SDE Sheet](https://takeuforward.org/dsa/strivers-sde-sheet-top-coding-interview-problems)

---

## 1) Majority Element - I

- **TUF Problem:** [Majority Element](https://takeuforward.org/plus/data-structure/majority-element)
- **LeetCode:** [Majority Element (LC 169)](https://leetcode.com/problems/majority-element/)
- **Striver Video:** [Watch](https://youtu.be/AoX3ErZn10Y)

### Problem
Given an integer array `nums` of size `n`, return the majority element (appears > n/2 times).

### Algorithm
1. Create hash map to store element frequencies
2. Count occurrences of each element
3. Return element with count > n/2

### Complexity
- **Time:** O(n) 
- **Space:** O(n)

### Examples
- Input: `[7, 0, 0, 1, 7, 7, 2, 7, 7]` → Output: `7`
- Input: `[1, 1, 1, 2, 1, 2]` → Output: `1`
- Input: `[-1, -1, -1, -1]` → Output: `-1`

---

## 2) Pow(x, n)

- **TUF Problem:** [Power Function](https://takeuforward.org/plus/dsa/problems/pow-x-n)
- **LeetCode:** [Pow(x, n) (LC 50)](https://leetcode.com/problems/powx-n/)
- **Striver Video:** [Watch](https://youtu.be/l0YC3xvbvVU)

### Problem
Implement `pow(x, n)` - calculate x raised to n. Result should have 4 decimal places.

### Algorithm (Binary Exponentiation)
1. Handle negative powers: x^(-n) = 1 / x^n
2. Use bit manipulation:
   - If n is odd: multiply result by x
   - Square x and half n
   - Continue while n > 0

**Why:** x^13 = x^(1101 binary) = x^8 * x^4 * x^1 → O(log n) instead of O(n)

### Complexity
- **Time:** O(log n)
- **Space:** O(1)

### Examples
- Input: `x=2.0, n=10` → Output: `1024.0000`
- Input: `x=2.0, n=-2` → Output: `0.2500`
- Input: `x=2.5, n=2` → Output: `6.2500`

---

## 3) Search in a 2D Matrix

- **TUF Problem:** [Search in 2D Matrix](https://takeuforward.org/plus/dsa/problems/search-in-a-2d-matrix)
- **LeetCode:** [Search a 2D Matrix (LC 74)](https://leetcode.com/problems/search-a-2d-matrix/)
- **Striver Video:** [Watch](https://youtu.be/ZYpYur0znng)

### Problem
Given a 2D matrix where:
- Each row is sorted
- First element of each row > last element of previous row
- Find if target exists

### Algorithm
Treat 2D matrix as 1D sorted array:
1. Binary search on indices 0 to m*n-1
2. Convert 1D index to 2D: `row = mid // m, col = mid % m`
3. Return True if found, False otherwise

### Complexity
- **Time:** O(log(m*n))
- **Space:** O(1)

### Examples
- Input: `mat=[[1,2,3,4],[5,6,7,8],[9,10,11,12]], target=8` → Output: `True`
- Input: `mat=[[1,2,4],[6,7,8],[9,10,34]], target=78` → Output: `False`
- Input: `mat=[[1,2,4],[6,7,8],[9,10,34]], target=7` → Output: `True`

---

## Key Learnings

1. **Majority Element:** Hash map is simple & practical (O(n) time, O(n) space)
2. **Power:** Binary exponentiation dramatically reduces complexity from O(n) to O(log n)
3. **2D Matrix:** Treating 2D as 1D with index conversion = smart optimization
