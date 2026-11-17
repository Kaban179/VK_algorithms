from typing import Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isCompleteTree(self, root: TreeNode | None) -> bool:
        queue = deque([root])
        seenNull = False

        while (len(queue) > 0):
            node = queue.popleft()
            if (not node):
                seenNull = True
            else:
                if seenNull:
                    return False
                queue.append(node.left)
                queue.append(node.right)

        return True

# Используем BFS (обход по уровням), чтобы проверять узлы слева направо.
# У полного бинарного дерева все уровни, кроме последнего, заполнены,
# а последний заполняется строго слева направо.
# Если встретили пустое место, после него не должно быть других узлов.
# Время: O(N), память: O(N).
         
