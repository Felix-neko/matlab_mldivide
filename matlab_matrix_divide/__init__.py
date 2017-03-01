# -*- coding: utf-8 -*-

import os
from os.path import abspath, dirname, join
import ctypes

ext = '.so' if os.name == 'posix' else '.pyd'
library_path = join(dirname(abspath(__file__)), "_matlab_matrix_divide" + ext)

if not os.path.exists(library_path):
    library_path = join(abspath(os.path.join(dirname(os.path.abspath(__file__)),
                        "../build/lib.win-amd64-2.7/matlab_matrix_divide/_matlab_matrix_divide.pyd")))

library = ctypes.CDLL(library_path)