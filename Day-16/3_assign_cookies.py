from typing import List


class Solution:
    def findMaximumCookieStudents(self, Student: List[int], Cookie: List[int]) -> int:
        """Return the maximum number of students who can get cookies."""
        Student.sort()
        Cookie.sort()

        student_index = 0
        cookie_index = 0

        while student_index < len(Student) and cookie_index < len(Cookie):
            if Cookie[cookie_index] >= Student[student_index]:
                student_index += 1

            cookie_index += 1

        return student_index


if __name__ == "__main__":
    solution = Solution()

    student1 = [1, 2, 3]
    cookie1 = [1, 1]
    print(f"Input: Student = {student1}, Cookie = {cookie1}")
    print(f"Output: {solution.findMaximumCookieStudents(student1, cookie1)}")
    print("Expected: 1\n")

    student2 = [1, 2]
    cookie2 = [1, 2, 3]
    print(f"Input: Student = {student2}, Cookie = {cookie2}")
    print(f"Output: {solution.findMaximumCookieStudents(student2, cookie2)}")
    print("Expected: 2\n")

    student3 = [4, 5, 1]
    cookie3 = [6, 4, 2]
    print(f"Input: Student = {student3}, Cookie = {cookie3}")
    print(f"Output: {solution.findMaximumCookieStudents(student3, cookie3)}")
    print("Expected: 3\n")
