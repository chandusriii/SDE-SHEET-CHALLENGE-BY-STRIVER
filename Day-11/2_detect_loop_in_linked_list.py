class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    def hasCycle(self, head):
        """Return True if the linked list contains a cycle."""
        slow = head
        fast = head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

            if slow is fast:
                return True

        return False


def build_linked_list(values, pos=-1):
    nodes = [Node(value) for value in values]

    for index in range(len(nodes) - 1):
        nodes[index].next = nodes[index + 1]

    if pos != -1 and nodes:
        nodes[-1].next = nodes[pos]

    return nodes[0] if nodes else None


if __name__ == "__main__":
    solution = Solution()

    head1 = build_linked_list([1, 2, 3, 4, 5], pos=1)
    print("Input: head = 1 -> 2 -> 3 -> 4 -> 5, pos = 1")
    print(f"Output: {solution.hasCycle(head1)}")
    print("Expected: True\n")

    head2 = build_linked_list([1, 3, 7, 4], pos=-1)
    print("Input: head = 1 -> 3 -> 7 -> 4, pos = -1")
    print(f"Output: {solution.hasCycle(head2)}")
    print("Expected: False\n")

    head3 = build_linked_list([6, 3, 7], pos=0)
    print("Input: head = 6 -> 3 -> 7, pos = 0")
    print(f"Output: {solution.hasCycle(head3)}")
    print("Expected: True\n")
