# #45DaysSDEChallenge - Day 2

**Date:** June 2, 2026  
**Problems Solved Today:** 3  
**Sheet:** [Striver SDE Sheet](https://takeuforward.org/dsa/strivers-sde-sheet-top-coding-interview-problems)

---

## 1) Kadane's Algorithm

- **TUF Problem:** [Kadane's Algorithm](https://takeuforward.org/dsa/kadanes-algorithm-maximum-subarray-sum-in-an-array/)
- **LeetCode (closest):** [Maximum Subarray (LC 53)](https://leetcode.com/problems/maximum-subarray/)
- **Striver Video:** [Watch](https://youtu.be/AHZpyENo7k4?si=DIxyXfFfoz55cS3v)

### What Striver Discussed
- Brute force: Generate all subarrays and compute the sum for each subarray.
- Better approach: Improve brute force by carrying the running sum while expanding subarrays.
- Optimal approach (used): Kadane's Algorithm.
  1. Keep a running sum.
  2. Update the maximum answer whenever the running sum improves.
  3. If the running sum becomes negative, reset it to `0` because it will only hurt future subarrays.

### Clean C++ Solution
```cpp
class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int maxi = nums[0];
        int sum = 0;

        for (int num : nums) {
            sum += num;
            maxi = max(maxi, sum);

            if (sum < 0) {
                sum = 0;
            }
        }

        return maxi;
    }
};
```

### Complexity
- **Time:** O(n)
- **Space:** O(1)

---

## 2) Best Time to Buy and Sell Stock

- **TUF Problem:** [Stock Buy And Sell](https://takeuforward.org/dsa/buy-and-sell-stock/)
- **LeetCode:** [Best Time to Buy and Sell Stock (LC 121)](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)
- **Striver Video:** [Watch](https://youtu.be/34VNqXm8BqE?si=vJO8sxVv5F5v5F5v)

### What Striver Discussed
- Brute force: Try every possible pair of buy and sell days and compute the profit.
- Optimal approach (used):
  1. Track the minimum price seen so far.
  2. For each day, calculate profit if we sell on that day.
  3. Keep updating the maximum profit.

### Clean C++ Solution
```cpp
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int minPrice = prices[0];
        int maxProfit = 0;

        for (int i = 1; i < prices.size(); i++) {
            int profit = prices[i] - minPrice;
            maxProfit = max(maxProfit, profit);
            minPrice = min(minPrice, prices[i]);
        }

        return maxProfit;
    }
};
```

### Complexity
- **Time:** O(n)
- **Space:** O(1)

---

## 3) Sort Colors

- **TUF Problem:** [Sort an array of 0's, 1's and 2's](https://takeuforward.org/dsa/sort-an-array-of-0s-1s-and-2s/)
- **LeetCode:** [Sort Colors (LC 75)](https://leetcode.com/problems/sort-colors/)
- **Striver Video:** [Watch](https://youtu.be/oaVa-9wEAToM?si=oaVa-9wEAToM)

### What Striver Discussed
- Better approach: Count the number of 0s, 1s, and 2s, then overwrite the array based on those counts.
- Optimal approach (used): Dutch National Flag Algorithm.
  - `low` points to where the next 0 should go.
  - `mid` scans the array.
  - `high` points to where the next 2 should go.
  - Swap based on whether nums[mid] is 0, 1, or 2.

### Clean C++ Solution
```cpp
class Solution {
public:
    void sortColors(vector<int>& nums) {
        int low = 0;
        int mid = 0;
        int high = nums.size() - 1;

        while (mid <= high) {
            if (nums[mid] == 0) {
                swap(nums[low], nums[mid]);
                low++;
                mid++;
            } else if (nums[mid] == 1) {
                mid++;
            } else {
                swap(nums[mid], nums[high]);
                high--;
            }
        }
    }
};
```

### Complexity
- **Time:** O(n)
- **Space:** O(1)

---

## Key Learnings From Today

### Kadane's Algorithm
- Learned how to maintain the best subarray sum ending at the current index using a running sum.
- Resetting the sum when it becomes negative helps start a better subarray ahead.

### Best Time to Buy and Sell Stock
- Understood the greedy pattern of tracking the minimum value seen so far.
- Maximum profit can be found in one pass by comparing each price with the best buy price before it.

### Sort Colors
- Learned the Dutch National Flag pattern using three pointers.
- This is an in-place one-pass partitioning technique with constant extra space.