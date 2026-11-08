from importlib import import_module
import pytest
T = import_module("Hometask_4.№5").TreeNode
@pytest.mark.parametrize(("p", "q", "expected"), [
    (None,None,True),(T(1),None,False),(None,T(1),False),(T(1),T(1),True),
    (T(1),T(2),False),(T(1,T(2)),T(1,T(2)),True),(T(1,T(2)),T(1,None,T(2)),False),
    (T(1,T(2),T(3)),T(1,T(3),T(2)),False),(T(1,T(2,T(4))),T(1,T(2,T(4))),True),
    (T(1,T(2),T(3)),T(1,T(2),None),False),
])
def test_is_same_tree(p, q, expected):
    assert import_module("Hometask_4.№5").Solution().isSameTree(p, q) == expected
