from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDepth(self, root: TreeNode | None) -> int:
        if not root:
            return 0

        queue = [root]
        depth = 1

        while len(queue) > 0:
            queueLen = len(queue)

            for i in range(queueLen):
                node = queue[i]

                # Обрабатываем узел
                if node:
                    if not (node.left or node.right):
                        return depth
                    queue.append(node.left)
                    queue.append(node.right)
            
            depth += 1
            queue = queue[queueLen:]
# Используем BFS для обхода дерева по уровням.
# На каждом уровне добавляем детей
# Если нашли лист, возвращаем текущую глубину.
# BFS гарантирует минимальную глубину, поскольку
# уровни обрабатываются последовательно от корня.
