from typing import List
import heapq


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        heap = []

        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i, lists[i]))

        dummy = ListNode(0)
        tail = dummy

        while heap:
            value, array_idx, node = heapq.heappop(heap)

            tail.next = node
            tail = tail.next

            if node.next:
                heapq.heappush(heap, (node.next.val, array_idx, node.next))

        tail.next = None
        return dummy.next

# Время: O(N log K), где N — общее число элементов, K — число массивов.
# Память: O(K) для кучи, O(N) для результата.
