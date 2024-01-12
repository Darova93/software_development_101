from solution import removeDuplicates

def test_removeDuplicates():
    assert removeDuplicates([1,1,2]) == 2

def test2_removeDuplicates():
    assert removeDuplicates([0,0,1,1,1,2,2,3,3,4]) == 5
