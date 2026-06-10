class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1, l2):
        """Add two reverse-order linked-list numbers and return the sum list."""
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


def build_linked_list(values):
    dummy = ListNode(0)
    tail = dummy

    for value in values:
        tail.next = ListNode(value)
        tail = tail.next

    return dummy.next


def linked_list_to_list(head):
    values = []

    while head:
        values.append(head.val)
        head = head.next

    return values


if __name__ == "__main__":
    solution = Solution()

    l1 = build_linked_list([5, 4])
    l2 = build_linked_list([4])
    print("Input: linkedList1 = [5, 4], linkedList2 = [4]")
    print(f"Output: {linked_list_to_list(solution.addTwoNumbers(l1, l2))}")
    print("Expected: [9, 4]\n")

    l3 = build_linked_list([4, 5, 6])
    l4 = build_linked_list([1, 2, 3])
    print("Input: linkedList1 = [4, 5, 6], linkedList2 = [1, 2, 3]")
    print(f"Output: {linked_list_to_list(solution.addTwoNumbers(l3, l4))}")
    print("Expected: [5, 7, 9]\n")

    l5 = build_linked_list([1])
    l6 = build_linked_list([8, 7])
    print("Input: linkedList1 = [1], linkedList2 = [8, 7]")
    print(f"Output: {linked_list_to_list(solution.addTwoNumbers(l5, l6))}")
    print("Expected: [9, 7]\n")
