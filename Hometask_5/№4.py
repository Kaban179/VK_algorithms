from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
        stack = []
        node = root
        count = 0
        stack.append(root)
        
        while node.left:
            node = node.left
            stack.append(node)

        while count < k:
            new = stack.pop()
            count += 1
            if new.right:
                stack.append(new.right)
                node = new.right
                while node.left:
                    node = node.left
                    stack.append(node)
        return new.val

    def kthLargest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        node = root
        count = 0
        stack.append(root)
    
        while node.right:
            node = node.right
            stack.append(node)
    
        while count < k:
            new = stack.pop()
            count += 1
    
            if new.left:
                stack.append(new.left)
                node = new.left
    
                while node.right:
                    node = node.right
                    stack.append(node)
    
        return new.val
