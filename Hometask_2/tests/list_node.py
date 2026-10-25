class ListNode:
    def __init__(self, val: int, next=None):
        self.val = val
        self.next = next


def make_list(values):
    head = None
    tail = None
    for value in values:
        node = ListNode(value)
        if head is None:
            head = node
        else:
            tail.next = node
        tail = node
    return head


def list_values(head):
    result = []
    while head is not None:
        result.append(head.val)
        head = head.next
    return result
