# #45DaysSDEChallenge - Day 9

**Date:** June 9, 2026  
**Problems Solved Today:** 3  
**Sheet:** [Striver SDE Sheet](https://takeuforward.org/dsa/strivers-sde-sheet-top-coding-interview-problems)

---

## 1) Reverse a Linked List

- **TUF Problem:** [Reverse a LL](https://takeuforward.org/plus/dsa/problems/reverse-a-ll)

### Problem Statement
Given the head of a singly linked list, reverse the linked list and return the head of the modified list.

### What Striver Discussed
- Iterative pointer reversal is the optimal approach.
- Keep three references:
  1. `prev` stores the already reversed part.
  2. `curr` stores the node currently being processed.
  3. `next_node` temporarily stores the next original node before changing the link.
- Move forward until `curr` becomes `None`, then `prev` is the new head.

### Clean Python Solution
```python
class Solution:
    def reverseList(self, head):
        prev = None
        curr = head

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        return prev
```

### Test Cases
- **Input:** `head -> 1 -> 2 -> 3 -> 4 -> 5`
  - **Output:** `head -> 5 -> 4 -> 3 -> 2 -> 1`

- **Input:** `head -> 6 -> 8`
  - **Output:** `head -> 8 -> 6`

- **Now Your Turn:** `head -> 1`
  - **Output:** `head -> 1`

### Complexity
- **Time:** O(n) - Each node is visited once
- **Space:** O(1) - Only a few pointers are used

---

## 2) Find Middle of Linked List

- **TUF Problem:** [Find Middle of Linked List](https://takeuforward.org/plus/dsa/problems/find-middle-of-linked-list)

### Problem Statement
Given the head of a singly linked list, return the middle node.

If the linked list has an even number of nodes, return the second middle node.

### What Striver Discussed
- Use the tortoise and hare approach.
- Move `slow` by one node and `fast` by two nodes.
- When `fast` reaches the end, `slow` will be at the middle.
- Starting both pointers at `head` naturally returns the second middle for even length lists.

### Clean Python Solution
```python
class Solution:
    def middleOfLinkedList(self, head):
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow
```

### Test Cases
- **Input:** `head -> 3 -> 8 -> 7 -> 1 -> 3`
  - **Output:** `7`

- **Input:** `head -> 2 -> 9 -> 1 -> 4 -> 0 -> 4`
  - **Output:** `4`

- **Now Your Turn:** `head -> 3 -> 8 -> 1 -> 7 -> 0`
  - **Output:** `1`

### Complexity
- **Time:** O(n) - The list is traversed once
- **Space:** O(1) - Only two pointers are used

---

## 3) Merge Two Sorted Lists

- **TUF Problem:** [Merge two Sorted Lists](https://takeuforward.org/plus/dsa/problems/merge-two-sorted-lists)

### Problem Statement
Given the heads of two sorted linked lists, merge them into one sorted linked list and return the head of the merged list.

### What Striver Discussed
- Use a dummy node to simplify attaching nodes.
- Compare the current nodes from both lists.
- Attach the smaller node to the result and move that list pointer forward.
- Once one list is exhausted, attach the remaining part of the other list.

### Clean Python Solution
```python
class Solution:
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode(0)
        tail = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next

            tail = tail.next

        if list1:
            tail.next = list1
        else:
            tail.next = list2

        return dummy.next
```

### Test Cases
- **Input:** `list1 = head -> 2 -> 4 -> 7 -> 9`, `list2 = head -> 1 -> 2 -> 5 -> 6`
  - **Output:** `head -> 1 -> 2 -> 2 -> 4 -> 5 -> 6 -> 7 -> 9`

- **Input:** `list1 = head -> 1 -> 2 -> 3 -> 4`, `list2 = head -> 5 -> 6 -> 10`
  - **Output:** `head -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 10`

- **Now Your Turn:** `list1 = head -> 0 -> 2`, `list2 = head -> 1 -> 3 -> 5 -> 6`
  - **Output:** `head -> 0 -> 1 -> 2 -> 3 -> 5 -> 6`

### Complexity
- **Time:** O(n + m) - Each node from both lists is processed once
- **Space:** O(1) - Nodes are relinked in place

---

## Key Learnings From Today

### Reverse a Linked List
- Store the next node before reversing the current link.
- After the loop, `prev` becomes the new head of the reversed list.
- This is a classic example of careful pointer movement.

### Find Middle of Linked List
- Slow and fast pointers help find the middle in one pass.
- Moving `fast` two steps makes `slow` stop exactly at the middle.
- For even length lists, this approach returns the second middle.

### Merge Two Sorted Lists
- A dummy node keeps the merge logic clean.
- Reusing existing nodes avoids extra list allocation.
- Attaching the remaining list at the end works because both input lists are already sorted.
