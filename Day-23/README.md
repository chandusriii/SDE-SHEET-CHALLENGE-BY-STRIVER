#45DaysSDEChallenge - Day 23
Date: June 23, 2026
Problems Solved Today: 3
Sheet: Striver SDE Sheet

## 1) Implement Max Heap

**TUF Problem:** Implement Max Heap

### What Striver Discussed

**Heap Basics**

* A Max Heap is a complete binary tree where every parent node is greater than or equal to its children.
* Efficiently supports insertion, deletion of maximum element, and priority-based operations.

**Operations Implemented**

* Insert
* Get Maximum
* Extract Maximum
* Change Key
* Heap Size
* Is Empty

**Approach Used**

* Insert: Add element at the end and perform Bottom-Up Heapify (Bubble Up).
* Extract Max: Replace root with last element and perform Top-Down Heapify (Heapify Down).
* Change Key:

  * If value increases, Bubble Up.
  * If value decreases, Heapify Down.

### Complexity

* Insert: O(log n)
* Extract Max: O(log n)
* Change Key: O(log n)
* Get Max: O(1)
* Heap Size: O(1)
* Is Empty: O(1)

---

## 2) K-th Largest Element in an Array

**TUF Problem:** K-th Largest Element in an Array

### What Striver Discussed

**Brute Force**

* Sort the entire array in descending order.
* Return the k-th element.

**Better / Optimal Approach (Used)**

* Maintain a Min Heap of size k.
* Insert elements one by one.
* If heap size exceeds k, remove the smallest element.
* After processing all elements, heap top represents the k-th largest element.

### Complexity

* Time: O(n log k)
* Space: O(k)

---

## 3) Maximum Sum Combination

**TUF Problem:** Maximum Sum Combination

### What Striver Discussed

**Brute Force**

* Generate all possible pair sums.
* Sort all sums in descending order.
* Return the first k sums.
* Complexity becomes O(n² log n²).

**Optimal Approach (Used)**

* Sort both arrays in descending order.
* Use a Max Heap to always pick the current maximum sum.
* Store visited index pairs in a set to avoid duplicate processing.
* Push neighboring combinations:

  * (i+1, j)
  * (i, j+1)

This efficiently generates the top k sums without generating all possible combinations.

### Complexity

* Time: O(n log n + k log k)
* Space: O(k)

---

# Key Learnings From Today

### Implement Max Heap

* Learned how Heap operations maintain the Max Heap property.
* Understood Bottom-Up Heapify and Top-Down Heapify.
* Practiced implementing a Heap from scratch without using built-in libraries.

### K-th Largest Element in an Array

* Learned how a Min Heap of size k helps avoid sorting the entire array.
* Understood the concept of maintaining only the most important k elements.

### Maximum Sum Combination

* Learned the powerful combination of Max Heap + Visited Set.
* Understood how to generate top k results efficiently without exploring all possibilities.
* Improved understanding of priority-based search techniques.

### Overall Takeaway

Today was all about mastering Heap data structures and Priority Queue patterns. These concepts are frequently used in coding interviews for optimization problems involving top-k elements, scheduling, and greedy selections.
