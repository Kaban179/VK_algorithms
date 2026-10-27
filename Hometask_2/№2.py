from __future__ import annotations
from typing import Optional


class Solution:
    def middleNode(self, head: ListNode | None) -> ListNode | None:
        #Используем метод двух указателей. Когда быстрый указатель выйдет за границу списка, медленный будет как раз на середине списка
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        return slow
