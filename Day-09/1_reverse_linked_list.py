class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head):
        """Reverse a singly linked list and return the new head."""
        prev = None
        curr = head

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        return prev


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
    print("Input: head -> 1 -> 2 -> 3 -> 4 -> 5")
    print(f"Output: head -> {linked_list_to_list(solution.reverseList(head1))}")
    print("Expected: [5, 4, 3, 2, 1]\n")

    head2 = build_linked_list([6, 8])
    print("Input: head -> 6 -> 8")
    print(f"Output: head -> {linked_list_to_list(solution.reverseList(head2))}")
    print("Expected: [8, 6]\n")

    head3 = build_linked_list([1])
    print("Input: head -> 1")
    print(f"Output: head -> {linked_list_to_list(solution.reverseList(head3))}")
    print("Expected: [1]\n")
