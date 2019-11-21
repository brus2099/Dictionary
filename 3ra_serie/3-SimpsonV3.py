
from sympy.abc import x
from sympy.utilities.lambdify import lambdify, implemented_function
from sympy import Function
import numpy as np
import matplotlib.pyplot as plt

numPoint = int(input("How many point?: "))
point = []

for i in range (0, numPoint):
    print("point", i, "in x:")
    v1 = int(input())
    print("point", i, "in y:")
    v2 = int(input())
    point.append([v1, v2])
    
print("lenPoints:", len(point))
print("Points: ", point)

run = point
lenP = len(run)
num = []
den = []
lis = []
multi = 1
restaDen = 1

from sympy import *
x = symbols('x')

for i in range (0, lenP):
    for j in range (0, lenP):
        num.append(x-run[j][0])
    num.pop(i)
    for m in range (0, lenP-1):
        multi = multi * num[m]
    varN = expand(multi*run[i][1])
    for b in range (0, lenP):
        den.append(run[i][0]-run[b][0])
        print("den", den)
    den.pop(i)
    for o in range (0, lenP-1):
        restaDen = restaDen * den[o]
    if varN == 0:
        lis.append((0, 0))
    else:
        lis.append(div(varN, restaDen))
    num = []
    den = []
    multi = 1
    restaDen = 1

suma = 0
for u in range (0, lenP):
    suma = suma + lis[u][0]
print(suma)

f = lambdify(x, suma, 'numpy')
x = np.linspace(-10, 10, 100)
aa = f(x)
plt.figure(figsize=(7, 7))
plt.axis([-10, 10, -10, 10])
plt.plot(x, aa, color="red")
for p in range (0, lenP):
    plt.plot(run[p][0], run[p][1], marker='.', color='blue')
plt.show()













