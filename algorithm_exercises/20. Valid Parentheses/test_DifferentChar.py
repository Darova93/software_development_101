import pytest
from solution import isValid
@pytest.mark.parametrize("test_input,expected", [('()[&]{}', False),
                                                 ('()[]{}(', False),
                                                 ('()[]{}', True)])
def test_answer(test_input,expected):
    result = isValid(test_input)
    assert(result == expected)
