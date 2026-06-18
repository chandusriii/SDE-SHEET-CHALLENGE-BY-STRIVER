from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """Return all unique combinations that sum to target."""
        answer = []

        def findCombination(index: int, remaining: int, combination: List[int]) -> None:
            if index == len(candidates):
                if remaining == 0:
                    answer.append(combination[:])
                return

            if candidates[index] <= remaining:
                combination.append(candidates[index])
                findCombination(index, remaining - candidates[index], combination)
                combination.pop()

            findCombination(index + 1, remaining, combination)

        findCombination(0, target, [])
        return answer


if __name__ == "__main__":
    solution = Solution()

    candidates1 = [2, 3, 5, 4]
    target1 = 7
    print(f"Input: candidates = {candidates1}, target = {target1}")
    print(f"Output: {solution.combinationSum(candidates1, target1)}")
    print("Expected: [[2, 2, 3], [2, 5], [3, 4]]\n")

    candidates2 = [2]
    target2 = 1
    print(f"Input: candidates = {candidates2}, target = {target2}")
    print(f"Output: {solution.combinationSum(candidates2, target2)}")
    print("Expected: []\n")

    candidates3 = [3, 4, 5, 6]
    target3 = 10
    print(f"Input: candidates = {candidates3}, target = {target3}")
    print(f"Output: {solution.combinationSum(candidates3, target3)}")
    print("Expected: [[3, 3, 4], [4, 6], [5, 5]]")
