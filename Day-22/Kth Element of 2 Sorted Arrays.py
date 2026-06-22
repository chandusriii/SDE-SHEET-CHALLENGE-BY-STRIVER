"""
Kth Element of 2 Sorted Arrays
Find the k-th element (1-indexed) in the union of two sorted arrays.
"""
from typing import List


def kth_element(nums1: List[int], nums2: List[int], k: int) -> int:
    # Ensure nums1 is the smaller
    if len(nums1) > len(nums2):
        return kth_element(nums2, nums1, k)
    m, n = len(nums1), len(nums2)
    if m == 0:
        return nums2[k-1]
    if k == 1:
        return min(nums1[0], nums2[0])
    i = min(m, k // 2)
    j = min(n, k - i)
    if nums1[i-1] <= nums2[j-1]:
        return kth_element(nums1[i:], nums2, k - i)
    else:
        return kth_element(nums1, nums2[j:], k - j)


if __name__ == "__main__":
    a = [2, 3, 6, 7, 9]
    b = [1, 4, 8, 10]
    k = 5
    print("A:", a)
    print("B:", b)
    print(f"{k}-th element:", kth_element(a, b, k))
