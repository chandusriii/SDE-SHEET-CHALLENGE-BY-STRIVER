# #45DaysSDEChallenge - Day 11

**Date:** June 11, 2026  
**Problems Solved Today:** 3  
**Sheet:** [Striver SDE Sheet](https://takeuforward.org/dsa/strivers-sde-sheet-top-coding-interview-problems)

---

## 1) Find the Intersection Point of Y Linked List

- **TUF Problem:** [Find the intersection point of Y LL](https://takeuforward.org/plus/dsa/problems/find-the-intersection-point-of-y-ll)

### Problem Statement
Given the heads of two singly linked lists, return the node where the two linked lists intersect. If they do not intersect, return `None`.

The intersection is based on node reference, not just equal values.

### What Striver Discussed
- Use two pointers, one starting at `headA` and the other at `headB`.
- Move both pointers one step at a time.
- When a pointer reaches the end, redirect it to the head of the other list.
- After at most `m + n` moves, both pointers either meet at the intersection node or become `None`.
- This balances the distance traveled without calculating list lengths.

### Clean Python Solution
```python
class Solution:
    def getIntersectionNode(self, headA, headB):
        pointer_a = headA
        pointer_b = headB

        while pointer_a is not pointer_b:
            pointer_a = headB if pointer_a is None else pointer_a.next
            pointer_b = headA if pointer_b is None else pointer_b.next

        return pointer_a
```

### Test Cases
- **Input:** `listA = 1 -> 2 -> 3 -> 4 -> 5`, `listB = 7 -> 8 -> 4 -> 5`
  - **Output:** `4`

- **Input:** `listA = 1 -> 2 -> 3`, `listB = 8 -> 9`
  - **Output:** `null`

- **Now Your Turn:** `intersectVal = 4`, `skipA = 0`, `skipB = 0`, `listA = 4 -> 5 -> 6`, `listB = 4 -> 5 -> 6`
  - **Output:** `4`

### Complexity
- **Time:** O(m + n) - Each pointer traverses both lists at most once
- **Space:** O(1) - Only two pointers are used

---

## 2) Detect a Loop in Linked List

- **TUF Problem:** [Detect a loop in LL](https://takeuforward.org/plus/dsa/problems/detect-a-loop-in-ll)

### Problem Statement
Given the head of a singly linked list, return `True` if a loop exists. Otherwise, return `False`.

### What Striver Discussed
- Use Floyd's cycle detection algorithm.
- Move `slow` by one step and `fast` by two steps.
- If there is a cycle, the two pointers will eventually meet.
- If `fast` or `fast.next` becomes `None`, the list has no cycle.

### Clean Python Solution
```python
class Solution:
    def hasCycle(self, head):
        slow = head
        fast = head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

            if slow is fast:
                return True

        return False
```

### Test Cases
- **Input:** `head = 1 -> 2 -> 3 -> 4 -> 5`, `pos = 1`
  - **Output:** `true`

- **Input:** `head = 1 -> 3 -> 7 -> 4`, `pos = -1`
  - **Output:** `false`

- **Now Your Turn:** `head = 6 -> 3 -> 7`, `pos = 0`
  - **Output:** `true`

### Complexity
- **Time:** O(n) - The fast pointer visits nodes until it reaches the end or meets slow
- **Space:** O(1) - Only two pointers are used

---

## 3) Reverse Linked List in Groups of K

- **TUF Problem:** [Reverse LL in group of given size K](https://takeuforward.org/plus/dsa/problems/reverse-ll-in-group-of-given-size-k)

### Problem Statement
Given the head of a singly linked list and an integer `k`, reverse nodes in groups of `k`. If the remaining nodes are fewer than `k`, keep them unchanged.

### What Striver Discussed
- Use a dummy node before the head to handle the first group cleanly.
- Before reversing a group, find the kth node from the previous group's tail.
- If a kth node does not exist, stop and leave the remaining nodes unchanged.
- Reverse links only inside the current group.
- Reconnect the reversed group with the previous and next parts of the list.

### Clean Python Solution
```python
class Solution:
    def reverseKGroup(self, head, k):
        if head is None or k == 1:
            return head

        dummy = ListNode(0)
        dummy.next = head
        group_previous = dummy

        while True:
            kth = self.getKthNode(group_previous, k)

            if kth is None:
                break

            group_next = kth.next
            previous = group_next
            current = group_previous.next

            while current is not group_next:
                next_node = current.next
                current.next = previous
                previous = current
                current = next_node

            old_group_head = group_previous.next
            group_previous.next = kth
            group_previous = old_group_head

        return dummy.next

    def getKthNode(self, current, k):
        while current and k > 0:
            current = current.next
            k -= 1

        return current
```

### Test Cases
- **Input:** `head = 1 -> 2 -> 3 -> 4 -> 5`, `k = 2`
  - **Output:** `head -> 2 -> 1 -> 4 -> 3 -> 5`

- **Input:** `head = 1 -> 2 -> 3 -> 4 -> 5`, `k = 3`
  - **Output:** `head -> 3 -> 2 -> 1 -> 4 -> 5`

- **Now Your Turn:** `head = 6 -> 1 -> 2 -> 3 -> 4 -> 7`, `k = 4`
  - **Output:** `head -> 3 -> 2 -> 1 -> 6 -> 4 -> 7`

### Complexity
- **Time:** O(n) - Each node is visited a constant number of times
- **Space:** O(1) - Nodes are reversed in place

---

## Key Learnings From Today

### Intersection Point of Y Linked List
- Intersection means the same node object, not just the same value.
- Switching heads makes both pointers cover equal total distance.
- The original linked list structure remains unchanged.

### Detect a Loop
- Slow and fast pointers can detect a cycle without extra memory.
- If a cycle exists, the fast pointer eventually catches the slow pointer.
- If the fast pointer reaches `None`, there is no loop.

### Reverse in K Groups
- Always confirm a full group of `k` nodes exists before reversing.
- A dummy node simplifies reconnection around the head.
- The last incomplete group must stay in original order.
