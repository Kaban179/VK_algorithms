from importlib import import_module
import pytest
T = import_module("Hometask_4.№2").TreeNode
@pytest.mark.parametrize(("root", "expected"), [
    (None, True), (T(1), True), (T(1,T(2),T(2)),True), (T(1,T(2),T(3)),False),
    (T(1,T(2,T(3)),T(2,None,T(3))),True), (T(1,T(2,T(3)),T(2,T(3))),False),
    (T(1,T(0),T(0)),True), (T(1,None,T(2)),False),
    (T(1,T(2,None,T(3)),T(2,T(3))),True),
    (T(1,T(2,T(3)),T(2,None,T(4))),False),
])
def test_is_symmetric(root, expected):
    assert import_module("Hometask_4.№2").Solution().isSymmetric(root) == expected
