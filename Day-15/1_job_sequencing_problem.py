from typing import List


class Solution:
    def JobScheduling(self, Jobs: List[List[int]]) -> List[int]:
        """Return the maximum number of jobs and profit possible."""
        Jobs.sort(key=lambda job: job[2], reverse=True)

        max_deadline = 0
        for job in Jobs:
            max_deadline = max(max_deadline, job[1])

        slots = [-1] * (max_deadline + 1)
        count_jobs = 0
        job_profit = 0

        for job_id, deadline, profit in Jobs:
            for time in range(deadline, 0, -1):
                if slots[time] == -1:
                    slots[time] = job_id
                    count_jobs += 1
                    job_profit += profit
                    break

        return [count_jobs, job_profit]


if __name__ == "__main__":
    solution = Solution()

    jobs1 = [[1, 4, 20], [2, 1, 10], [3, 1, 40], [4, 1, 30]]
    print(f"Input: Jobs = {jobs1}")
    print(f"Output: {solution.JobScheduling(jobs1)}")
    print("Expected: [2, 60]\n")

    jobs2 = [[1, 2, 100], [2, 1, 19], [3, 2, 27], [4, 1, 25], [5, 1, 15]]
    print(f"Input: Jobs = {jobs2}")
    print(f"Output: {solution.JobScheduling(jobs2)}")
    print("Expected: [2, 127]\n")

    jobs3 = [[1, 1, 100], [2, 2, 200], [3, 3, 300], [4, 4, 400]]
    print(f"Input: Jobs = {jobs3}")
    print(f"Output: {solution.JobScheduling(jobs3)}")
    print("Expected: [4, 1000]\n")
