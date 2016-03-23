# -*- coding: utf-8 -*-
from distutils.core import setup, Extension

import os, sys

matlab_source_dir = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                          "../codegen/lib/matlab_mldivide"))

my_source_dir = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                          "../MatlabMLDivide/TestMatlabMLDivide"))

matlab_sources = filter(lambda x: x.endswith(".cpp") or x.endswith(".c"), os.listdir(matlab_source_dir))
matlab_sources = [os.path.join(matlab_source_dir, source) for source in matlab_sources]

my_sources = filter(lambda x: x.endswith(".cpp") or x.endswith(".c"), os.listdir(my_source_dir))
my_sources = [os.path.join(my_source_dir, source) for source in my_sources]

print matlab_sources


header_files = []

setup(name='PyMatlabDivide',
      version='0.0',
      package_dir={'': 'py_mldivide'},
      # py_modules=['foo'],
      ext_modules = [Extension("_matlab_mldivide", matlab_sources + my_sources,
                               include_dirs=[matlab_source_dir, my_source_dir])],
      )

