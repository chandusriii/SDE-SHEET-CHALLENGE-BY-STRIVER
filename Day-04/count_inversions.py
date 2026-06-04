"""
Count Inversions

Problem: Given an integer array, return the number of inversions in the array.
An inversion is formed when two elements a[i] and a[j] satisfy:
- a[i] > a[j] AND i < j

Inversions indicate how close an array is to being sorted.

Approach: Merge Sort with Inversion Counting
Time Complexity: O(n log n)
Space Complexity: O(n)
"""

class Solution:
    def merge(self, arr, low, mid, high):
        """
        Merge two sorted subarrays and count inversions.
        
        When an element from the right subarray is smaller than an element 
        from the left subarray, it forms inversions with all remaining 
        elements in the left subarray.
        
        Args:
            arr: The array being sorted
            low: Start index of left subarray
            mid: End index of left subarray
            high: End index of right subarray
            
        Returns:
            Count of inversions formed during this merge
        """
        temp = []
        left = low
        right = mid + 1
        cnt = 0

        while left <= mid and right <= high:
            if arr[left] <= arr[right]:
                temp.append(arr[left])
                left += 1
            else:
                # Elements from right are smaller than left
                # They form inversions with all remaining elements in left
                temp.append(arr[right])
                cnt += (mid - left + 1)
                right += 1

        # Add remaining elements from left
        while left <= mid:
            temp.append(arr[left])
            left += 1

        # Add remaining elements from right
        while right <= high:
            temp.append(arr[right])
            right += 1

        # Copy sorted elements back to original array
        for i in range(low, high + 1):
            arr[i] = temp[i - low]

        return cnt

    def mergeSort(self, arr, low, high):
        """
        Recursively divide the array and count inversions.
        
        Args:
            arr: The array to sort and count inversions
            low: Start index
            high: End index
            
        Returns:
            Total count of inversions in the subarray
        """
        cnt = 0

        if low >= high:
            return cnt

        mid = (low + high) // 2

        # Count inversions in left half
        cnt += self.mergeSort(arr, low, mid)
        
        # Count inversions in right half
        cnt += self.mergeSort(arr, mid + 1, high)
        
        # Count inversions formed during merge
        cnt += self.merge(arr, low, mid, high)

        return cnt

    def numberOfInversions(self, nums):
        """
        Count the total number of inversions in the array.
        
        Args:
            nums: List of integers
            
        Returns:
            The number of inversions
        """
        return self.mergeSort(nums, 0, len(nums) - 1)


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    nums1 = [2, 3, 7, 1, 3, 5]
    result1 = solution.numberOfInversions(nums1.copy())
    print(f"Input: {nums1}")
    print(f"Output: {result1}")  # Expected: 5
    print("Inversions: (2,1), (3,1), (7,1), (7,3), (7,5)")
    print()
    
    # Test case 2
    nums2 = [-10, -5, 6, 11, 15, 17]
    result2 = solution.numberOfInversions(nums2.copy())
    print(f"Input: {nums2}")
    print(f"Output: {result2}")  # Expected: 0
    print("Already sorted, no inversions")
    print()
    
    # Test case 3
    nums3 = [9, 5, 4, 2]
    result3 = solution.numberOfInversions(nums3.copy())
    print(f"Input: {nums3}")
    print(f"Output: {result3}")  # Expected: 6
    print("All pairs form inversions")
