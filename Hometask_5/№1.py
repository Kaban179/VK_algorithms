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
         
