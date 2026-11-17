from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.balance_factor = None


class Solution:
    def fillBalanceFactors(self, root: TreeNode | None) -> None:

        def height(node):
            if not node:
                return 0

            # Вычисляем высоты поддеревьев рекурсивно
            left_height = height(node.left)
            right_height = height(node.right)

            # Фактор баланса - разница высот левого и правого поддеревьев
            node.balance_factor = left_height - right_height

            # Высота узла - максимум высот поддеревьев + 1
            return max(left_height, right_height) + 1
        height(root)

        # Время: O(N), где N — число узлов
        # Память: O(h) на рекурсию, где h — высота дерева
