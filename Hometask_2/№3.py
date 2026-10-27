from __future__ import annotations
from typing import Optional


class Solution:
    def removeElements(self, head: ListNode | None, val: int) -> ListNode | None:
        #Реализован вариант задачи как на литкоде, где нужно удалить все ноды со значением Val
        #Чтобы обрабатывать голову и внутренние элементы одинаково, создаем dummy вершину и вставляем ее в начало списка
        # Теперь голову отдельно обрабатывать не надо
        # Если встречаем вершину для удаления, то меняем указатель прошлой вершины next на следующую за удаленным элементом ноду
        dummy = ListNode(next=head)

        prev = dummy
        cur = head

        while cur:
            if cur.val == val:
                prev.next = cur.next
                cur = cur.next
            else:

                cur = cur.next
                prev = prev.next
        return dummy.next
        
