class Solution:
    def median(self, arr1, arr2):
        if len(arr1) > len(arr2):
            arr1, arr2 = arr2, arr1

        m, n = len(arr1), len(arr2)
        low, high = 0, m

        while low <= high:
            cut1 = (low + high) // 2
            cut2 = (m + n + 1) // 2 - cut1

            left1 = float('-inf') if cut1 == 0 else arr1[cut1 - 1]
            right1 = float('inf') if cut1 == m else arr1[cut1]

            left2 = float('-inf') if cut2 == 0 else arr2[cut2 - 1]
            right2 = float('inf') if cut2 == n else arr2[cut2]

            if left1 <= right2 and left2 <= right1:
                if (m + n) % 2 == 0:
                    return (max(left1, left2) + min(right1, right2)) / 2.0
                else:
                    return float(max(left1, left2))

            elif left1 > right2:
                high = cut1 - 1
            else:
                low = cut1 + 1

        return 0.0


# Driver Code
arr1 = [2, 4, 5]
arr2 = [1, 6]

obj = Solution()
print(obj.median(arr1, arr2))
