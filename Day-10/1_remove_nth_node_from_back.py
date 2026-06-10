class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head, n):
        """Remove the nth node from the end and return the updated head."""
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

    head1 = build_linked_list([1, 2, 3, 4, 5])
    print("Input: linkedList = 1 -> 2 -> 3 -> 4 -> 5, n = 2")
    print(f"Output: {linked_list_to_list(solution.removeNthFromEnd(head1, 2))}")
    print("Expected: [1, 2, 3, 5]\n")

    head2 = build_linked_list([5, 4, 3, 2, 1])
    print("Input: linkedList = 5 -> 4 -> 3 -> 2 -> 1, n = 5")
    print(f"Output: {linked_list_to_list(solution.removeNthFromEnd(head2, 5))}")
    print("Expected: [4, 3, 2, 1]\n")

    head3 = build_linked_list([9, 8, 7])
    print("Input: linkedList = 9 -> 8 -> 7, n = 1")
    print(f"Output: {linked_list_to_list(solution.removeNthFromEnd(head3, 1))}")
    print("Expected: [9, 8]\n")
