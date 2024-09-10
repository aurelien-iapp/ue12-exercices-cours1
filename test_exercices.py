import numpy as np
from numpy.testing import assert_equal, assert_array_less, assert_allclose
import exercices


def test_create_zeros(self):
    actual = exercices.create_zeros()
    expected = [0, 0, 0, 0, 0]
    assert_equal(actual, expected)
