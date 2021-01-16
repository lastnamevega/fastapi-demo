from ...lib.fibonacci import fibonacci
import pytest


@pytest.mark.parametrize('input, output', [
    (0, 0),
    (1, 1),
    (2, 1),
    (3, 2),
    (99, 218922995834555169026),
])
def test_fibonacci(input, output):
    assert fibonacci(input) == output


def test_fibonacci_less_than():
    input = -1

    with pytest.raises(ValueError) as value_error:
        fibonacci(input)
        assert str(value_error) == f'{input} less than 0'
