class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        Calculate unique paths in an m x n grid.
        Can only move right or down.
        
        Formula: C(m+n-2, min(m-1, n-1))
        
        Args:
            m: Number of rows
            n: Number of columns
            
        Returns:
            Number of unique paths from (0,0) to (m-1,n-1)
        """
        N = m + n - 2  # Total moves needed
        r = min(m - 1, n - 1)  # Choose the smaller for efficiency

        result = 1
        # Compute C(N, r) iteratively without factorials
        for i in range(1, r + 1):
            result = result * (N - r + i) // i

        return result


# Test cases
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    print(f"Input: m = 3, n = 2")
    print(f"Output: {solution.uniquePaths(3, 2)}")
    print(f"Expected: 3\n")

    # Test case 2
    print(f"Input: m = 2, n = 4")
    print(f"Output: {solution.uniquePaths(2, 4)}")
    print(f"Expected: 4\n")

    # Test case 3
    print(f"Input: m = 3, n = 3")
    print(f"Output: {solution.uniquePaths(3, 3)}")
    print(f"Expected: 6\n")

    # Test case 4
    print(f"Input: m = 1, n = 1")
    print(f"Output: {solution.uniquePaths(1, 1)}")
    print(f"Expected: 1\n")

    # Test case 5
    print(f"Input: m = 10, n = 10")
    print(f"Output: {solution.uniquePaths(10, 10)}")
    print(f"Expected: 48620\n")
