import pytest
from ...lib.fibonacci import fibonacci


@pytest.mark.parametrize('number, result', [
    (0, 1),
    (1, 1),
    (2, 1),
    (3, 2),
    (20, 6765),
])
def test_fibonacci(number, result):
    assert fibonacci(number) == result


def test_fibonacci_less_than():
    num = -1

    with pytest.raises(ValueError) as value_error:
        fibonacci(num)
        assert str(value_error) == f'{num} less than min of 0'


def test_fibonacci_greater_than():
    num = 21

    with pytest.raises(ValueError) as value_error:
        fibonacci(num)
        assert str(value_error) == f'{num} greater than max of 20'
