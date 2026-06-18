from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        """Return all partitions where every substring is a palindrome."""
        result = []

        def is_palindrome(left: int, right: int) -> bool:
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        def backtrack(start: int, path: List[str]) -> None:
            if start == len(s):
                result.append(path[:])
                return

            for end in range(start, len(s)):
                if is_palindrome(start, end):
                    path.append(s[start : end + 1])
                    backtrack(end + 1, path)
                    path.pop()

        backtrack(0, [])
        return result


if __name__ == "__main__":
    solution = Solution()

    s1 = "aabaa"
    print(f'Input: s = "{s1}"')
    print(f"Output: {solution.partition(s1)}")
    print('Expected: [["a", "a", "b", "a", "a"], ["a", "a", "b", "aa"], ["a", "aba", "a"], ["aa", "b", "a", "a"], ["aa", "b", "aa"], ["aabaa"]]\n')

    s2 = "baa"
    print(f'Input: s = "{s2}"')
    print(f"Output: {solution.partition(s2)}")
    print('Expected: [["b", "a", "a"], ["b", "aa"]]\n')

    s3 = "ab"
    print(f'Input: s = "{s3}"')
    print(f"Output: {solution.partition(s3)}")
    print('Expected: [["a", "b"]]')
