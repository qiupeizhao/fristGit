from test import*
from convexhull import*
from matplotlib import*

import timeit


def test_1():
    listPts = readDataPts('Set_A.dat', 500)  #File name, numPts given as example only
    giftwrap(listPts)         



print(timeit.timeit(test_1,number = 100))