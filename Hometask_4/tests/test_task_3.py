from importlib import import_module
import pytest
T = import_module("Hometask_4.№3").TreeNode
@pytest.mark.parametrize(("root", "expected"), [
    (None,0),(T(1),1),(T(1,T(2)),2),(T(1,None,T(2)),2),(T(1,T(2),T(3)),2),
    (T(1,T(2,T(4)),T(3)),2),(T(1,T(2,T(4)),None),3),
    (T(1,None,T(2,None,T(3))),3),(T(1,T(2,None,T(4)),T(3)),2),
    (T(1,T(2,T(4)),T(3,None,T(5))),2),
])
def test_min_depth(root, expected):
    assert import_module("Hometask_4.№3").Solution().minDepth(root) == expected
