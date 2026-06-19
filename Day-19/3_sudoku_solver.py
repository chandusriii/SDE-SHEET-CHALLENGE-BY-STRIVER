from typing import List


class Solution:
    def isValid(self, board: List[List[str]], row: int, col: int, ch: str) -> bool:
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

    def solve(self, board: List[List[str]]) -> bool:
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

    def solveSudoku(self, board: List[List[str]]) -> None:
        """Solve the Sudoku board in-place."""
        self.solve(board)


if __name__ == "__main__":
    board = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]

    Solution().solveSudoku(board)

    print("Solved Sudoku:")
    for row in board:
        print(row)
