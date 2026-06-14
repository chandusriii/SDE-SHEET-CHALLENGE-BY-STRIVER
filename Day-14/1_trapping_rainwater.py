from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        """Return the total units of rainwater trapped between bars."""
        n = len(height)
        left = 0
        right = n - 1
        max_left = 0
        max_right = 0
        total_water = 0

        while left <= right:
            if height[left] <= height[right]:
                if height[left] >= max_left:
                    max_left = height[left]
                else:
                    total_water += max_left - height[left]

                left += 1
            else:
                if height[right] >= max_right:
                    max_right = height[right]
                else:
                    total_water += max_right - height[right]

                right -= 1

        return total_water


if __name__ == "__main__":
    solution = Solution()

    height1 = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    print(f"Input: height = {height1}")
    print(f"Output: {solution.trap(height1)}")
    print("Expected: 6\n")

    height2 = [4, 2, 0, 3, 2, 5]
    print(f"Input: height = {height2}")
    print(f"Output: {solution.trap(height2)}")
    print("Expected: 9\n")

    height3 = [7, 4, 0, 9]
    print(f"Input: height = {height3}")
    print(f"Output: {solution.trap(height3)}")
    print("Expected: 10\n")
