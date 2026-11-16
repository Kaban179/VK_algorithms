from importlib import import_module
import pytest

TreeNode = import_module("Hometask_5.№4").TreeNode

def bst(values):
    root = None
    for value in values:
        if root is None:
            root = TreeNode(value)
            continue
        node = root
        while True:
            side = "left" if value < node.val else "right"
            child = getattr(node, side)
            if child is None:
                setattr(node, side, TreeNode(value))
                break
            node = child
    return root

@pytest.mark.parametrize(("values", "k", "smallest", "largest"), [
    ([3,1,4,2], 1, 1, 4), ([5,3,6,2,4,1], 3, 3, 4),
    ([2,1,3], 2, 2, 2), ([7], 1, 7, 7),
    ([8,4,12,2,6,10,14], 4, 8, 8),
    ([10,5,15,3,7,12,18], 2, 5, 15),
    ([0,-5,5,-10,-2,2,10], 3, -2, 2),
    ([1,2,3,4,5], 5, 5, 1), ([5,4,3,2,1], 1, 1, 5),
    ([20,10,30,5,15,25,35,13], 6, 25, 13),
    ([-4,-2,0,2,4], 4, 2, -2), ([9,3,12,1,6,10,15,5,7], 5, 7, 7),
])
def test_kth_order_statistics_in_bst(values, k, smallest, largest):
    solution = import_module("Hometask_5.№4").Solution()
    root = bst(values)
    assert solution.kthSmallest(root, k) == smallest
    assert solution.kthLargest(root, k) == largest
