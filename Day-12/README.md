# #45DaysSDEChallenge - Day 12

**Date:** June 12, 2026  
**Problems Solved Today:** 3  
**Sheet:** [Striver SDE Sheet](https://takeuforward.org/dsa/strivers-sde-sheet-top-coding-interview-problems)

---

## 1) Flattening of Linked List

- **TUF Problem:** [Flattening of LL](https://takeuforward.org/plus/dsa/problems/flattening-of-ll)

### Problem Statement
Given a special linked list where each node has a `next` pointer and a `child` pointer, flatten all sorted child linked lists into one sorted linked list using only the `child` pointer.

### What Striver Discussed
- Treat every vertical child chain as a sorted linked list.
- Recursively flatten the list on the right using the `next` pointer.
- Merge the current child list with the already flattened right side.
- During merging, connect nodes through `child` and clear `next` pointers.

### Clean Python Solution
```python
class Solution:
    def merge(self, list1, list2):
        dummy = ListNode(-1)
        tail = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                tail.child = list1
                list1 = list1.child
            else:
                tail.child = list2
                list2 = list2.child

            tail = tail.child
            tail.next = None

        tail.child = list1 if list1 else list2

        return dummy.child

    def flattenLinkedList(self, head):
        if head is None or head.next is None:
            return head

        flattened_next = self.flattenLinkedList(head.next)
        head.next = None

        return self.merge(head, flattened_next)
```

### Test Cases
- **Input:** child lists = `[1, 2, 3]`, `[4, 5, 6]`, `[7, 8, 9, 10, 11, 12]`
  - **Output:** `head -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> 10 -> 11 -> 12`

- **Input:** child lists = `[2, 4, 5]`, `[10, 12, 13]`, `[16, 17, 20]`
  - **Output:** `head -> 2 -> 4 -> 5 -> 10 -> 12 -> 13 -> 16 -> 17 -> 20`

### Complexity
- **Time:** O(total nodes * number of head nodes) in the recursive pairwise merge approach
- **Space:** O(number of head nodes) due to recursion stack

---

## 2) Find the Starting Point in Linked List

- **TUF Problem:** [Find the starting point in LL](https://takeuforward.org/plus/dsa/problems/find-the-starting-point-in-ll)

### Problem Statement
Given the head of a singly linked list, return the node where a cycle begins. If no cycle exists, return `None`.

### What Striver Discussed
- Use Floyd's slow and fast pointer method to detect a cycle.
- When `slow` and `fast` meet, reset `slow` to the head.
- Move both pointers one step at a time.
- The node where they meet again is the starting point of the loop.

### Clean Python Solution
```python
class Solution:
    def findStartingPoint(self, head):
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow is fast:
                slow = head

                while slow is not fast:
                    slow = slow.next
                    fast = fast.next

                return slow

        return None
```

### Test Cases
- **Input:** `head = 1 -> 2 -> 3 -> 4 -> 5`, `pos = 1`
  - **Output:** `2`

- **Input:** `head = 1 -> 3 -> 7 -> 4`, `pos = -1`
  - **Output:** `null`

- **Now Your Turn:** `head = 6 -> 3 -> 7`, `pos = 0`
  - **Output:** `6`

### Complexity
- **Time:** O(n) - Each pointer moves through the list a limited number of times
- **Space:** O(1) - Only two pointers are used

---

## 3) Check if Linked List is Palindrome or Not

- **TUF Problem:** [Check if LL is palindrome or not](https://takeuforward.org/plus/dsa/problems/check-if-ll-is-palindrome-or-not)

### Problem Statement
Given the head of a singly linked list where each node stores one digit, check whether the sequence of digits forms a palindrome.

### What Striver Discussed
- Find the middle node using slow and fast pointers.
- Reverse the second half of the linked list.
- Compare the first half and reversed second half node by node.
- Restore the second half before returning the answer.

### Clean Python Solution
```python
class Solution:
    def reverse(self, head):
        previous = None
        current = head

        while current:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node

        return previous

    def isPalindrome(self, head):
        if head is None or head.next is None:
            return True

        slow = head
        fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        second_half = self.reverse(slow.next)
        first = head
        second = second_half

        while second:
            if first.val != second.val:
                slow.next = self.reverse(second_half)
                return False

            first = first.next
            second = second.next

        slow.next = self.reverse(second_half)

        return True
```

### Test Cases
- **Input:** `head = 3 -> 7 -> 5 -> 7 -> 3`
  - **Output:** `true`

- **Input:** `head = 1 -> 1 -> 2 -> 1`
  - **Output:** `false`

- **Now Your Turn:** `head = 9 -> 9 -> 9 -> 9`
  - **Output:** `true`

### Complexity
- **Time:** O(n) - The list is traversed a constant number of times
- **Space:** O(1) - The second half is reversed in place

---

## Key Learnings From Today

### Flattening of Linked List
- A multi-level linked list can be reduced to repeated sorted-list merges.
- The final flattened list should use `child` pointers, not `next` pointers.
- Clearing `next` pointers avoids carrying old horizontal links into the answer.

### Starting Point of Loop
- Cycle detection and cycle entry discovery are two separate steps.
- After the first meeting point, moving one pointer from head and one from the meeting node gives the cycle start.
- The answer is the node reference, not the index.

### Palindrome Linked List
- Reversing only the second half keeps the algorithm O(1) in extra space.
- Comparing while the second half exists handles both odd and even lengths.
- Restoring the reversed half keeps the original linked list unchanged.

