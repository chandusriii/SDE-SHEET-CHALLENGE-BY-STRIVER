"""
Search in a 2D Matrix - Day 5 SDE Sheet Challenge

Problem: Given a 2D array where:
- Each row is sorted in non-decreasing order
- First element of each row is greater than last element of previous row
- Find if a target value exists in the matrix

Algorithm: Binary Search on 1D representation of 2D matrix
Time Complexity: O(log(m*n))
Space Complexity: O(1)
"""

class Solution:
    def searchMatrix(self, mat, target):
        """
        Search for target in 2D matrix using binary search.
        
        Key Insight:
        Treat the 2D matrix as a 1D sorted array and perform binary search.
        Index Conversion: row = mid // m, col = mid % m
        """
        n = len(mat)
        m = len(mat[0])

        low = 0
        high = n * m - 1

        while low <= high:
            mid = (low + high) // 2
            row = mid // m
            col = mid % m

            if mat[row][col] == target:
                return True
            elif mat[row][col] < target:
                low = mid + 1
            else:
                high = mid - 1

        return False


if __name__ == "__main__":
    obj = Solution()
    mat1 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    print(obj.searchMatrix(mat1, 8))  # True
    
    mat2 = [[1, 2, 4], [6, 7, 8], [9, 10, 34]]
    print(obj.searchMatrix(mat2, 78))  # False
    print(obj.searchMatrix(mat2, 7))  # True
