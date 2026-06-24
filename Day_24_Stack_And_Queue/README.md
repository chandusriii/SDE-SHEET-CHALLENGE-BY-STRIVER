# 45DaysSDEChallenge - Day 24

Date: June 24, 2026
Problems Solved Today: 4
Sheet: Striver SDE Sheet

## 1) Implement Stack using Arrays

### Problem Statement

Implement a Last-In-First-Out (LIFO) Stack using an array supporting push, pop, top, and isEmpty operations.

### Approach

* Use an array (list) to store elements.
* Push elements at the end of the array.
* Pop elements from the end of the array.
* Top operation returns the last element without removing it.

### Time Complexity

* Push: O(1)
* Pop: O(1)
* Top: O(1)

### Space Complexity

O(n)

---

## 2) Implement Queue using Arrays

### Problem Statement

Implement a First-In-First-Out (FIFO) Queue using an array supporting push, pop, peek, and isEmpty operations.

### Approach

* Use an array with a front pointer.
* Insert elements at the rear.
* Remove elements from the front.
* Front pointer avoids shifting elements after each pop.

### Time Complexity

* Push: O(1)
* Pop: O(1)
* Peek: O(1)

### Space Complexity

O(n)

---

## 3) Implement Stack using Queue

### Problem Statement

Implement a Stack using a single Queue while maintaining LIFO behavior.

### Approach

* Push the new element into the queue.
* Rotate all previous elements behind the newly inserted element.
* The front of the queue always represents the top of the stack.

### Time Complexity

* Push: O(n)
* Pop: O(1)
* Top: O(1)

### Space Complexity

O(n)

---

## 4) Implement Queue using Stack

### Problem Statement

Implement a Queue using two Stacks while maintaining FIFO behavior.

### Approach

* Use one stack for insertion.
* Use another stack for deletion.
* Transfer elements only when the deletion stack becomes empty.
* This preserves queue order efficiently.

### Time Complexity

* Push: O(1)
* Pop: O(1) Amortized
* Peek: O(1) Amortized

### Space Complexity

O(n)

---

## Key Learnings

* Stack follows LIFO (Last In First Out).
* Queue follows FIFO (First In First Out).
* One data structure can be implemented using another.
* Queue rotation technique for implementing Stack using Queue.
* Two-stack transfer technique for implementing Queue using Stack.
* Understanding amortized complexity.

---

## Day 24 Summary

Solved 4 fundamental Stack and Queue implementation problems from Striver's SDE Sheet. Practiced array-based implementations and learned how to simulate Stack using Queue and Queue using Stack, strengthening core data structure concepts frequently asked in coding interviews.

