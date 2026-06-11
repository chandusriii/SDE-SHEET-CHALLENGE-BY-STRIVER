class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def getIntersectionNode(self, headA, headB):
        """Return the node where two linked lists intersect, or None."""
        pointer_a = headA
        pointer_b = headB

        while pointer_a is not pointer_b:
            pointer_a = headB if pointer_a is None else pointer_a.next
            pointer_b = headA if pointer_b is None else pointer_b.next

        return pointer_a


def build_linked_list(values):
    dummy = ListNode(0)
    tail = dummy

    for value in values:
        tail.next = ListNode(value)
        tail = tail.next

    return dummy.next


def get_tail(head):
    while head and head.next:
        head = head.next

    return head


def get_node_at(head, index):
    for _ in range(index):
        head = head.next

    return head


def build_intersecting_lists(list_a_values, list_b_prefix_values, skip_a):
    head_a = build_linked_list(list_a_values)
    intersection = get_node_at(head_a, skip_a)
    head_b = build_linked_list(list_b_prefix_values)

    if head_b is None:
        head_b = intersection
    else:
        get_tail(head_b).next = intersection

    return head_a, head_b


def node_value(node):
    return None if node is None else node.val


if __name__ == "__main__":
    solution = Solution()

    head_a1, head_b1 = build_intersecting_lists([1, 2, 3, 4, 5], [7, 8], 3)
    print("Input: listA = 1 -> 2 -> 3 -> 4 -> 5, listB = 7 -> 8 -> 4 -> 5")
    print(f"Output: {node_value(solution.getIntersectionNode(head_a1, head_b1))}")
    print("Expected: 4\n")

    head_a2 = build_linked_list([1, 2, 3])
    head_b2 = build_linked_list([8, 9])
    print("Input: listA = 1 -> 2 -> 3, listB = 8 -> 9")
    print(f"Output: {node_value(solution.getIntersectionNode(head_a2, head_b2))}")
    print("Expected: None\n")

    head_a3 = build_linked_list([4, 5, 6])
    head_b3 = head_a3
    print("Input: listA = 4 -> 5 -> 6, listB = 4 -> 5 -> 6")
    print(f"Output: {node_value(solution.getIntersectionNode(head_a3, head_b3))}")
    print("Expected: 4\n")
