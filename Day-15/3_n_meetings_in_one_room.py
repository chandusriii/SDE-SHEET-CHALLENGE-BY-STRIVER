from typing import List


class Solution:
    def maxMeetings(self, start: List[int], end: List[int]) -> int:
        """Return the maximum meetings possible in one room."""
        n = len(start)
        meetings = [(end[i], start[i]) for i in range(n)]
        meetings.sort()

        count = 0
        last_end = -1

        for meeting_end, meeting_start in meetings:
            if meeting_start > last_end:
                count += 1
                last_end = meeting_end

        return count


if __name__ == "__main__":
    solution = Solution()

    start1 = [1, 3, 0, 5, 8, 5]
    end1 = [2, 4, 6, 7, 9, 9]
    print(f"Input: Start = {start1}, End = {end1}")
    print(f"Output: {solution.maxMeetings(start1, end1)}")
    print("Expected: 4\n")

    start2 = [10, 12, 20]
    end2 = [20, 25, 30]
    print(f"Input: Start = {start2}, End = {end2}")
    print(f"Output: {solution.maxMeetings(start2, end2)}")
    print("Expected: 1\n")

    start3 = [1, 4, 6, 9]
    end3 = [2, 5, 7, 12]
    print(f"Input: Start = {start3}, End = {end3}")
    print(f"Output: {solution.maxMeetings(start3, end3)}")
    print("Expected: 4\n")
