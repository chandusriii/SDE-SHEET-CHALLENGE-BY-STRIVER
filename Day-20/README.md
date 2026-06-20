# #45DaysSDEChallenge - Day 20

**Date:** June 20, 2026  
**Problems Solved Today:** 3  
**Sheet:** [Striver SDE Sheet](https://takeuforward.org/dsa/strivers-sde-sheet-top-coding-interview-problems)

---

## 1) M Coloring Problem

- **TUF Problem:** [M Coloring Problem](https://takeuforward.org/plus/dsa/problems/m-coloring-problem)
- **Striver Video:** [M Coloring Problem | Recursion and Backtracking](https://www.youtube.com/watch?v=wuVwUK25Rfc)
- **LeetCode:** No direct LeetCode equivalent

### Problem Statement
Given an undirected graph with `n` vertices and an integer `m`, determine whether the graph can be colored using at most `m` colors so that no two adjacent vertices have the same color.

### What Striver Discussed
- Try coloring one node at a time.
- For every node, test all colors from `1` to `m`.
- A color is safe only if no adjacent node already has that color.
- If a color choice leads to a dead end, reset it and try the next color.
- If all nodes are colored successfully, return `True`.

### Clean Python Solution
```python
class Solution:
    def isSafe(self, node, color, graph, n, col):
        for neighbour in range(n):
            if graph[node][neighbour] and color[neighbour] == col:
                return False
        return True

    def solve(self, node, color, graph, m, n):
        if node == n:
            return True

        for col in range(1, m + 1):
            if self.isSafe(node, color, graph, n, col):
                color[node] = col

                if self.solve(node + 1, color, graph, m, n):
                    return True

                color[node] = 0

        return False

    def graphColoring(self, edges, m, n):
        graph = [[0] * n for _ in range(n)]

        for u, v in edges:
            graph[u][v] = 1
            graph[v][u] = 1

        color = [0] * n
        return self.solve(0, color, graph, m, n)
```

### Test Cases
- **Input:** `N = 4`, `M = 3`, `Edges = [(0, 1), (1, 2), (2, 3), (3, 0), (0, 2)]`  
  **Output:** `True`

- **Input:** `N = 3`, `M = 2`, `Edges = [(0, 1), (1, 2), (0, 2)]`  
  **Output:** `False`

- **Now Your Turn:** `N = 5`, `M = 3`, `Edges = [(0, 1), (1, 2), (0, 2), (2, 3), (2, 4), (3, 4)]`  
  **Output:** `True`

### Complexity
- **Time:** O(m^n) - Each node may try up to `m` colors
- **Space:** O(n^2 + n) - Adjacency matrix, color array, and recursion stack

---

## 2) Rat in a Maze

- **TUF Problem:** [Rat in a Maze](https://takeuforward.org/plus/dsa/problems/rat-in-a-maze)
- **Striver Video:** [Rat in a Maze | Recursion and Backtracking](https://www.youtube.com/watch?v=bLGZhJlt4y0)
- **LeetCode:** No direct LeetCode equivalent

### Problem Statement
Given an `n x n` grid, a rat starts at `(0, 0)` and must reach `(n - 1, n - 1)`. Cells with value `1` are open and cells with value `0` are blocked. Return all paths using `D`, `L`, `R`, and `U`, without visiting a cell more than once in the same path.

### What Striver Discussed
- Start from the top-left cell and recursively explore valid moves.
- Keep a `visited` matrix so the same cell is not used twice in one path.
- Try directions in lexicographic order: `D`, `L`, `R`, `U`.
- When the destination is reached, store the path string.
- Backtrack by unmarking the current cell after exploring all moves.

### Clean Python Solution
```python
class Solution:
    def findPath(self, grid):
        n = len(grid)

        if grid[0][0] == 0 or grid[n - 1][n - 1] == 0:
            return []

        visited = [[False] * n for _ in range(n)]
        ans = []

        def isSafe(x, y):
            return 0 <= x < n and 0 <= y < n and grid[x][y] == 1 and not visited[x][y]

        def solve(x, y, path):
            if x == n - 1 and y == n - 1:
                ans.append(path)
                return

            visited[x][y] = True

            for dx, dy, move in [(1, 0, "D"), (0, -1, "L"), (0, 1, "R"), (-1, 0, "U")]:
                next_x = x + dx
                next_y = y + dy

                if isSafe(next_x, next_y):
                    solve(next_x, next_y, path + move)

            visited[x][y] = False

        solve(0, 0, "")
        return ans
```

### Test Cases
- **Input:** `grid = [[1, 0, 0, 0], [1, 1, 0, 1], [1, 1, 0, 0], [0, 1, 1, 1]]`  
  **Output:** `["DDRDRR", "DRDDRR"]`

- **Input:** `grid = [[1, 0], [1, 0]]`  
  **Output:** `[]`

- **Now Your Turn:** `grid = [[1, 0, 0], [1, 1, 0], [0, 1, 1]]`  
  **Output:** `["DRDR"]`

### Complexity
- **Time:** O(4^(n*n)) - Every open cell can branch into four directions in the worst case
- **Space:** O(n^2) - Visited matrix and recursion stack

---

## 3) Word Break

- **TUF Problem:** [Word Break](https://takeuforward.org/plus/dsa/problems/word-break)
- **Striver Video:** [Word Break | DP on Strings](https://www.youtube.com/watch?v=th4OnoGasMU)
- **LeetCode:** [Word Break (LC 139)](https://leetcode.com/problems/word-break/)

### Problem Statement
Given a string `s` and a dictionary of words, return `True` if `s` can be segmented into one or more dictionary words. The same dictionary word can be reused multiple times.

### What Striver Discussed
- Use dynamic programming where `dp[i]` means `s[:i]` can be segmented.
- Start with `dp[0] = True` because an empty prefix is valid.
- For each end index, test every possible split point.
- If the prefix is valid and the suffix exists in the dictionary, mark the current index as valid.

### Clean Python Solution
```python
class Solution:
    def wordBreak(self, s, wordDict):
        word_set = set(wordDict)
        n = len(s)

        dp = [False] * (n + 1)
        dp[0] = True

        for end in range(1, n + 1):
            for start in range(end):
                if dp[start] and s[start:end] in word_set:
                    dp[end] = True
                    break

        return dp[n]
```

### Test Cases
- **Input:** `s = "takeuforward"`, `wordDict = ["take", "forward", "you", "u"]`  
  **Output:** `True`

- **Input:** `s = "applepineapple"`, `wordDict = ["apple"]`  
  **Output:** `False`

- **Now Your Turn:** `s = "catsanddogs"`, `wordDict = ["and", "dogs", "cats", "animals"]`  
  **Output:** `True`

### Complexity
- **Time:** O(n^2 * k) - Every substring split can be checked, and slicing costs up to substring length
- **Space:** O(n + d) - DP array and dictionary set

---

## Key Learnings From Today

### M Coloring Problem
- Backtracking can test graph color assignments one vertex at a time.
- A color is valid only when no adjacent vertex already uses it.
- Resetting a color during backtracking keeps later choices independent.

### Rat in a Maze
- A visited matrix prevents cycles inside a path.
- Direction order controls the order of generated path strings.
- Backtracking restores the cell so other paths can still use it later.

### Word Break
- DP converts repeated segmentation checks into stored prefix states.
- `dp[0] = True` is the base for building valid prefixes.
- A set makes dictionary word lookup efficient.
