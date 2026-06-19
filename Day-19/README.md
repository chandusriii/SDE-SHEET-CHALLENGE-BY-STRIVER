# #45DaysSDEChallenge - Day 19

**Date:** June 19, 2026  
**Problems Solved Today:** 3  
**Sheet:** [Striver SDE Sheet](https://takeuforward.org/dsa/strivers-sde-sheet-top-coding-interview-problems)

---

## 1) Permutations of a String

- **TUF Problem:** [Permutations of a String](https://takeuforward.org/plus/dsa/problems/permutations-of-a-string)
- **Striver Video:** [Print All Permutations of a String/Array | Recursion](https://www.youtube.com/watch?v=f2ic2Rsc9pU)
- **LeetCode:** [Permutations II (LC 47)](https://leetcode.com/problems/permutations-ii/)

### Problem Statement
Given a string `s`, return all unique permutations of its characters in lexicographic order. If duplicate characters exist, every unique permutation should appear only once.

### What Striver Discussed
- Sort the characters first so permutations are generated in lexicographic order.
- Use a `used` array to track which characters are already part of the current permutation.
- Skip a duplicate character if the previous identical character has not been used in the current branch.
- Store the permutation once its length becomes equal to the input string length.

### Clean Python Solution
```python
class Solution:
    def permuteUnique(self, s):
        chars = sorted(s)
        used = [False] * len(chars)
        result = []

        def backtrack(current):
            if len(current) == len(chars):
                result.append("".join(current))
                return

            for i in range(len(chars)):
                if used[i]:
                    continue

                if i > 0 and chars[i] == chars[i - 1] and not used[i - 1]:
                    continue

                used[i] = True
                current.append(chars[i])

                backtrack(current)

                current.pop()
                used[i] = False

        backtrack([])
        return result
```

### Test Cases
- **Input:** `s = "abc"`  
  **Output:** `["abc", "acb", "bac", "bca", "cab", "cba"]`

- **Input:** `s = "aab"`  
  **Output:** `["aab", "aba", "baa"]`

- **Now Your Turn:** `s = "aa"`  
  **Output:** `["aa"]`

### Complexity
- **Time:** O(n! * n) - There can be up to `n!` permutations and each permutation costs `n` to build
- **Space:** O(n) - Recursion depth, used array, and current permutation storage

---

## 2) N Queen

- **TUF Problem:** [N Queen](https://takeuforward.org/plus/dsa/problems/n-queen)
- **Striver Video:** [N Queen Problem | Recursion and Backtracking](https://www.youtube.com/watch?v=i05Ju7AftcM)
- **LeetCode:** [N-Queens (LC 51)](https://leetcode.com/problems/n-queens/)

### Problem Statement
Given an integer `n`, return every unique way to place `n` queens on an `n x n` chessboard so that no two queens attack each other.

### What Striver Discussed
- Place queens column by column.
- Track used rows, diagonals, and anti-diagonals to check safety in O(1).
- `row + col` identifies one diagonal direction.
- `n - 1 + col - row` identifies the other diagonal direction.
- Backtrack after every recursive call so the next placement can be explored.

### Clean Python Solution
```python
class Solution:
    def solveNQueens(self, n):
        ans = []
        board = [["." for _ in range(n)] for _ in range(n)]

        left_row = [0] * n
        lower_diagonal = [0] * (2 * n - 1)
        upper_diagonal = [0] * (2 * n - 1)

        def solve(col):
            if col == n:
                ans.append(["".join(row) for row in board])
                return

            for row in range(n):
                if (
                    left_row[row] == 0
                    and lower_diagonal[row + col] == 0
                    and upper_diagonal[n - 1 + col - row] == 0
                ):
                    board[row][col] = "Q"
                    left_row[row] = 1
                    lower_diagonal[row + col] = 1
                    upper_diagonal[n - 1 + col - row] = 1

                    solve(col + 1)

                    board[row][col] = "."
                    left_row[row] = 0
                    lower_diagonal[row + col] = 0
                    upper_diagonal[n - 1 + col - row] = 0

        solve(0)
        return ans if ans else [[]]
```

### Test Cases
- **Input:** `n = 4`  
  **Output:** `[["..Q.", "Q...", "...Q", ".Q.."], [".Q..", "...Q", "Q...", "..Q."]]`

- **Input:** `n = 2`  
  **Output:** `[[]]`

- **Now Your Turn:** `n = 1`  
  **Output:** `[["Q"]]`

### Complexity
- **Time:** O(n!) - Backtracking explores possible queen placements column by column
- **Space:** O(n^2) - Board storage plus row and diagonal tracking arrays

---

## 3) Sudoku Solver

- **TUF Problem:** [Sudoku Solver](https://takeuforward.org/plus/dsa/problems/sudoku-solver)
- **Striver Video:** [Sudoku Solver | Recursion and Backtracking](https://www.youtube.com/watch?v=FWAIf_EVUKE)
- **LeetCode:** [Sudoku Solver (LC 37)](https://leetcode.com/problems/sudoku-solver/)

### Problem Statement
Given a partially filled `9 x 9` Sudoku board, fill the empty cells so that every row, column, and `3 x 3` sub-box contains the digits `1` to `9` exactly once.

### What Striver Discussed
- Find the first empty cell.
- Try digits `1` through `9`.
- A digit is valid only if it does not already exist in the same row, column, or box.
- Recursively solve the remaining board after placing a valid digit.
- If the recursive path fails, reset the cell and try the next digit.

### Clean Python Solution
```python
class Solution:
    def isValid(self, board, row, col, ch):
        for i in range(9):
            if board[row][i] == ch:
                return False

            if board[i][col] == ch:
                return False

            box_row = 3 * (row // 3) + i // 3
            box_col = 3 * (col // 3) + i % 3
            if board[box_row][box_col] == ch:
                return False

        return True

    def solve(self, board):
        for row in range(9):
            for col in range(9):
                if board[row][col] == ".":
                    for ch in "123456789":
                        if self.isValid(board, row, col, ch):
                            board[row][col] = ch

                            if self.solve(board):
                                return True

                            board[row][col] = "."

                    return False

        return True

    def solveSudoku(self, board):
        self.solve(board)
```

### Test Case
- **Input:** Standard partially filled Sudoku board from the driver file  
  **Output:** Completed valid Sudoku board

### Complexity
- **Time:** O(9^(empty cells)) - Each empty cell may try up to 9 digits
- **Space:** O(empty cells) - Recursion depth depends on the number of empty cells

---

## Key Learnings From Today

### Permutations of a String
- Sorting keeps generated permutations lexicographic.
- The duplicate-skip condition avoids repeated permutations.
- A `used` array makes character selection clear and controlled.

### N Queen
- Row and diagonal arrays reduce safety checks to O(1).
- Column-wise placement avoids placing more than one queen in a column.
- Backtracking cleanly explores and removes queen placements.

### Sudoku Solver
- Sudoku can be solved as a constraint-based backtracking problem.
- Row, column, and box validation decide whether a digit can be placed.
- Resetting cells during backtracking restores the board for other possibilities.
