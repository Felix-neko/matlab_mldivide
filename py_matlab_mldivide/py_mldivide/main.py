# -*- coding: utf-8 -*-

import os, sys

import ctypes

import numpy as np

# path_to_dll = "D:/Projects/matlab_mldivide/MatlabMLDivide/x64/Debug/TestMatlabMLDivide.dll"


path_to_dll = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                           "../build/lib.win-amd64-2.7/_matlab_mldivide.pyd"))

print path_to_dll

# try:
test_dll = ctypes.CDLL(path_to_dll)
# except Exception as ex:
#     print ex
# test_dll.main()

test_array = np.asarray(np.linspace(1 + 0.5j, 10 + 5j, 10), dtype=np.complex128)
# print test_array

data_ptr = test_array.ctypes.data_as(ctypes.POINTER(ctypes.c_double))


a_array = np.asarray([[8, 1, 6], [3, 5, 7], [4, 9, 2]], dtype=np.complex128)
b_array = np.asarray([[15], [15], [15]], dtype=np.complex128)
c_array = np.zeros(shape=(3, 1), dtype=np.complex128)

a_ptr = a_array.ctypes.data_as(ctypes.POINTER(ctypes.c_double))
b_ptr = b_array.ctypes.data_as(ctypes.POINTER(ctypes.c_double))
c_ptr = c_array.ctypes.data_as(ctypes.POINTER(ctypes.c_double))

print "BEFORE:"
print c_array

test_dll.mldivide(a_ptr, 3, 3, b_ptr, 3, 1, c_ptr, 3, 1)

print "AFTER:"
print c_array


# test_dll.test(data_ptr)

# print np.__version__