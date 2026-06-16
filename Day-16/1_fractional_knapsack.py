from typing import List


class Solution:
    def fractionalKnapsack(self, val: List[int], wt: List[int], capacity: int) -> float:
        """Return the maximum value that can fit in the knapsack."""
        n = len(val)
        items = []

        for i in range(n):
            items.append((val[i] / wt[i], val[i], wt[i]))

        items.sort(reverse=True)

        total_value = 0.0
        current_weight = 0

        for ratio, value, weight in items:
            if current_weight + weight <= capacity:
                current_weight += weight
                total_value += value
            else:
                remaining = capacity - current_weight
                total_value += ratio * remaining
                break

        return round(total_value, 6)


if __name__ == "__main__":
    solution = Solution()

    val1 = [60, 100, 120]
    wt1 = [10, 20, 30]
    capacity1 = 50
    print(f"Input: val = {val1}, wt = {wt1}, capacity = {capacity1}")
    print(f"Output: {solution.fractionalKnapsack(val1, wt1, capacity1):.6f}")
    print("Expected: 240.000000\n")

    val2 = [60, 100]
    wt2 = [10, 20]
    capacity2 = 50
    print(f"Input: val = {val2}, wt = {wt2}, capacity = {capacity2}")
    print(f"Output: {solution.fractionalKnapsack(val2, wt2, capacity2):.6f}")
    print("Expected: 160.000000\n")
