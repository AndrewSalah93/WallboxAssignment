from Scripts.UnitTesting_Part1 import check_first_repeated_integer
import pytest


def test_fn_return_first_repeated_number():
    assert check_first_repeated_integer([3, 2, 3], [2, 3]) == 3


def test_fn_return_expected_result_when_nothing_repeated():
    assert check_first_repeated_integer([3, 2, 3], [4, 5]) == -1


def test_fn_if_first_vec_empty():
    assert check_first_repeated_integer([], [4, 5]) == "First vector is empty"


def test_fn_if_second_vec_empty():
    assert check_first_repeated_integer([2, 3], []) == "Second vector is empty"


def test_fn_return_if_all_integers_repeated():
    assert check_first_repeated_integer([1, 1, 1], [1, 1]) == 1