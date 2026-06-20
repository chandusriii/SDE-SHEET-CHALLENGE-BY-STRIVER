from typing import List


class Solution:
    def isSafe(
        self,
        x: int,
        y: int,
        n: int,
        grid: List[List[int]],
        visited: List[List[bool]],
    ) -> bool:
        return 0 <= x < n and 0 <= y < n and grid[x][y] == 1 and not visited[x][y]

    def solve(
        self,
        x: int,
        y: int,
        n: int,
        grid: List[List[int]],
        visited: List[List[bool]],
        path: str,
        ans: List[str],
    ) -> None:
        if x == n - 1 and y == n - 1:
            ans.append(path)
            return

        visited[x][y] = True

        directions = [
            (1, 0, "D"),
            (0, -1, "L"),
            (0, 1, "R"),
            (-1, 0, "U"),
        ]

        for dx, dy, move in directions:
            next_x = x + dx
            next_y = y + dy

            if self.isSafe(next_x, next_y, n, grid, visited):
                self.solve(next_x, next_y, n, grid, visited, path + move, ans)

        visited[x][y] = False

    def findPath(self, grid: List[List[int]]) -> List[str]:
        n = len(grid)

        if grid[0][0] == 0 or grid[n - 1][n - 1] == 0:
            return []

        visited = [[False] * n for _ in range(n)]
        ans = []

        self.solve(0, 0, n, grid, visited, "", ans)
        return ans


if __name__ == "__main__":
    solution = Solution()

    grid1 = [
        [1, 0, 0, 0],
        [1, 1, 0, 1],
        [1, 1, 0, 0],
        [0, 1, 1, 1],
    ]
    print(f"Input: grid = {grid1}")
    print(f"Output: {solution.findPath(grid1)}")
    print("Expected: ['DDRDRR', 'DRDDRR']\n")

    grid2 = [
        [1, 0],
        [1, 0],
    ]
    print(f"Input: grid = {grid2}")
    print(f"Output: {solution.findPath(grid2)}")
    print("Expected: []\n")

    grid3 = [
        [1, 0, 0],
        [1, 1, 0],
        [0, 1, 1],
    ]
    print(f"Input: grid = {grid3}")
    print(f"Output: {solution.findPath(grid3)}")
    print("Expected: ['DRDR']")
