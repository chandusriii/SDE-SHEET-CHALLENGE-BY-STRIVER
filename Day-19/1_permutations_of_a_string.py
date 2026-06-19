from typing import List


class Solution:
    def permuteUnique(self, s: str) -> List[str]:
        """Return all unique permutations of s in lexicographic order."""
        chars = sorted(s)
        used = [False] * len(chars)
        result = []

        def backtrack(current: List[str]) -> None:
            if len(current) == len(chars):
                result.append("".join(current))
                return

            for i in range(len(chars)):
                if used[i]:
                    continue

                if i > 0 and chars[i] == chars[i - 1] and not used[i - 1]:
                    continue

                used[i] = True
                current.append(chars[i])

                backtrack(current)

                current.pop()
                used[i] = False

        backtrack([])
        return result


if __name__ == "__main__":
    solution = Solution()

    s1 = "abc"
    print(f'Input: s = "{s1}"')
    print(f"Output: {solution.permuteUnique(s1)}")
    print("Expected: ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']\n")

    s2 = "aab"
    print(f'Input: s = "{s2}"')
    print(f"Output: {solution.permuteUnique(s2)}")
    print("Expected: ['aab', 'aba', 'baa']\n")

    s3 = "aa"
    print(f'Input: s = "{s3}"')
    print(f"Output: {solution.permuteUnique(s3)}")
    print("Expected: ['aa']")
