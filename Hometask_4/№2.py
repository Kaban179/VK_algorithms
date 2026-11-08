from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isMirror(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        if (not p) and (not q):
            return True
        elif not (q and p):
            return False
        else: 
            return (p.val == q.val) and self.isMirror(p.right, q.left) and self.isMirror(p.left, q.right)


    def isSymmetric(self, root: TreeNode | None) -> bool:
        if not root:
            return True
        return self.isMirror(root.left, root.right)
 # Рекурсивно проверяем зеркальность левого и правого поддеревьев.
# Сравниваем значения узлов и пары p.left с q.right, p.right с q.left.
# Если оба узла отсутствуют — возвращаем True,
# если только один — False
