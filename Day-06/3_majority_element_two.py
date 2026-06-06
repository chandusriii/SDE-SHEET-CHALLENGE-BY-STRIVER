from typing import List

class Solution:
    def majorityElementTwo(self, nums: List[int]) -> List[int]:
        """
        Find all elements that appear more than n/3 times.
        Uses Boyer-Moore Voting Algorithm (extended version).
        
        Key insight: At most 2 elements can appear more than n/3 times.
        
        Args:
            nums: List of integers
            
        Returns:
            List of elements appearing more than n/3 times, sorted
        """
        n = len(nums)

        # Initialize counters and candidates
        cnt1, cnt2 = 0, 0
        el1, el2 = float('-inf'), float('-inf')

        # First pass: Find potential candidates using vote cancellation
        for num in nums:
            if cnt1 == 0 and num != el2:
                el1 = num
                cnt1 = 1
            elif cnt2 == 0 and num != el1:
                el2 = num
                cnt2 = 1
            elif num == el1:
                cnt1 += 1
            elif num == el2:
                cnt2 += 1
            else:
                # Cancel one vote from each candidate
                cnt1 -= 1
                cnt2 -= 1

        # Second pass: Verify the candidates
        cnt1, cnt2 = 0, 0
        for num in nums:
            if num == el1:
                cnt1 += 1
            if num == el2:
                cnt2 += 1

        # Build result
        ans = []

        if cnt1 > n // 3:
            ans.append(el1)

        if cnt2 > n // 3 and el1 != el2:
            ans.append(el2)

        ans.sort()
        return ans


# Test cases
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    nums1 = [1, 2, 1, 1, 3, 2]
    print(f"Input: {nums1}")
    print(f"Output: {solution.majorityElementTwo(nums1)}")
    print(f"Expected: [1]\n")

    # Test case 2
    nums2 = [1, 2, 1, 1, 3, 2, 2]
    print(f"Input: {nums2}")
    print(f"Output: {solution.majorityElementTwo(nums2)}")
    print(f"Expected: [1, 2]\n")

    # Test case 3
    nums3 = [1, 2, 1, 1, 3, 2, 2, 3]
    print(f"Input: {nums3}")
    print(f"Output: {solution.majorityElementTwo(nums3)}")
    print(f"Expected: [1, 2]\n")

    # Test case 4
    nums4 = [1]
    print(f"Input: {nums4}")
    print(f"Output: {solution.majorityElementTwo(nums4)}")
    print(f"Expected: [1]\n")

    # Test case 5
    nums5 = [1, 1, 1, 2, 3]
    print(f"Input: {nums5}")
    print(f"Output: {solution.majorityElementTwo(nums5)}")
    print(f"Expected: [1]\n")
