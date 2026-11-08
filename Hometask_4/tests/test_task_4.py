from importlib import import_module
import pytest
@pytest.mark.parametrize(("values", "expected"), [
    ([2,1,3],3),([5,3,8,2,4,7,9],18),([0,-2,4],-8),([-5,-8,-1],8),
    ([7],49),([],0),([None],0),([4,2,6,1,3,5,7],7),
    ([10,5,15,None,None,12,20],200),([-2,-5,3],-15),
])
def test_minimum_times_maximum_bst_value(values, expected):
    assert import_module("Hometask_4.№4").Solution().minMaxProduct(values) == expected
