from importlib import import_module
import pytest

TreeNode = import_module("Hometask_5.№5").TreeNode

def make_tree(items):
    if not items:
        return None
    nodes = {value: TreeNode(value) for value, _, _ in items}
    for value, left, right in items:
        nodes[value].left = nodes.get(left)
        nodes[value].right = nodes.get(right)
    return nodes[items[0][0]]

def factors(root):
    if root is None:
        return {}
    result, stack = {}, [root]
    while stack:
        node = stack.pop()
        result[node.val] = node.balance_factor
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    return result

@pytest.mark.parametrize(("items", "expected"), [
    ([], {}), ([(1,None,None)], {1:0}),
    ([(2,1,None),(1,None,None)], {2:1,1:0}),
    ([(2,None,3),(3,None,None)], {2:-1,3:0}),
    ([(2,1,3),(1,None,None),(3,None,None)], {2:0,1:0,3:0}),
    ([(4,2,6),(2,1,3),(6,5,7),(1,None,None),(3,None,None),(5,None,None),(7,None,None)], {4:0,2:0,6:0,1:0,3:0,5:0,7:0}),
    ([(5,3,None),(3,2,4),(2,1,None),(4,None,None),(1,None,None)], {5:3,3:1,2:1,4:0,1:0}),
    ([(5,None,7),(7,6,8),(6,None,None),(8,None,None)], {5:-2,7:0,6:0,8:0}),
    ([(10,5,15),(5,2,None),(15,None,20),(2,None,None),(20,None,None)], {10:0,5:1,15:-1,2:0,20:0}),
    ([(8,4,12),(4,2,6),(12,10,None),(2,None,None),(6,None,None),(10,None,None)], {8:0,4:0,12:1,2:0,6:0,10:0}),
    ([(0,-2,2),(-2,-3,-1),(2,1,3),(-3,None,None),(-1,None,None),(1,None,None),(3,None,None)], {0:0,-2:0,2:0,-3:0,-1:0,1:0,3:0}),
    ([(6,3,9),(3,1,4),(9,8,11),(1,None,None),(4,None,5),(8,None,None),(11,None,None),(5,None,None)], {6:1,3:-1,9:0,1:0,4:-1,8:0,11:0,5:0}),
])
def test_balance_factor_is_written_for_each_node(items, expected):
    root = make_tree(items)
    import_module("Hometask_5.№5").Solution().calculateBalanceFactors(root)
    assert factors(root) == expected
