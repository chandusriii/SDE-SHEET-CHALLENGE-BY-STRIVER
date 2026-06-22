"""
Book Allocation Problem
Given N books with pages[], allocate to M students so that the maximum pages assigned to a student is minimized.
Return the minimized maximum. If not possible, return -1.
"""
from typing import List


def is_possible(pages: List[int], students: int, max_pages: int) -> bool:
    required = 1
    current = 0
    for p in pages:
        if p > max_pages:
            return False
        if current + p <= max_pages:
            current += p
        else:
            required += 1
            current = p
            if required > students:
                return False
    return True


def allocate_books(pages: List[int], students: int) -> int:
    if students > len(pages):
        return -1
    low, high = max(pages), sum(pages)
    ans = high
    while low <= high:
        mid = (low + high) // 2
        if is_possible(pages, students, mid):
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    return ans


if __name__ == "__main__":
    pages = [10, 20, 30, 40]
    students = 2
    print("Pages:", pages)
    print("Students:", students)
    print("Minimum largest pages:", allocate_books(pages, students))
