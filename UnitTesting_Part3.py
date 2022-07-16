import pytest


def min_permutations_of_sequence(seq):
    """
    This function finds the minimum number of permutations to make a sequence interspersed.

        Parameter(s):
            seq: array of binary values

        Return(s):
            min_permutation (int): represents the minimum number of swaps done to make binary sequence interspersed
            "The sequence is empty": in case the given sequence is empty
            "The sequence is not complete": in case the sequence contains only one binary value
            "The sequence can not be interspersed": in case the sequence is impossible to be interspersed
    """
    length_of_seq = len(seq)
    min_permutations = 0
    if length_of_seq == 0:
        return "The sequence is empty"
    elif length_of_seq == 1:
        return "The sequence is not complete"
    count_of_0 = 0
    count_of_1 = 0
    count_of_0_even_pos, count_of_1_even_pos, count_of_0_odd_pos, count_of_1_odd_pos = count_even_odd_0s_1s(seq)
    for x in seq:
        if x == 0:
            count_of_0 = count_of_0 + 1
        else:
            count_of_1 = count_of_1 + 1
    if (count_of_0 > count_of_1 + 1) or (count_of_1 > count_of_0 + 1):
        return "The sequence can not be interspersed"
    elif count_of_0 == count_of_1:
        min_permutations = min(min(count_of_0_even_pos, count_of_1_odd_pos), min(count_of_1_even_pos, count_of_0_odd_pos))
    elif count_of_0 == count_of_1 + 1:
        min_permutations = count_of_0_odd_pos
    elif count_of_1 == count_of_0 + 1:
        min_permutations = count_of_1_odd_pos
    return min_permutations


def count_even_odd_0s_1s(seq):
    """
    This is a helping function that counts the number of 1s and 0s in even and odd positions of the sequence
        
        Parameter(s):
              seq: array of binary values
            
        Return(s):
              count_of_0_even_pos (int): represents the number of 0s in even positions in the sequence
              count_of_0_odd_pos (int): represents the number of 0s in odd positions in the sequence
              count_of_1_even_pos (int): represents the number of 1s in even positions in the sequence
              count_of_1_odd_pos (int): represents the number of 1s in odd positions in the sequence
    """
    length_of_seq = len(seq)
    count_of_0_even_pos = 0
    count_of_0_odd_pos = 0
    count_of_1_even_pos = 0
    count_of_1_odd_pos = 0
    for y in range(length_of_seq):
        if y % 2 == 0:
            if seq[y] == 0:
                count_of_0_even_pos += 1
            else:
                count_of_1_even_pos += 1
        else:
            if seq[y] == 0:
                count_of_0_odd_pos += 1
            else:
                count_of_1_odd_pos += 1
    return count_of_0_even_pos, count_of_1_even_pos, count_of_0_odd_pos, count_of_1_odd_pos


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
