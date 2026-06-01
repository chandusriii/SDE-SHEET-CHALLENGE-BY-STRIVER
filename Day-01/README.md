# #45DaysSDEChallenge - Day 1

**Date:** June 1, 2026  
**Problems Solved Today:** 3  
**Sheet:** [Striver SDE Sheet](https://takeuforward.org/dsa/strivers-sde-sheet-top-coding-interview-problems)

---

## 1) Set Matrix Zeroes

- **TUF Problem:** [Set Matrix Zeroes](https://takeuforward.org/plus/dsa/problems/set-matrix-zeroes?source=strivers-sde-sheet)
- **LeetCode:** [Set Matrix Zeroes (LC 73)](https://leetcode.com/problems/set-matrix-zeroes/)
- **Striver Video:** [Watch](https://youtu.be/N0MgLvceX7M?si=8TtQ3DhMW4rDTN6O)

### What Striver Discussed
- Brute force: For every `0`, mark full row and column using extra marker arrays.
- Better approach: Use separate row and column arrays to remember which rows/cols should become zero.
- Optimal approach (used): Use first row and first column as markers and one extra variable (`col0`) to handle first column safely. This gives constant extra space.

### Complexity
- **Time:** O(m*n)  
- **Space:** O(1)

---

## 2) Pascal's Triangle I

- **TUF Problem:** [Pascal's Triangle I](https://takeuforward.org/data-structure/program-to-generate-pascals-triangle)
- **LeetCode (closest):** [Pascal's Triangle (LC 118)](https://leetcode.com/problems/pascals-triangle/)
- **Striver Video:** [Watch](https://youtu.be/bR7mQgwQ_o8?si=ciAIQ27Y5Jel8DGF)

### What Striver Discussed
Striver explains 3 related Pascal Triangle patterns:
- Find element at `(r, c)`
- Print nth row
- Generate full triangle

For finding one element, he uses:
- Optimal formula: `nCr`, where value at `(r, c)` is `(r-1)C(c-1)`, computed iteratively without factorials.

### Complexity
- **Time:** O(c)  
- **Space:** O(1)

---

## 3) Next Permutation

- **TUF Problem:** [Next Permutation](https://takeuforward.org/plus/dsa/problems/next-permutation?source=strivers-sde-sheet)
- **LeetCode:** [Next Permutation (LC 31)](https://leetcode.com/problems/next-permutation/)
- **Striver Video:** [Watch](https://youtu.be/JDOXKqF60RQ?si=L_qjgvaDEVuEjYNb)

### What Striver Discussed
- Brute force: Generate all permutations, sort them, find current, then take next. Very expensive.
- Optimal approach (used):
  1. Find breakpoint from right where `nums[i] < nums[i+1]`
  2. If no breakpoint, reverse full array
  3. Find smallest greater element on right side and swap
  4. Reverse suffix to get next lexicographically smallest arrangement

### Complexity
- **Time:** O(n)  
- **Space:** O(1)

---

## Key Learnings From Today

1. **Set Matrix Zeroes**
   - Learned how to reduce space from O(m+n) to O(1) by using matrix first row/first column as markers.
   - Important edge case: first column must be tracked separately (`col0`).

2. **Pascal's Triangle I**
   - Understood direct mathematical computation using nCr instead of building full triangle.
   - Iterative multiplication/division avoids factorial overhead.

3. **Next Permutation**
   - Learned lexicographic permutation logic: find breakpoint, swap with next greater from right, reverse suffix.
   - This pattern is useful in many array rearrangement problems.
