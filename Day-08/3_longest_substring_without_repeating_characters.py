class Solution:
    def longestNonRepeatingSubstring(self, s: str) -> int:
        """Return the longest substring length without repeating characters."""
        last_seen = {}
        left = 0
        longest = 0

        for right, char in enumerate(s):
            if char in last_seen and last_seen[char] >= left:
                left = last_seen[char] + 1

            last_seen[char] = right
            longest = max(longest, right - left + 1)

        return longest


if __name__ == "__main__":
    solution = Solution()

    s1 = "abcddabac"
    print(f"Input: S = {s1}")
    print(f"Output: {solution.longestNonRepeatingSubstring(s1)}")
    print("Expected: 4\n")

    s2 = "aaabbbccc"
    print(f"Input: S = {s2}")
    print(f"Output: {solution.longestNonRepeatingSubstring(s2)}")
    print("Expected: 2\n")

    s3 = "aaaa"
    print(f"Input: S = {s3}")
    print(f"Output: {solution.longestNonRepeatingSubstring(s3)}")
    print("Expected: 1\n")
