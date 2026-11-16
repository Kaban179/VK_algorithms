from importlib import import_module
import pytest

TreeNode = import_module("Hometask_5.№1").TreeNode

def tree(values):
    if not values or values[0] is None:
        return None
    root = TreeNode(values[0])
    queue = [root]
    i = 1
    while queue and i < len(values):
        node = queue.pop(0)
        for side in ("left", "right"):
            if i < len(values) and values[i] is not None:
                child = TreeNode(values[i])
                setattr(node, side, child)
                queue.append(child)
            i += 1
    return root

@pytest.mark.parametrize(("values", "expected"), [
    ([], True), ([1], True), ([1,2,3], True), ([1,2,3,4], True),
    ([1,2,3,4,5,6], True), ([1,2,3,4,5,None,None], True),
    ([1,2,3,4,None,6], False), ([1,2,3,None,5], False),
    ([1,None,3], False), ([1,2,None,4], False),
    ([1,2,3,4,5,6,7], True), ([1,2,3,4,5,6,None], True),
])
def test_is_complete_tree(values, expected):
    assert import_module("Hometask_5.№1").Solution().isCompleteTree(tree(values)) == expected
