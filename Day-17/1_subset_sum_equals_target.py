from typing import List


class Solution:
    def isSubsetSum(self, arr: List[int], target: int) -> bool:
        """Return True if any subset of arr has sum equal to target."""
        dp = [False] * (target + 1)
        dp[0] = True

        for num in arr:
            for current_sum in range(target, num - 1, -1):
                dp[current_sum] = dp[current_sum] or dp[current_sum - num]

        return dp[target]


if __name__ == "__main__":
    solution = Solution()

    arr1 = [1, 2, 7, 3]
    target1 = 6
    print(f"Input: arr = {arr1}, target = {target1}")
    print(f"Output: {solution.isSubsetSum(arr1, target1)}")
    print("Expected: True\n")

    arr2 = [2, 3, 5]
    target2 = 6
    print(f"Input: arr = {arr2}, target = {target2}")
    print(f"Output: {solution.isSubsetSum(arr2, target2)}")
    print("Expected: False\n")

    arr3 = [7, 54, 4, 12, 15, 5]
    target3 = 9
    print(f"Input: arr = {arr3}, target = {target3}")
    print(f"Output: {solution.isSubsetSum(arr3, target3)}")
    print("Expected: True")
