class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        """Return the kth lexicographic permutation of numbers 1 to n."""
        numbers = list(range(1, n + 1))

        factorial = 1
        for value in range(1, n):
            factorial *= value

        k -= 1
        result = []

        while numbers:
            index = k // factorial
            result.append(str(numbers.pop(index)))

            if not numbers:
                break

            k %= factorial
            factorial //= len(numbers)

        return "".join(result)


if __name__ == "__main__":
    solution = Solution()

    n1, k1 = 3, 3
    print(f"Input: n = {n1}, k = {k1}")
    print(f"Output: {solution.getPermutation(n1, k1)}")
    print("Expected: 213\n")

    n2, k2 = 3, 5
    print(f"Input: n = {n2}, k = {k2}")
    print(f"Output: {solution.getPermutation(n2, k2)}")
    print("Expected: 312")
