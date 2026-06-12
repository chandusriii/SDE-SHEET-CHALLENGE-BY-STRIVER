class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def findStartingPoint(self, head):
        """Return the node where the cycle starts, or None if no cycle exists."""
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow is fast:
                slow = head

                while slow is not fast:
                    slow = slow.next
                    fast = fast.next

                return slow

        return None


def build_linked_list(values, pos=-1):
    nodes = [ListNode(value) for value in values]

    for index in range(len(nodes) - 1):
        nodes[index].next = nodes[index + 1]

    if pos != -1 and nodes:
        nodes[-1].next = nodes[pos]

    return nodes[0] if nodes else None


def node_value(node):
    return None if node is None else node.val


if __name__ == "__main__":
    solution = Solution()

    head1 = build_linked_list([1, 2, 3, 4, 5], pos=1)
    print("Input: head = 1 -> 2 -> 3 -> 4 -> 5, pos = 1")
    print(f"Output: {node_value(solution.findStartingPoint(head1))}")
    print("Expected: 2\n")

    head2 = build_linked_list([1, 3, 7, 4], pos=-1)
    print("Input: head = 1 -> 3 -> 7 -> 4, pos = -1")
    print(f"Output: {node_value(solution.findStartingPoint(head2))}")
    print("Expected: None\n")

    head3 = build_linked_list([6, 3, 7], pos=0)
    print("Input: head = 6 -> 3 -> 7, pos = 0")
    print(f"Output: {node_value(solution.findStartingPoint(head3))}")
    print("Expected: 6\n")

