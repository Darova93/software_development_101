from solution import removeDuplicates
import pytest

@pytest.mark.parametrize("nums, expectedNums", [([1,1,2], 2), ([0,0,1,1,1,2,2,3,3,4], 5)])
def test_removeDuplicates(nums, expectedNums):
    result = removeDuplicates(nums)
    assert result == expectedNums


"""
def test_removeDuplicates():
    assert removeDuplicates([1,1,2]) == 2

def test2_removeDuplicates():
    assert removeDuplicates([0,0,1,1,1,2,2,3,3,4]) == 5
"""
