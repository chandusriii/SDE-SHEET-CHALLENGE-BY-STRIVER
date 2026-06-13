# #45DaysSDEChallenge - Day 13

**Date:** June 13, 2026  
**Problems Solved Today:** 3  
**Sheet:** [Striver SDE Sheet](https://takeuforward.org/dsa/strivers-sde-sheet-top-coding-interview-problems)

---

## 1) Rotate a Linked List

- **TUF Problem:** [Rotate a LL](https://takeuforward.org/plus/dsa/problems/rotate-a-ll)

### Problem Statement
Given the head of a singly linked list and an integer `k`, rotate the linked list to the right by `k` places. Node values should not be changed; only links between nodes should be modified.

### What Striver Discussed
- First calculate the length of the linked list and keep track of the tail node.
- Since rotating by the list length gives the same list, reduce `k` using `k % length`.
- Connect the tail to the head to temporarily make the list circular.
- The new tail will be at position `length - k` from the start.
- Break the circular link after the new tail.

### Clean Python Solution
```python
class Solution:
    def rotateRight(self, head, k):
        if not head or not head.next or k == 0:
            return head

        length = 1
        tail = head

        while tail.next:
            tail = tail.next
            length += 1

        k = k % length

        if k == 0:
            return head

        tail.next = head

        steps = length - k
        new_tail = head

        for _ in range(steps - 1):
            new_tail = new_tail.next

        new_head = new_tail.next
        new_tail.next = None

        return new_head
```

### Test Cases
- **Input:** `head = 1 -> 2 -> 3 -> 4 -> 5`, `k = 2`  
  **Output:** `head -> 4 -> 5 -> 1 -> 2 -> 3`

- **Input:** `head = 1 -> 2 -> 3 -> 4 -> 5`, `k = 4`  
  **Output:** `head -> 2 -> 3 -> 4 -> 5 -> 1`

- **Now Your Turn:** `head = 1 -> 2 -> 3 -> 4 -> 5`, `k = 7`  
  **Output:** `head -> 4 -> 5 -> 1 -> 2 -> 3`

### Complexity
- **Time:** O(n) - One traversal to find the length and one traversal to find the new tail
- **Space:** O(1) - Only pointers are changed

---

## 2) Clone a Linked List with Random and Next Pointer

- **TUF Problem:** [Clone a LL with random and next pointer](https://takeuforward.org/plus/dsa/problems/clone-a-ll-with-random-and-next-pointer)

### Problem Statement
Given the head of a linked list where each node has a `next` pointer and a `random` pointer, create a deep copy of the list. The copied nodes must be new nodes, and their `random` pointers must point to the corresponding copied nodes.

### What Striver Discussed
- Insert each copied node right after its original node.
- Use the original node's `random` pointer to assign the copied node's `random` pointer.
- Separate the combined list into the original list and the copied list.
- This avoids using an extra hash map.

### Clean Python Solution
```python
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.random = None


class Solution:
    def copyRandomList(self, head):
        if not head:
            return None

        curr = head
        while curr:
            copy = Node(curr.val)
            copy.next = curr.next
            curr.next = copy
            curr = copy.next

        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next

        curr = head
        copy_head = head.next

        while curr:
            copy = curr.next
            curr.next = copy.next

            if copy.next:
                copy.next = copy.next.next

            curr = curr.next

        return copy_head
```

### Test Cases
- **Input:** `[[1, -1], [2, 0], [3, 4], [4, 1], [5, 2]]`  
  **Output:** `1 2 3 4 5, true`

- **Input:** `[[5, -1], [3, -1], [2, 1], [1, 1]]`  
  **Output:** `5 3 2 1, true`

- **Now Your Turn:** `[[-1, -1], [-2, -1], [-3, -1], [10, -1]]`  
  **Output:** `-1 -2 -3 10, true`

### Complexity
- **Time:** O(n) - The list is traversed three times
- **Space:** O(1) - No extra hash map is used, apart from the newly created nodes

---

## 3) 3 Sum

- **TUF Problem:** [3 Sum](https://takeuforward.org/plus/dsa/problems/3-sum)

### Problem Statement
Given an integer array `nums`, return all unique triplets `[nums[i], nums[j], nums[k]]` such that the three indices are different and the sum of the three values is `0`.

### What Striver Discussed
- Sort the array first.
- Fix one element and use two pointers to search for the remaining pair.
- Skip duplicate fixed elements.
- After finding a valid triplet, skip duplicate left and right values.
- This gives unique triplets without using a set for the final answer.

### Clean Python Solution
```python
class Solution:
    def threeSum(self, nums):
        nums.sort()
        n = len(nums)
        result = []

        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = n - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                elif total < 0:
                    left += 1
                else:
                    right -= 1

        return result
```

### Test Cases
- **Input:** `nums = [2, -2, 0, 3, -3, 5]`  
  **Output:** `[[-3, -2, 5], [-3, 0, 3], [-2, 0, 2]]`

- **Input:** `nums = [2, -1, -1, 3, -1]`  
  **Output:** `[[-1, -1, 2]]`

- **Now Your Turn:** `nums = [8, -6, 5, 4]`  
  **Output:** `[]`

### Complexity
- **Time:** O(n^2) - For every fixed index, the remaining part is scanned using two pointers
- **Space:** O(1) - Ignoring the output list, only pointers are used

---

## Key Learnings From Today

### Rotate a Linked List
- Large values of `k` can be reduced using modulo with the length.
- Making the linked list circular simplifies reconnecting the rotated parts.
- The new tail is found at `length - k` steps from the original head.

### Clone a Linked List with Random Pointer
- Interleaving copied nodes with original nodes helps map original nodes to copied nodes without a hash map.
- `curr.random.next` gives the copied version of the random target.
- Separating the lists carefully restores the original list and returns the deep copy.

### 3 Sum
- Sorting makes duplicate handling and two-pointer searching easier.
- Skipping duplicates is necessary to avoid repeated triplets.
- If no three numbers sum to zero, the correct output is an empty list.
