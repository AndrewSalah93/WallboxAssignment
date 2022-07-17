from .context import wallbox
from wallbox.part3 import min_permutations_of_sequence
import pytest

# The following functions are used to test the implementation of min_permutations_of_sequence()


def test_fn_returns_0_if_seq_perfectly_interspersed():
    assert min_permutations_of_sequence([0, 1, 0, 1]) == 0


def test_fn_returns_min_permutations_for_even_seq():
    assert min_permutations_of_sequence([0, 1, 1, 0]) == 1


def test_fn_returns_seq_can_not_be_interspersed():
    assert min_permutations_of_sequence([0, 1, 1, 0, 1, 1]) == "The sequence can not be interspersed"


def test_fn_returns_alert_sequence_empty():
    assert min_permutations_of_sequence([]) == "The sequence is empty"


def test_fn_returns_min_permutations_for_odd_seq():
    assert min_permutations_of_sequence([0, 1, 1, 0, 1]) == 1


def test_fn_return_seq_not_complete_if_seq_of_single_element():
    assert min_permutations_of_sequence([0]) == "The sequence is not complete"