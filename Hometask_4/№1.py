from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, values: List[Optional[int]]) -> Optional[TreeNode]:

        def build(i):
            # Если индекс вышел за массив или узел отсутствует
            if i >= len(values) or values[i] is None:
                return None

            # Создаём текущий узел
            root = TreeNode(values[i])

            # Рекурсивно строим левое и правое поддеревья
            root.left = build(2 * i + 1)
            root.right = build(2 * i + 2)

            return root

        return build(0)

# Строим дерево рекурсивно. Если i элемент, это узел, то его левый узел лежит в 2*i + 1, а правый в 2*i + 2
# Корень находится в i = 0, каждый узел хранится в объекте TreeNode 
