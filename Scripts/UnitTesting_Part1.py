import pytest


def check_first_repeated_integer(vec1, vec2):
    """
    This function gets the first number from vector of integers repeated in a second vector

            Parameter(s):
                vec1: first array of integers
                vec2: second array of integers

            Return(s):
                found (int): value of repeated integer
                "First vector is empty": in case first vector is empty
                "Second vector is empty": in case second vector empty
                -1: in case nothing is repeated from first vector in second one
    """
    vec1_len = len(vec1)
    if vec1_len == 0:
        return "First vector is empty"
    vec2_len = len(vec2)
    if vec2_len == 0:
        return "Second vector is empty"
    found = -1
    for x in range(vec1_len):
        for y in range(vec2_len):
            if vec1[x] == vec2[y]:
                found = vec1[x]
                break
        if found != -1:
            break
    return found

