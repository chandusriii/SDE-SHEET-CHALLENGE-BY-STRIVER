"""
Aggressive Cows
Place C cows in stalls such that the minimum distance between any two cows is maximized.
Return the largest minimum distance.
"""
from typing import List


def can_place(stalls: List[int], cows: int, dist: int) -> bool:
    count = 1
    last_pos = stalls[0]
    for s in stalls[1:]:
        if s - last_pos >= dist:
            count += 1
            last_pos = s
            if count == cows:
                return True
    return False


def aggressive_cows(stalls: List[int], cows: int) -> int:
    stalls.sort()
    low, high = 0, stalls[-1] - stalls[0]
    best = 0
    while low <= high:
        mid = (low + high) // 2
        if can_place(stalls, cows, mid):
            best = mid
            low = mid + 1
        else:
            high = mid - 1
    return best


if __name__ == "__main__":
    stalls = [1, 2, 8, 4, 9]
    cows = 3
    print("Stalls:", stalls)
    print("Cows:", cows)
    print("Largest minimum distance:", aggressive_cows(stalls, cows))
