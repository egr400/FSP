# import cython libraries for build and set up
from distutils.core import setup
from Cython.Build import cythonize 

# cythonizes and sets up cython file
setup(ext_modules = cythonize('program_broken_cy.pyx'))