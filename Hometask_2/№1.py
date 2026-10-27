from __future__ import annotations
from typing import Optional


class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        if not head:
            return None
        prev = head
        cur = head.next
        head.next = None

        while cur:
            next = cur.next # Сохран яем следующий узел
            cur.next = prev # Разворачиваем ссылку на предыдущий узел
            
            prev = cur # Сдв игаем предыдущий указатель
            cur = next  # Переходим к следующему узлу
        
        return prev

         # O(n) по времени: каждый узел посещаем ровно один раз.
        # O(1) по памяти: используем только три указателя.
