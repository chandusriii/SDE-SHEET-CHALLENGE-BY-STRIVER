class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head, k):
        """Reverse nodes in groups of k and leave the final smaller group unchanged."""
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
    print(f"Output: {linked_list_to_list(solution.reverseKGroup(head1, 2))}")
    print("Expected: [2, 1, 4, 3, 5]\n")

    head2 = build_linked_list([1, 2, 3, 4, 5])
    print("Input: head = 1 -> 2 -> 3 -> 4 -> 5, k = 3")
    print(f"Output: {linked_list_to_list(solution.reverseKGroup(head2, 3))}")
    print("Expected: [3, 2, 1, 4, 5]\n")

    head3 = build_linked_list([6, 1, 2, 3, 4, 7])
    print("Input: head = 6 -> 1 -> 2 -> 3 -> 4 -> 7, k = 4")
    print(f"Output: {linked_list_to_list(solution.reverseKGroup(head3, 4))}")
    print("Expected: [3, 2, 1, 6, 4, 7]\n")
