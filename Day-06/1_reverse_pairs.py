from typing import List

class Solution:
    def merge(self, arr, low, mid, high):
        """Merge two sorted halves of the array."""
        temp = []
        left = low
        right = mid + 1

        while left <= mid and right <= high:
            if arr[left] <= arr[right]:
                temp.append(arr[left])
                left += 1
            else:
                temp.append(arr[right])
                right += 1

        while left <= mid:
            temp.append(arr[left])
            left += 1

        while right <= high:
            temp.append(arr[right])
            right += 1

        for i in range(low, high + 1):
            arr[i] = temp[i - low]

    def countPairs(self, arr, low, mid, high):
        """Count reverse pairs using two pointers."""
        right = mid + 1
        cnt = 0

        for i in range(low, mid + 1):
            while right <= high and arr[i] > 2 * arr[right]:
                right += 1
            cnt += right - (mid + 1)

        return cnt

    def mergeSort(self, arr, low, high):
        """Merge sort with reverse pair counting."""
        if low >= high:
            return 0

        mid = (low + high) // 2

        # Count pairs in left half, right half, and across halves
        cnt = self.mergeSort(arr, low, mid)
        cnt += self.mergeSort(arr, mid + 1, high)
        cnt += self.countPairs(arr, low, mid, high)

        # Merge the sorted halves
        self.merge(arr, low, mid, high)

        return cnt

    def reversePairs(self, nums: List[int]) -> int:
        """Find the number of reverse pairs in the array."""
        return self.mergeSort(nums, 0, len(nums) - 1)


# Test cases
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    nums1 = [6, 4, 1, 2, 7]
    print(f"Input: {nums1}")
    print(f"Output: {solution.reversePairs(nums1.copy())}")
    print(f"Expected: 3\n")

    # Test case 2
    nums2 = [5, 4, 4, 3, 3]
    print(f"Input: {nums2}")
    print(f"Output: {solution.reversePairs(nums2.copy())}")
    print(f"Expected: 0\n")

    # Test case 3
    nums3 = [6, 4, 4, 2, 2]
    print(f"Input: {nums3}")
    print(f"Output: {solution.reversePairs(nums3.copy())}")
    print(f"Expected: 3\n")
