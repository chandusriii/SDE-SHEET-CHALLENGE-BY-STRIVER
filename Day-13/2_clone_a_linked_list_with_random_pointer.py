class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.random = None


class Solution:
    def copyRandomList(self, head):
        """Create a deep copy of a linked list with next and random pointers."""
        if not head:
            return None

        curr = head
        while curr:
            copy = Node(curr.val)
            copy.next = curr.next
            curr.next = copy
            curr = copy.next

        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next

        curr = head
        copy_head = head.next

        while curr:
            copy = curr.next
            curr.next = copy.next

            if copy.next:
                copy.next = copy.next.next

            curr = curr.next

        return copy_head


def build_random_list(values):
    nodes = [Node(value) for value, _ in values]

    for index in range(len(nodes) - 1):
        nodes[index].next = nodes[index + 1]

    for index, (_, random_index) in enumerate(values):
        if random_index != -1:
            nodes[index].random = nodes[random_index]

    return nodes[0] if nodes else None


def values_from_next_pointers(head):
    values = []

    while head:
        values.append(head.val)
        head = head.next

    return values


def is_deep_copy(original, copy):
    original_nodes = []
    copy_nodes = []

    curr = original
    while curr:
        original_nodes.append(curr)
        curr = curr.next

    curr = copy
    while curr:
        copy_nodes.append(curr)
        curr = curr.next

    if len(original_nodes) != len(copy_nodes):
        return False

    mapping = {original_nodes[index]: copy_nodes[index] for index in range(len(original_nodes))}

    for original_node, copy_node in zip(original_nodes, copy_nodes):
        if original_node is copy_node or original_node.val != copy_node.val:
            return False

        expected_random = mapping.get(original_node.random)
        if copy_node.random is not expected_random:
            return False

    return True


if __name__ == "__main__":
    solution = Solution()

    head1 = build_random_list([[1, -1], [2, 0], [3, 4], [4, 1], [5, 2]])
    copy1 = solution.copyRandomList(head1)
    print("Input: [[1, -1], [2, 0], [3, 4], [4, 1], [5, 2]]")
    print(f"Output: {values_from_next_pointers(copy1)}, {is_deep_copy(head1, copy1)}")
    print("Expected: [1, 2, 3, 4, 5], True\n")

    head2 = build_random_list([[5, -1], [3, -1], [2, 1], [1, 1]])
    copy2 = solution.copyRandomList(head2)
    print("Input: [[5, -1], [3, -1], [2, 1], [1, 1]]")
    print(f"Output: {values_from_next_pointers(copy2)}, {is_deep_copy(head2, copy2)}")
    print("Expected: [5, 3, 2, 1], True\n")

    head3 = build_random_list([[-1, -1], [-2, -1], [-3, -1], [10, -1]])
    copy3 = solution.copyRandomList(head3)
    print("Input: [[-1, -1], [-2, -1], [-3, -1], [10, -1]]")
    print(f"Output: {values_from_next_pointers(copy3)}, {is_deep_copy(head3, copy3)}")
    print("Expected: [-1, -2, -3, 10], True\n")
