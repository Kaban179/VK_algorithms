from importlib import import_module
import pytest

TreeNode = import_module("Hometask_5.№6").TreeNode

def tree(values):
    if not values or values[0] is None:
        return None
    root = TreeNode(values[0])
    queue, i = [root], 1
    while queue and i < len(values):
        node = queue.pop(0)
        for side in ("left", "right"):
            if i < len(values) and values[i] is not None:
                child = TreeNode(values[i])
                setattr(node, side, child)
                queue.append(child)
            i += 1
    return root

def level_order(root):
    if root is None:
        return []
    result, queue = [], [root]
    while queue:
        node = queue.pop(0)
        if node is None:
            result.append(None)
        else:
            result.append(node.val)
            queue.extend([node.left, node.right])
    while result and result[-1] is None:
        result.pop()
    return result

@pytest.mark.parametrize(("values", "expected"), [
    ([], []), ([1], [1]), ([1,2,3], [1,3,2]),
    ([4,2,7,1,3,6,9], [4,7,2,9,6,3,1]),
    ([1,None,2], [1,2]), ([1,2,None], [1,None,2]),
    ([0,-1,1,-2,None,None,2], [0,1,-1,2,None,None,-2]),
    ([5,3,8,None,4,7,9], [5,8,3,9,7,4]),
    ([-1,-2,-3], [-1,-3,-2]), ([1,2,3,4,5,6], [1,3,2,None,6,5,4]),
    ([10,None,20,None,30], [10,20,None,30]), ([2,1,3,None,None,4], [2,3,1,None,4]),
])
def test_invert_tree(values, expected):
    root = tree(values)
    result = import_module("Hometask_5.№6").Solution().invertTree(root)
    assert level_order(result) == expected
