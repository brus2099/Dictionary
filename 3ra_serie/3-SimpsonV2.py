# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 16:53:59 2019

@author: Bruno Cruz Granados
"""

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

# Lista para numeradores. Contiene las expresiones algebraicas
num = []

# Lista para denominadores. Contiene valores enteros
den = []

# Lista para guardar iteraciones
lis = []

multi = 1
restaDen = 1

from sympy import *
x = symbols('x')

for i in range (0, lenP):
    #numerador
    for j in range (0, lenP):
        num.append(x-run[j][0])
    num.pop(i)
    for m in range (0, lenP-1):
        multi = multi * num[m]
    varN = expand(multi*run[i][1])
    #denominador
    for b in range (0, lenP):
        den.append(run[i][0]-run[b][0])
        print("den", den)
    den.pop(i)
    print("den.pop", den)
    for o in range (0, lenP-1):
        print("restaden ini", restaDen)
        restaDen = restaDen * den[o]
        print("restaden sal", restaDen)
    print(varN)
    print(restaDen)
    #division y guardado 
    if varN == 0:
        lis.append((0, 0))
    else:
        lis.append(div(varN, restaDen))
    print(lis)
    num = []
    den = []
    multi = 1
    restaDen = 1
    ##print(lis[i][0])

suma = 0
for u in range (0, lenP):
    suma = suma + lis[u][0]
print(suma)

fx = lambda x : suma

x = np.linspace(-20, 20, 100)

aa = fx(x)
plt.axis([-20, 20, -20, 20])
plt.plot(x, aa, color="red")

plt.show()




