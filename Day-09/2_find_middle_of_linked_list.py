class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleOfLinkedList(self, head):
        """Return the middle node, choosing the second middle for even length lists."""
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow


def build_linked_list(values):
    dummy = ListNode(0)
    tail = dummy

    for value in values:
        tail.next = ListNode(value)
        tail = tail.next

    return dummy.next


if __name__ == "__main__":
    solution = Solution()

    head1 = build_linked_list([3, 8, 7, 1, 3])
    print("Input: head -> 3 -> 8 -> 7 -> 1 -> 3")
    print(f"Output: {solution.middleOfLinkedList(head1).val}")
    print("Expected: 7\n")

    head2 = build_linked_list([2, 9, 1, 4, 0, 4])
    print("Input: head -> 2 -> 9 -> 1 -> 4 -> 0 -> 4")
    print(f"Output: {solution.middleOfLinkedList(head2).val}")
    print("Expected: 4\n")

    head3 = build_linked_list([3, 8, 1, 7, 0])
    print("Input: head -> 3 -> 8 -> 1 -> 7 -> 0")
    print(f"Output: {solution.middleOfLinkedList(head3).val}")
    print("Expected: 1\n")
