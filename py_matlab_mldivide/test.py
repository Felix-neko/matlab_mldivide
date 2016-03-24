# -*- coding: utf-8 -*-

import numpy as np
import numpy.testing

import unittest

from matlab_matrix_divide import matrix_divide


class TestMatrixDivision(unittest.TestCase):
    def test_mldivide(self):
        a_array = np.asarray([[8, 1, 6], [3, 5, 7], [4, 9, 2]], dtype=np.complex128)
        b_array = np.asarray([[15], [15], [15]], dtype=np.complex128)
        c_array = matrix_divide.mldivide(a_array, b_array)

        np.testing.assert_allclose(c_array, [[1], [1], [1]])

if __name__ == "__main__":
    unittest.main()