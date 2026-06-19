from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        """Return every valid N-Queens board arrangement."""
        ans = []
        board = [["." for _ in range(n)] for _ in range(n)]

        left_row = [0] * n
        lower_diagonal = [0] * (2 * n - 1)
        upper_diagonal = [0] * (2 * n - 1)

        def solve(col: int) -> None:
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


if __name__ == "__main__":
    solution = Solution()

    n1 = 4
    print(f"Input: n = {n1}")
    print(f"Output: {solution.solveNQueens(n1)}")
    print("Expected: [['..Q.', 'Q...', '...Q', '.Q..'], ['.Q..', '...Q', 'Q...', '..Q.']]\n")

    n2 = 2
    print(f"Input: n = {n2}")
    print(f"Output: {solution.solveNQueens(n2)}")
    print("Expected: [[]]\n")

    n3 = 1
    print(f"Input: n = {n3}")
    print(f"Output: {solution.solveNQueens(n3)}")
    print("Expected: [['Q']]")
