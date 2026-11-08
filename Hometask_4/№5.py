from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        if (not p) and (not q):
            return True
        elif not (q and p):
            return False
        else: 
            return (p.val == q.val) and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

# Два дерева считаются одинаковыми, если:
# 1. Оба дерева пустые - они одинаковы.
# 2. Если только одно дерево пустое — они различаются.
# 3. Значения соответствующих узлов должны совпадать.
# 4. Левые и правые поддеревья также должны быть одинаковыми.
#
# Проверка выполняется рекурсивно.
