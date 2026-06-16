from typing import List


class Solution:
    def MinimumCoins(self, coins: List[int], amount: int) -> int:
        """Return the minimum number of coins needed to make amount."""
        n = len(coins)
        inf = int(1e9)

        prev = [0] * (amount + 1)
        cur = [0] * (amount + 1)

        for target in range(amount + 1):
            if target % coins[0] == 0:
                prev[target] = target // coins[0]
            else:
                prev[target] = inf

        for index in range(1, n):
            for target in range(amount + 1):
                not_take = prev[target]

                take = inf
                if coins[index] <= target:
                    take = 1 + cur[target - coins[index]]

                cur[target] = min(not_take, take)

            prev = cur[:]

        return -1 if prev[amount] >= inf else prev[amount]


if __name__ == "__main__":
    solution = Solution()

    coins1 = [1, 2, 5]
    amount1 = 11
    print(f"Input: coins = {coins1}, amount = {amount1}")
    print(f"Output: {solution.MinimumCoins(coins1, amount1)}")
    print("Expected: 3\n")

    coins2 = [2, 5]
    amount2 = 3
    print(f"Input: coins = {coins2}, amount = {amount2}")
    print(f"Output: {solution.MinimumCoins(coins2, amount2)}")
    print("Expected: -1\n")

    coins3 = [10]
    amount3 = 5
    print(f"Input: coins = {coins3}, amount = {amount3}")
    print(f"Output: {solution.MinimumCoins(coins3, amount3)}")
    print("Expected: -1\n")
