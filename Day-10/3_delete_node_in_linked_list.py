class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteNode(self, node):
        """Delete the given non-tail node in O(1) time."""
        node.val = node.next.val
        node.next = node.next.next


def build_linked_list(values):
    dummy = ListNode(0)
    tail = dummy

    for value in values:
        tail.next = ListNode(value)
        tail = tail.next

    return dummy.next


def find_node(head, target):
    while head:
        if head.val == target:
            return head

        head = head.next

    return None


def linked_list_to_list(head):
    values = []

    while head:
        values.append(head.val)
        head = head.next

    return values


if __name__ == "__main__":
    solution = Solution()

    head1 = build_linked_list([4, 5, 1, 9])
    node1 = find_node(head1, 5)
    solution.deleteNode(node1)
    print("Input: head = [4, 5, 1, 9], node = 5")
    print(f"Output: {linked_list_to_list(head1)}")
    print("Expected: [4, 1, 9]\n")

    head2 = build_linked_list([1, 2, 3, 4])
    node2 = find_node(head2, 3)
    solution.deleteNode(node2)
    print("Input: head = [1, 2, 3, 4], node = 3")
    print(f"Output: {linked_list_to_list(head2)}")
    print("Expected: [1, 2, 4]\n")

    head3 = build_linked_list([1, 2])
    node3 = find_node(head3, 1)
    solution.deleteNode(node3)
    print("Input: head = [1, 2], node = 1")
    print(f"Output: {linked_list_to_list(head3)}")
    print("Expected: [2]\n")
