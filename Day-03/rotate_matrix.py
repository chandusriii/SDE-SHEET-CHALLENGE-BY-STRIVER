"""
Day 3 - Problem 3: Rotate Matrix by 90 Degrees
Link: https://takeuforward.org/dsa/rotate-matrix-by-90-degree
LeetCode: https://leetcode.com/problems/rotate-image/
"""

class Solution:
    def rotateMatrix(self, matrix):
        """
        Rotate matrix by 90 degrees clockwise in-place.
        
        Args:
            matrix: N x N 2D matrix
        
        Returns:
            The rotated matrix (modified in-place)
        
        Time Complexity: O(n²)
        Space Complexity: O(1)
        
        Approach: Transpose + Reverse Rows
        1. Transpose: Swap matrix[i][j] with matrix[j][i]
        2. Reverse each row
        
        Example:
        Original:      After Transpose:    After Row Reverse:
        1 2 3          1 4 7               7 4 1
        4 5 6    →     2 5 8        →      8 5 2
        7 8 9          3 6 9               9 6 3
        """
        n = len(matrix)

        # Step 1: Transpose the matrix
        # Swap matrix[i][j] with matrix[j][i]
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Step 2: Reverse each row
        for i in range(n):
            matrix[i].reverse()

        return matrix


# Helper function to print matrix
def print_matrix(matrix):
    for row in matrix:
        print(row)
    print()


# Test cases
if __name__ == "__main__":
    sol = Solution()
    
    # Test case 1: 3x3 matrix
    print("Test 1:")
    matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print("Before rotation:")
    print_matrix(matrix1)
    sol.rotateMatrix(matrix1)
    print("After rotation:")
    print_matrix(matrix1)
    # Expected: [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
    
    # Test case 2: 4x4 matrix
    print("Test 2:")
    matrix2 = [[0, 1, 1, 2], [2, 0, 3, 1], [4, 5, 0, 5], [5, 6, 7, 0]]
    print("Before rotation:")
    print_matrix(matrix2)
    sol.rotateMatrix(matrix2)
    print("After rotation:")
    print_matrix(matrix2)
    # Expected: [[5, 4, 2, 0], [6, 5, 0, 1], [7, 0, 3, 1], [0, 5, 1, 2]]
    
    # Test case 3: Given example from problem
    print("Test 3:")
    matrix3 = [[1, 1, 2], [5, 3, 1], [5, 3, 5]]
    print("Before rotation:")
    print_matrix(matrix3)
    sol.rotateMatrix(matrix3)
    print("After rotation:")
    print_matrix(matrix3)
    # Expected: [[5, 5, 1], [3, 3, 1], [5, 1, 2]]
    
    # Test case 4: 1x1 matrix
    print("Test 4:")
    matrix4 = [[1]]
    print("Before rotation:")
    print_matrix(matrix4)
    sol.rotateMatrix(matrix4)
    print("After rotation:")
    print_matrix(matrix4)
    # Expected: [[1]]
    
    # Test case 5: 2x2 matrix
    print("Test 5:")
    matrix5 = [[1, 2], [3, 4]]
    print("Before rotation:")
    print_matrix(matrix5)
    sol.rotateMatrix(matrix5)
    print("After rotation:")
    print_matrix(matrix5)
    # Expected: [[3, 1], [4, 2]]
