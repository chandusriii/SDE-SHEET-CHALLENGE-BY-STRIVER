class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1, list2):
        """Merge two sorted linked lists and return the merged head."""
        dummy = ListNode(0)
        tail = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next

            tail = tail.next

        if list1:
            tail.next = list1
        else:
            tail.next = list2

        return dummy.next


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

    list1 = build_linked_list([2, 4, 7, 9])
    list2 = build_linked_list([1, 2, 5, 6])
    print("Input: list1 = head -> 2 -> 4 -> 7 -> 9, list2 = head -> 1 -> 2 -> 5 -> 6")
    print(f"Output: head -> {linked_list_to_list(solution.mergeTwoLists(list1, list2))}")
    print("Expected: [1, 2, 2, 4, 5, 6, 7, 9]\n")

    list3 = build_linked_list([1, 2, 3, 4])
    list4 = build_linked_list([5, 6, 10])
    print("Input: list1 = head -> 1 -> 2 -> 3 -> 4, list2 = head -> 5 -> 6 -> 10")
    print(f"Output: head -> {linked_list_to_list(solution.mergeTwoLists(list3, list4))}")
    print("Expected: [1, 2, 3, 4, 5, 6, 10]\n")

    list5 = build_linked_list([0, 2])
    list6 = build_linked_list([1, 3, 5, 6])
    print("Input: list1 = head -> 0 -> 2, list2 = head -> 1 -> 3 -> 5 -> 6")
    print(f"Output: head -> {linked_list_to_list(solution.mergeTwoLists(list5, list6))}")
    print("Expected: [0, 1, 2, 3, 5, 6]\n")
