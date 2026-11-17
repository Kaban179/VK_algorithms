from pathlib import Path
from runpy import run_path

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def linked_list(values):
    dummy = tail = ListNode()
    for value in values:
        tail.next = ListNode(value)
        tail = tail.next
    return dummy.next

def to_values(node):
    values = []
    seen = set()
    while node is not None:
        assert id(node) not in seen, "cycle in merged list"
        seen.add(id(node))
        values.append(node.val)
        node = node.next
    return values

Solution = run_path(str(Path(__file__).resolve().parents[1] / "№2.py"), init_globals={"ListNode": ListNode})["Solution"]
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
    result = Solution().mergeKLists([linked_list(values) for values in arrays])
    assert to_values(result) == expected
