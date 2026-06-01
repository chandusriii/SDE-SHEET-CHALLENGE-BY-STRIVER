class Solution:
    def setZeroes(self, matrix):
        m = len(matrix)
        n = len(matrix[0])

        col0 = 1

        # Step 1: Mark rows and columns
        for i in range(m):
            if matrix[i][0] == 0:
                col0 = 0

            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # Step 2: Fill zeros using markers
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # Step 3: Handle first row
        if matrix[0][0] == 0:
            for j in range(n):
                matrix[0][j] = 0

        # Step 4: Handle first column
        if col0 == 0:
            for i in range(m):
                matrix[i][0] = 0
