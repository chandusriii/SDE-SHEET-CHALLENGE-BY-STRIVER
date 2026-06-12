class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


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
        """Return True if the linked list values read the same both ways."""
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


def build_linked_list(values):
    dummy = ListNode(0)
    tail = dummy

    for value in values:
        tail.next = ListNode(value)
        tail = tail.next

    return dummy.next


if __name__ == "__main__":
    solution = Solution()

    head1 = build_linked_list([3, 7, 5, 7, 3])
    print("Input: head = 3 -> 7 -> 5 -> 7 -> 3")
    print(f"Output: {solution.isPalindrome(head1)}")
    print("Expected: True\n")

    head2 = build_linked_list([1, 1, 2, 1])
    print("Input: head = 1 -> 1 -> 2 -> 1")
    print(f"Output: {solution.isPalindrome(head2)}")
    print("Expected: False\n")

    head3 = build_linked_list([9, 9, 9, 9])
    print("Input: head = 9 -> 9 -> 9 -> 9")
    print(f"Output: {solution.isPalindrome(head3)}")
    print("Expected: True\n")

