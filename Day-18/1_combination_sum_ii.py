from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        """Return unique combinations where each candidate is used at most once."""
        candidates.sort()
        result = []

        def backtrack(start: int, remaining: int, path: List[int]) -> None:
            if remaining == 0:
                result.append(path[:])
                return

            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                if candidates[i] > remaining:
                    break

                path.append(candidates[i])
                backtrack(i + 1, remaining - candidates[i], path)
                path.pop()

        backtrack(0, target, [])
        return result


if __name__ == "__main__":
    solution = Solution()

    candidates1 = [2, 1, 2, 7, 6, 1, 5]
    target1 = 8
    print(f"Input: candidates = {candidates1}, target = {target1}")
    print(f"Output: {solution.combinationSum2(candidates1, target1)}")
    print("Expected: [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]\n")

    candidates2 = [2, 5, 2, 1, 2]
    target2 = 5
    print(f"Input: candidates = {candidates2}, target = {target2}")
    print(f"Output: {solution.combinationSum2(candidates2, target2)}")
    print("Expected: [[1, 2, 2], [5]]\n")

    candidates3 = [2, 1, 2]
    target3 = 5
    print(f"Input: candidates = {candidates3}, target = {target3}")
    print(f"Output: {solution.combinationSum2(candidates3, target3)}")
    print("Expected: [[1, 2, 2]]")
