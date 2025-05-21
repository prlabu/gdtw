# SPDX-License-Identifier: Apache-2.0
# 
# Copyright (C) 2019-2024 Dave Deriso <dderiso@alumni.stanford.edu>, Twitter: @davederiso
# Copyright (C) 2019-2024 Stephen Boyd
# 
# GDTW is a Python/C++ library that performs dynamic time warping.
# GDTW improves upon other methods (such as the original DTW, ShapeDTW, and FastDTW) by introducing regularization, 
# which obviates the need for pre-processing, and cross-validation for choosing optimal regularization hyper-parameters. 
# 
# Paper: https://rdcu.be/cT5dD
# Source: https://github.com/dderiso/gdtw
# Docs: https://dderiso.github.io/gdtw

# -*- coding: utf-8 -*-
from setuptools import setup, Extension
import numpy as np
import os, sys

# Check to see if there's a prefered compiler on this machine
if "CC" in os.environ:
  print("*"*110)
  print(f"Detected env variable: CC={os.environ['CC']}")
  print(f"We'll attempt to compile this library with {os.environ['CC']}.")
  print("If compilation fails, remove this variable from your environment by typing 'unset CC', and try running setup again.")
  print("*"*110)

from setuptools.command.build_ext import build_ext

class BuildExt(build_ext):
  def build_extensions(self):
    cc = None
    if "CC" in os.environ:
      cc = os.environ["CC"]
    
    elif sys.platform == 'darwin':
      cc = "g++"
      self.compiler.compiler_so.append('-stdlib=libc++')
      self.compiler.compiler.append('-stdlib=libc++')
      # self.compiler.compiler_so.append('-target x86_64-apple-macos')
      # self.compiler.compiler.append('-target x86_64-apple-macos')
    
    elif sys.platform == "linux":
      cc = "g++"
      if '-Wstrict-prototypes' in self.compiler.compiler_so:
        self.compiler.compiler_so.remove('-Wstrict-prototypes') # gets rid of a useless warning
      self.compiler.compiler_so.append('-Wno-maybe-uninitialized')
  
    elif sys.platform == "win32":
      cc = "cl"
      if hasattr(self.compiler, 'compile_options'):
        self.compiler.compile_options.extend(['/EHsc', '/O2', '/W3', '/GL', '/DNDEBUG', '/MD'])
      elif hasattr(self.compiler, 'compiler'):
        self.compiler.compiler.extend(['/EHsc', '/O2', '/W3', '/GL', '/DNDEBUG', '/MD'])
      # Add extra compile arguments for Windows
      if hasattr(self.compiler, 'compile_options'):
        self.compiler.compile_options.extend(['/std:c++14', '/arch:AVX2', '/Ot'])
      elif hasattr(self.compiler, 'compiler'):
        self.compiler.compiler.extend(['/std:c++14', '/arch:AVX2', '/Ot'])
      
    if cc is not None:
      if hasattr(self.compiler, 'compiler_so'):
        self.compiler.compiler_so[0] = cc
      if hasattr(self.compiler, 'compiler'):
        self.compiler.compiler[0] = cc
      if hasattr(self.compiler, 'linker_so'):
        self.compiler.linker_so[0] = cc
    super(BuildExt, self).build_extensions()

cpp_module = Extension(
  'gdtwcpp', 
  sources=['gdtw/gdtw_solver.cpp'],
  include_dirs=[
    np.get_include(),
    "./gdtw",
  ],
  extra_compile_args=["-Ofast", "-Wall", "-std=c++11"],# "-flto"], # "-target", "x86_64-apple-macos"
  language="c++11"
)

setup_params = setup(
  cmdclass={'build_ext': BuildExt},
  ext_modules=[cpp_module],
  packages=['gdtw']
)

