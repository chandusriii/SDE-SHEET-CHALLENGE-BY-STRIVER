from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """Return True if s can be segmented using dictionary words."""
        word_set = set(wordDict)
        n = len(s)

        dp = [False] * (n + 1)
        dp[0] = True

        for end in range(1, n + 1):
            for start in range(end):
                if dp[start] and s[start:end] in word_set:
                    dp[end] = True
                    break

        return dp[n]


if __name__ == "__main__":
    solution = Solution()

    s1 = "takeuforward"
    word_dict1 = ["take", "forward", "you", "u"]
    print(f's = "{s1}", wordDict = {word_dict1}')
    print(f"Output: {solution.wordBreak(s1, word_dict1)}")
    print("Expected: True\n")

    s2 = "applepineapple"
    word_dict2 = ["apple"]
    print(f's = "{s2}", wordDict = {word_dict2}')
    print(f"Output: {solution.wordBreak(s2, word_dict2)}")
    print("Expected: False\n")

    s3 = "catsanddogs"
    word_dict3 = ["and", "dogs", "cats", "animals"]
    print(f's = "{s3}", wordDict = {word_dict3}')
    print(f"Output: {solution.wordBreak(s3, word_dict3)}")
    print("Expected: True")
