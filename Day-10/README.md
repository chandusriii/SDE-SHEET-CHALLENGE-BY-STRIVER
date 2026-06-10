# #45DaysSDEChallenge - Day 10

**Date:** June 10, 2026  
**Problems Solved Today:** 3  
**Sheet:** [Striver SDE Sheet](https://takeuforward.org/dsa/strivers-sde-sheet-top-coding-interview-problems)

---

## 1) Remove Nth Node From the Back of Linked List

- **TUF Problem:** [Remove Nth node from the back of the LL](https://takeuforward.org/plus/dsa/problems/remove-nth-node-from-the-back-of-the-ll)

### Problem Statement
Given the head of a singly linked list and an integer `n`, remove the nth node from the back of the linked list and return the modified head.

### What Striver Discussed
- Use two pointers to remove the target node in one pass.
- Add a dummy node before the head to handle deletion of the first node cleanly.
- Move `fast` ahead by `n + 1` steps from the dummy node.
- Move `slow` and `fast` together until `fast` reaches the end.
- `slow.next` will be the node to delete.

### Clean Python Solution
```python
class Solution:
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0)
        dummy.next = head

        slow = dummy
        fast = dummy

        for _ in range(n + 1):
            fast = fast.next

        while fast:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next

        return dummy.next
```

### Test Cases
- **Input:** `linkedList = 1 -> 2 -> 3 -> 4 -> 5`, `n = 2`
  - **Output:** `1 -> 2 -> 3 -> 5`

- **Input:** `linkedList = 5 -> 4 -> 3 -> 2 -> 1`, `n = 5`
  - **Output:** `4 -> 3 -> 2 -> 1`

- **Now Your Turn:** `linkedList = 9 -> 8 -> 7`, `n = 1`
  - **Output:** `9 -> 8`

### Complexity
- **Time:** O(n) - The linked list is traversed once
- **Space:** O(1) - Only two pointers and one dummy node are used

---

## 2) Add Two Numbers in Linked List

- **TUF Problem:** [Add two numbers in Linked List](https://takeuforward.org/plus/dsa/problems/add-two-numbers-in-linked-list)

### Problem Statement
Given two non-empty linked lists representing two non-negative integers in reverse order, add the numbers and return the sum as a linked list in reverse order.

### What Striver Discussed
- Use a dummy node to build the answer list.
- Traverse both lists while carrying the overflow digit.
- At each step, add `l1`, `l2`, and `carry`.
- Store `total % 10` in the new node and update `carry = total // 10`.
- Continue while either list has nodes or a carry remains.

### Clean Python Solution
```python
class Solution:
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode(0)
        current = dummy
        carry = 0

        while l1 or l2 or carry:
            total = carry

            if l1:
                total += l1.val
                l1 = l1.next

            if l2:
                total += l2.val
                l2 = l2.next

            carry = total // 10
            current.next = ListNode(total % 10)
            current = current.next

        return dummy.next
```

### Test Cases
- **Input:** `linkedList1 = [5, 4]`, `linkedList2 = [4]`
  - **Output:** `[9, 4]`

- **Input:** `linkedList1 = [4, 5, 6]`, `linkedList2 = [1, 2, 3]`
  - **Output:** `[5, 7, 9]`

- **Now Your Turn:** `linkedList1 = [1]`, `linkedList2 = [8, 7]`
  - **Output:** `[9, 7]`

### Complexity
- **Time:** O(max(n, m)) - Each node from both lists is processed once
- **Space:** O(max(n, m)) - A new linked list is created for the sum

---

## 3) Delete Node in a Linked List O(1)

- **TUF Problem:** [Delete Node in a Linked List O(1)](https://takeuforward.org/plus/dsa/problems/delete-node-in-a-linked-list-o1)

### Problem Statement
Given only access to a node in a singly linked list, delete that node in-place. The given node is guaranteed not to be the tail.

### What Striver Discussed
- Since the head is not available, the previous node cannot be reached.
- Copy the next node's value into the current node.
- Skip the next node by changing `node.next`.
- This effectively deletes the given node in O(1) time.

### Clean Python Solution
```python
class Solution:
    def deleteNode(self, node):
        node.val = node.next.val
        node.next = node.next.next
```

### Test Cases
- **Input:** `head = [4, 5, 1, 9]`, `node = 5`
  - **Output:** `[4, 1, 9]`

- **Input:** `head = [1, 2, 3, 4]`, `node = 3`
  - **Output:** `[1, 2, 4]`

- **Now Your Turn:** `head = [1, 2]`, `node = 1`
  - **Output:** `[2]`

### Complexity
- **Time:** O(1) - Only the given node is modified
- **Space:** O(1) - No extra data structure is used

---

## Key Learnings From Today

### Remove Nth Node From Back
- A dummy node makes head deletion simple.
- Keeping a fixed gap between `fast` and `slow` helps find the previous node of the target in one pass.

### Add Two Numbers
- Linked lists store digits in reverse order, so addition can be done from head to tail.
- Carry handling is the key part, especially when one list is longer or an extra final carry remains.

### Delete Node in O(1)
- When the previous node is unavailable, copy the next node into the current node.
- This works only because the node to delete is guaranteed not to be the tail.
