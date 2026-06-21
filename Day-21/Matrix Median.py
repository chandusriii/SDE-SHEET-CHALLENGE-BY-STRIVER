import bisect

class Solution:
    def findMedian(self, matrix):
        n = len(matrix)
        m = len(matrix[0])

        low = min(row[0] for row in matrix)
        high = max(row[-1] for row in matrix)

        required = (n * m + 1) // 2

        while low < high:
            mid = (low + high) // 2

            count = 0
            for row in matrix:
                count += bisect.bisect_right(row, mid)

            if count < required:
                low = mid + 1
            else:
                high = mid

        return low
