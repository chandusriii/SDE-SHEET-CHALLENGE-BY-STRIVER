class ListNode:
    def __init__(self, val=0, next=None, child=None):
        self.val = val
        self.next = next
        self.child = child


class Solution:
    def merge(self, list1, list2):
        """Merge two sorted child-linked lists."""
        dummy = ListNode(-1)
        tail = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                tail.child = list1
                list1 = list1.child
            else:
                tail.child = list2
                list2 = list2.child

            tail = tail.child
            tail.next = None

        tail.child = list1 if list1 else list2

        return dummy.child

    def flattenLinkedList(self, head):
        """Flatten all sorted child lists into one sorted list using child pointers."""
        if head is None or head.next is None:
            return head

        flattened_next = self.flattenLinkedList(head.next)
        head.next = None

        return self.merge(head, flattened_next)


def build_child_list(values):
    dummy = ListNode(0)
    tail = dummy

    for value in values:
        tail.child = ListNode(value)
        tail = tail.child

    return dummy.child


def build_special_linked_list(columns):
    heads = [build_child_list(column) for column in columns]

    for index in range(len(heads) - 1):
        heads[index].next = heads[index + 1]

    return heads[0] if heads else None


def child_list_to_list(head):
    values = []

    while head:
        values.append(head.val)
        head = head.child

    return values


if __name__ == "__main__":
    solution = Solution()

    head1 = build_special_linked_list([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9, 10, 11, 12],
    ])
    print("Input: child lists = [1, 2, 3], [4, 5, 6], [7, 8, 9, 10, 11, 12]")
    print(f"Output: head -> {child_list_to_list(solution.flattenLinkedList(head1))}")
    print("Expected: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]\n")

    head2 = build_special_linked_list([
        [2, 4, 5],
        [10, 12, 13],
        [16, 17, 20],
    ])
    print("Input: child lists = [2, 4, 5], [10, 12, 13], [16, 17, 20]")
    print(f"Output: head -> {child_list_to_list(solution.flattenLinkedList(head2))}")
    print("Expected: [2, 4, 5, 10, 12, 13, 16, 17, 20]\n")

