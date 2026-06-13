class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head, k):
        """Rotate the linked list to the right by k places."""
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
    print("Input: head = 1 -> 2 -> 3 -> 4 -> 5, k = 2")
    print(f"Output: {linked_list_to_list(solution.rotateRight(head1, 2))}")
    print("Expected: [4, 5, 1, 2, 3]\n")

    head2 = build_linked_list([1, 2, 3, 4, 5])
    print("Input: head = 1 -> 2 -> 3 -> 4 -> 5, k = 4")
    print(f"Output: {linked_list_to_list(solution.rotateRight(head2, 4))}")
    print("Expected: [2, 3, 4, 5, 1]\n")

    head3 = build_linked_list([1, 2, 3, 4, 5])
    print("Input: head = 1 -> 2 -> 3 -> 4 -> 5, k = 7")
    print(f"Output: {linked_list_to_list(solution.rotateRight(head3, 7))}")
    print("Expected: [4, 5, 1, 2, 3]\n")
