from typing import List


class Solution:
    def findPlatform(self, Arrival: List[int], Departure: List[int]) -> int:
        """Return the minimum platforms needed so no train waits."""
        n = len(Arrival)
        Arrival.sort()
        Departure.sort()

        platforms = 1
        result = 1
        i = 1
        j = 0

        while i < n and j < n:
            if Arrival[i] <= Departure[j]:
                platforms += 1
                i += 1
            else:
                platforms -= 1
                j += 1

            result = max(result, platforms)

        return result


if __name__ == "__main__":
    solution = Solution()

    arrival1 = [900, 940, 950, 1100, 1500, 1800]
    departure1 = [910, 1200, 1120, 1130, 1900, 2000]
    print(f"Input: Arrival = {arrival1}, Departure = {departure1}")
    print(f"Output: {solution.findPlatform(arrival1, departure1)}")
    print("Expected: 3\n")

    arrival2 = [900, 1100, 1235]
    departure2 = [1000, 1200, 1240]
    print(f"Input: Arrival = {arrival2}, Departure = {departure2}")
    print(f"Output: {solution.findPlatform(arrival2, departure2)}")
    print("Expected: 1\n")

    arrival3 = [900, 1000, 1200]
    departure3 = [1000, 1200, 1240]
    print(f"Input: Arrival = {arrival3}, Departure = {departure3}")
    print(f"Output: {solution.findPlatform(arrival3, departure3)}")
    print("Expected: 2\n")
