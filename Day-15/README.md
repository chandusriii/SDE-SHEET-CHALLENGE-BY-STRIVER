# #45DaysSDEChallenge - Day 15

**Date:** June 15, 2026  
**Problems Solved Today:** 3  
**Sheet:** [Striver SDE Sheet](https://takeuforward.org/dsa/strivers-sde-sheet-top-coding-interview-problems)

---

## 1) Job Sequencing Problem

- **TUF Problem:** [Job sequencing Problem](https://takeuforward.org/plus/dsa/problems/job-sequencing-problem)

### Problem Statement
Given jobs where each job has a job ID, deadline, and profit, schedule jobs so that each job takes one unit of time and the total profit is maximized. A job earns profit only if it is completed before or on its deadline.

### What Striver Discussed
- Pick jobs with higher profit first.
- Sort all jobs by profit in descending order.
- For every job, try to place it in the latest available slot before its deadline.
- Placing jobs as late as possible leaves earlier slots open for jobs with smaller deadlines.

### Clean Python Solution
```python
class Solution:
    def JobScheduling(self, Jobs):
        Jobs.sort(key=lambda x: x[2], reverse=True)

        maxi = 0
        for job in Jobs:
            maxi = max(maxi, job[1])

        slot = [-1] * (maxi + 1)
        countJobs = 0
        jobProfit = 0

        for job in Jobs:
            deadline = job[1]
            profit = job[2]

            for j in range(deadline, 0, -1):
                if slot[j] == -1:
                    slot[j] = job[0]
                    countJobs += 1
                    jobProfit += profit
                    break

        return [countJobs, jobProfit]
```

### Test Cases
- **Input:** `Jobs = [[1, 4, 20], [2, 1, 10], [3, 1, 40], [4, 1, 30]]`  
  **Output:** `2 60`

- **Input:** `Jobs = [[1, 2, 100], [2, 1, 19], [3, 2, 27], [4, 1, 25], [5, 1, 15]]`  
  **Output:** `2 127`

- **Now Your Turn:** `Jobs = [[1, 1, 100], [2, 2, 200], [3, 3, 300], [4, 4, 400]]`  
  **Output:** `4 1000`

### Complexity
- **Time:** O(n log n + n * d) - Sorting jobs and checking slots up to each deadline
- **Space:** O(d) - Slot array for deadlines

---

## 2) Minimum Number of Platforms Required for a Railway

- **TUF Problem:** [Minimum number of platforms required for a railway](https://takeuforward.org/plus/dsa/problems/minimum-number-of-platforms-required-for-a-railway)

### Problem Statement
Given arrival and departure times of trains, find the minimum number of platforms needed so that no train has to wait. If one train arrives at the same time another departs, a different platform is still required.

### What Striver Discussed
- Sort arrival times and departure times separately.
- Use two pointers to simulate events in chronological order.
- If the next arrival happens before or at the earliest departure, one more platform is needed.
- Otherwise, one train has departed and a platform becomes free.

### Clean Python Solution
```python
class Solution:
    def findPlatform(self, Arrival, Departure):
        n = len(Arrival)

        Arrival.sort()
        Departure.sort()

        platforms = 1
        result = 1
        i, j = 1, 0

        while i < n and j < n:
            if Arrival[i] <= Departure[j]:
                platforms += 1
                i += 1
            else:
                platforms -= 1
                j += 1

            result = max(result, platforms)

        return result
```

### Test Cases
- **Input:** `Arrival = [900, 940, 950, 1100, 1500, 1800]`, `Departure = [910, 1200, 1120, 1130, 1900, 2000]`  
  **Output:** `3`

- **Input:** `Arrival = [900, 1100, 1235]`, `Departure = [1000, 1200, 1240]`  
  **Output:** `1`

- **Now Your Turn:** `Arrival = [900, 1000, 1200]`, `Departure = [1000, 1200, 1240]`  
  **Output:** `2`

### Complexity
- **Time:** O(n log n) - Sorting arrival and departure arrays
- **Space:** O(1) - Apart from sorting, only counters and pointers are used

---

## 3) N Meetings in One Room

- **TUF Problem:** [N meetings in one room](https://takeuforward.org/plus/dsa/problems/n-meetings-in-one-room)

### Problem Statement
Given one meeting room and arrays `start` and `end`, find the maximum number of meetings that can be held when only one meeting can happen at a time.

### What Striver Discussed
- To maximize the number of meetings, always choose the meeting that ends earliest.
- Pair each meeting's start time with its end time.
- Sort meetings by end time.
- Select a meeting only if its start time is greater than the end time of the last selected meeting.

### Clean Python Solution
```python
class Solution:
    def maxMeetings(self, start, end):
        n = len(start)

        meetings = [(end[i], start[i]) for i in range(n)]
        meetings.sort()

        count = 0
        last_end = -1

        for e, s in meetings:
            if s > last_end:
                count += 1
                last_end = e

        return count
```

### Test Cases
- **Input:** `Start = [1, 3, 0, 5, 8, 5]`, `End = [2, 4, 6, 7, 9, 9]`  
  **Output:** `4`

- **Input:** `Start = [10, 12, 20]`, `End = [20, 25, 30]`  
  **Output:** `1`

- **Now Your Turn:** `Start = [1, 4, 6, 9]`, `End = [2, 5, 7, 12]`  
  **Output:** `4`

### Complexity
- **Time:** O(n log n) - Sorting meetings by end time
- **Space:** O(n) - Meeting pairs are stored

---

## Key Learnings From Today

### Job Sequencing Problem
- Greedy choice works by prioritizing maximum profit first.
- Scheduling jobs at the latest possible slot protects earlier slots.
- Deadlines can be modeled with a slot array.

### Minimum Number of Platforms
- Sorting arrivals and departures separately makes overlaps easy to count.
- Equal arrival and departure times still need separate platforms.
- The maximum active platform count is the final answer.

### N Meetings in One Room
- Earliest finishing meetings leave the most room for future meetings.
- Sorting by end time is the core greedy step.
- A meeting can be selected only when its start time is greater than the previous selected end time.
