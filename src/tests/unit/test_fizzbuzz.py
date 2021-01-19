from ...lib.fizzbuzz import fizzbuzz
import pytest


def divisible_by(number: int):
    return range(number, 101, number)


@pytest.mark.parametrize('number', [
    i for i in divisible_by(1) if i not in divisible_by(3) and i not in divisible_by(5)
])
def test_fizzbuzz_indivisible(number):
    assert fizzbuzz(number) == number


@pytest.mark.parametrize('number', [
    i for i in divisible_by(3) if i not in divisible_by(15)
])
def test_fizzbuzz_fizz(number):
    assert fizzbuzz(number) == 'fizz'


@pytest.mark.parametrize('number', [
    i for i in divisible_by(5) if i not in divisible_by(15)
])
def test_fizzbuzz_buzz(number):
    assert fizzbuzz(number) == 'buzz'


@pytest.mark.parametrize('number', divisible_by(15))
def test_fizzbuzz_fizzbuzz(number):
    assert fizzbuzz(number) == 'fizzbuzz'


def test_fizzbuzz_less_than():
    input = 0

    with pytest.raises(ValueError) as value_error:
        fizzbuzz(input)
        assert str(value_error) == f'{input} must be a natural number'
