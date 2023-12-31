from main import division
import pytest


@pytest.mark.parametrize(
    "a, b, expected_result",
    [(10, 2, 5), (20, 10, 2), (30, -3, -10), (5, 2, 2.5)]
)
def test_division_good(a, b, expected_result):
    assert division(a, b) == expected_result


@pytest.mark.parametrize(
    "a, b, error_type",
    [(2, 0, ZeroDivisionError), (2, '2', TypeError)]
)
def test_division_with_error(a, b, error_type):
    with pytest.raises(error_type):
        division(a, b)
