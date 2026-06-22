class Solution:
    def countStudents(self, nums, maxPages):
        students = 1
        pages = 0

        for num in nums:
            if pages + num <= maxPages:
                pages += num
            else:
                students += 1
                pages = num

        return students

    def findPages(self, nums, m):
        n = len(nums)

        if m > n:
            return -1

        low = max(nums)
        high = sum(nums)

        while low <= high:
            mid = (low + high) // 2

            students = self.countStudents(nums, mid)

            if students > m:
                low = mid + 1
            else:
                high = mid - 1

        return low


# Driver Code
nums = [15, 17, 20]
m = 2

obj = Solution()
print(obj.findPages(nums, m))
