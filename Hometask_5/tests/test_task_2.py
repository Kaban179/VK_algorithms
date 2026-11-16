from importlib import import_module
import pytest

@pytest.mark.parametrize(("arrays", "expected"), [
    ([], []), ([[]], []), ([[],[],[]], []), ([[1]], [1]),
    ([[1,4,7]], [1,4,7]), ([[1,3],[2,4]], [1,2,3,4]),
    ([[1,4,5],[1,3,4],[2,6]], [1,1,2,3,4,4,5,6]),
    ([[-5,-1],[ -3,0]], [-5,-3,-1,0]),
    ([[1,1,1],[1,1]], [1,1,1,1,1]),
    ([[0,2,4],[1,3,5]], [0,1,2,3,4,5]),
    ([[1],[],[2],[],[3]], [1,2,3]),
    ([[-10,0,10],[-9,1,11],[-8,2,12]], [-10,-9,-8,0,1,2,10,11,12]),
])
def test_merge_k_sorted_arrays(arrays, expected):
    assert import_module("Hometask_5.№2").Solution().mergeKArrays(arrays) == expected
