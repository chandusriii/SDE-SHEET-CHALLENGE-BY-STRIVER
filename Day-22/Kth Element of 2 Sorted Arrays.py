class Solution:
    def kthElement(self, a, b, k):
        if len(a) > len(b):
            return self.kthElement(b, a, k)

        m, n = len(a), len(b)

        low = max(0, k - n)
        high = min(k, m)

        while low <= high:
            cut1 = (low + high) // 2
            cut2 = k - cut1

            left1 = float('-inf') if cut1 == 0 else a[cut1 - 1]
            left2 = float('-inf') if cut2 == 0 else b[cut2 - 1]

            right1 = float('inf') if cut1 == m else a[cut1]
            right2 = float('inf') if cut2 == n else b[cut2]

            if left1 <= right2 and left2 <= right1:
                return max(left1, left2)

            elif left1 > right2:
                high = cut1 - 1
            else:
                low = cut1 + 1

        return -1


# Driver Code
a = [2, 3, 6]
b = [7, 9]
k = 4

obj = Solution()
print(obj.kthElement(a, b, k))
