class Solution:
    def NthRoot(self, N, M):
        low, high = 1, M

        while low <= high:
            mid = (low + high) // 2

            power = 1
            for _ in range(N):
                power *= mid
                if power > M:
                    break

            if power == M:
                return mid
            elif power < M:
                low = mid + 1
            else:
                high = mid - 1

        return -1
