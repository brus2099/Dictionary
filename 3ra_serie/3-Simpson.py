# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 21:18:15 2019

@author: Bruno Cruz Granados
"""

import numpy as np
from numpy.polynomial import Polynomial as P
import matplotlib.pyplot as plt

p = P([6, 5 ,1])
print(p.roots())


from sympy import *

#init_printing(use_latex='mathjax')

x, y = symbols('x y')

a = div( x**2 - x, 2 )
b = div( x**2 + x, 2 )
print(a[0], a[1])
print(expand((x**2 - x)/2 + (x**2 + x)/2))

val3=[1, 1]

val = []

val.append(x-val3[0])

print(type(val[0]))


x = np.arange(-10.0, 10.0, 0.01)
y = x**4/24 + 13*x**3/60 - 5*x**2/24 - 29*x/20 - 2
plt.axis([-100, 100, -100, 100])
plt.plot(x, y)
plt.show()


#plt.plot(x, y)
#plt.show()