from importlib import import_module
import pytest

Node = import_module("Hometask_4.№1").TreeNode

def level_order(root):
    if root is None:
        return []
    result, queue = [], [root]
    while queue:
        node = queue.pop(0)
        if node is None:
            result.append(None)
            continue
        result.append(node.val)
        queue.extend([node.left, node.right])
    while result and result[-1] is None:
        result.pop()
    return result

@pytest.mark.parametrize(("values", "expected"), [
    ([], []), ([None], []), ([1], [1]), ([1, 2, 3], [1, 2, 3]),
    ([1, None, 2], [1, None, 2]), ([1, 2, None, 3], [1, 2, None, 3]),
    ([0], [0]), ([-1, -2, -3], [-1, -2, -3]),
    ([1, None, None], [1]), ([1, 2, 3, None, 4], [1, 2, 3, None, 4]),
])
def test_build_tree_from_level_order(values, expected):
    root = import_module("Hometask_4.№1").Solution().buildTree(values)
    assert level_order(root) == expected
