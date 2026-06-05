"""
Majority Element - I - Day 5 SDE Sheet Challenge

Problem: Given an integer array nums of size n, return the majority element of the array.
The majority element is an element that appears more than n/2 times in the array.
The array is guaranteed to have a majority element.

Approach: Hash Map (Count Frequency)
Time Complexity: O(n)
Space Complexity: O(n)
"""

from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """
        Find the majority element using a hash map to count frequencies.
        
        Algorithm:
        1. Create a hash map to store frequency of each element
        2. Count occurrences of each element in the array
        3. Return the element with count > n/2
        
        Args:
            nums: List of integers
            
        Returns:
            The majority element that appears more than n/2 times
        """
        n = len(nums)
        mp = {}
        
        for num in nums:
            mp[num] = mp.get(num, 0) + 1
        
        for num, count in mp.items():
            if count > n // 2:
                return num
        
        return -1


if __name__ == "__main__":
    sol = Solution()
    print(sol.majorityElement([7, 0, 0, 1, 7, 7, 2, 7, 7]))  # 7
    print(sol.majorityElement([1, 1, 1, 2, 1, 2]))  # 1
    print(sol.majorityElement([-1, -1, -1, -1]))  # -1
