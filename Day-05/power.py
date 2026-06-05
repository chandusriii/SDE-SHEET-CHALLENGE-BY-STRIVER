"""
Power(x, n) - Day 5 SDE Sheet Challenge

Problem: Implement the power function pow(x, n), which calculates x raised to n (x^n).
Note: In output print 4 digits places after decimal point.

Algorithm: Binary Exponentiation (Iterative)
Time Complexity: O(log n)
Space Complexity: O(1)
"""

class Solution:
    def myPow(self, x: float, n: int) -> float:
        """
        Calculate x raised to n using binary exponentiation.
        
        Why this works:
        - x^13 = x^(1101 in binary) = x^8 * x^4 * x^1
        - We process each bit of n from right to left
        - Time complexity: O(log n) instead of O(n)
        """
        if n < 0:
            x = 1 / x
            n = -n

        result = 1.0
        while n > 0:
            if n % 2 == 1:
                result *= x
            x *= x
            n //= 2

        return result


if __name__ == "__main__":
    sol = Solution()
    print(f"{sol.myPow(2.0, 10):.4f}")  # 1024.0000
    print(f"{sol.myPow(2.0, -2):.4f}")  # 0.2500
    print(f"{sol.myPow(2.5, 2):.4f}")  # 6.2500
