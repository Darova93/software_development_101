from solution import removeDuplicates

def loopComp(nums, expectedNums):
    for i in range(len(expectedNums)):
        if nums[i] != expectedNums[i]:
            return False
    return True


def test_removeDuplicates():
    assert removeDuplicates([1,2,3]) == 2
    assert loopComp([1,2,3], [1,2])

def test2_removeDuplicates():
    assert loopComp([0,0,1,1,1,2,2,3,3,4], [0,1,2,3,4])
    assert removeDuplicates([0,0,1,1,1,2,2,3,3,4]) == 5
