from importlib import import_module
import pytest

@pytest.mark.parametrize(("nums", "k", "smallest", "largest"), [
    ([3,2,1,5,6,4], 2, 2, 5),
    ([3,2,3,1,2,4,5,5,6], 4, 3, 4),
    ([1], 1, 1, 1),
    ([-1,-2,-3,-4], 1, -4, -1),
    ([2,2,2], 2, 2, 2),
    ([10,-1,0,7], 3, 7, 0),
    ([8,4,6,2], 4, 8, 2),
    ([8,4,6,2], 1, 2, 8),
    ([5,1,9,3,7], 3, 5, 5),
    ([0,-5,5,-10,10], 2, -5, 5),
    ([4,1,4,2,4], 2, 2, 4),
    ([100,-100,50,0], 3, 50, 0),
])
def test_kth_order_statistics_in_array(nums, k, smallest, largest):
    solution = import_module("Hometask_5.№3").Solution()
    assert solution.findKthSmallest(nums[:], k) == smallest
    assert solution.findKthLargest(nums[:], k) == largest
