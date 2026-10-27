from __future__ import annotations
from typing import Optional


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        # Реализуем по одному проходу по каждому списку. Мы меняем только указатели между нодами, не используем новую память.
        # То есть затраты получаются O(n+m) по сложности и О(1) по памяти
        fake_node = ListNode()
        curr1 = list1
        curr2 = list2
        curr = fake_node
        while curr1 or curr2:
            if curr2 is None or ( curr1 is not None and curr1.val <= curr2.val):
                curr.next = curr1
                curr1 = curr1.next
            else:
                curr.next = curr2
                curr2 = curr2.next
            curr = curr.next
        return fake_node.next
