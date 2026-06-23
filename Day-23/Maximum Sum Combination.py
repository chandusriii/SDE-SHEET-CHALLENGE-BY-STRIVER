import heapq

class Solution:
    def maxCombinations(self, nums1, nums2, k):
        n = len(nums1)

        nums1.sort(reverse=True)
        nums2.sort(reverse=True)

        max_heap = []
        visited = set()

        heapq.heappush(max_heap, (-(nums1[0] + nums2[0]), 0, 0))
        visited.add((0, 0))

        ans = []

        while k > 0 and max_heap:
            curr_sum, i, j = heapq.heappop(max_heap)
            ans.append(-curr_sum)

            if i + 1 < n and (i + 1, j) not in visited:
                heapq.heappush(
                    max_heap,
                    (-(nums1[i + 1] + nums2[j]), i + 1, j)
                )
                visited.add((i + 1, j))

            if j + 1 < n and (i, j + 1) not in visited:
                heapq.heappush(
                    max_heap,
                    (-(nums1[i] + nums2[j + 1]), i, j + 1)
                )
                visited.add((i, j + 1))

            k -= 1

        return ans
