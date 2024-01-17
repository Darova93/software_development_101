from .solution import removeDuplicates
import pytest

@pytest.mark.parametrize("nums, expectedNums", [([1,1,2], 2), ([0,0,1,1,1,2,2,3,3,4], 5)])
def test_removeDuplicates(nums, expectedNums):
    result = removeDuplicates(nums)
    assert result == expectedNums
