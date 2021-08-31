# 208539270 yardenbakish
# 208983700 tamircohen1
"""setup.py - this is the file that will allow to import mykmeanssp - our kmeans
 implementation in C, along with all the other C files where different functions are implemented"""

"""all of the c files are connected throught the kmeans.h header file"""

from setuptools import setup, Extension

setup(
    name = 'mykmeanssp',
    ext_modules = [Extension('mykmeanssp', ['kmeans.c', 'isCentroidsChanged.c', 'updateCent.c', 'squaredEuclideanDist.c', 'freeArray.c', 'freeAll.c', 'initialize.c', 'iterations.c'])])
