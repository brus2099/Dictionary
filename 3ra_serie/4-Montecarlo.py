import numpy as np
import matplotlib.pyplot as plt
from math import e
from random import randrange


prec = int(input("Con cuantos puntos llenar la grafica?"))
x = np.arange(0, 6, 0.01)
y = e**x

plt.axis([1.9, 4.1, 0, 60])
plt.plot([2, 2], [0, 100], color = 'red')
plt.plot([4, 4], [0, 100], color = 'red')
plt.plot(x, y)
plt.plot(2, e**2, marker='.', color='black')
plt.plot(4, e**4, marker='.', color='black')

list = []
inPoint = 0
outPoint = 0

for i in range (0, prec):
    list.append([(randrange(0, 2000)/1000)+2, randrange(54598)/1000])
    # Descomenta el siguiente print para ver la lista de todos los puntos
    #print(list[i])

for i in range (0, prec):
    if list[i][1] <= e**list[i][0]:
        plt.plot(list[i][0], list[i][1], marker='.', color='blue')
        inPoint = inPoint + 1
    else:
        plt.plot(list[i][0], list[i][1], marker='.', color='aquamarine')
        outPoint = outPoint + 1

plt.show()
print("Puntos dentro:", inPoint)
print("Puntos fuera:", outPoint)
print("Puntos totales:", inPoint+outPoint)
print("Area total:", 2*(e**4), "u^2")
print("Area aproximada:", ( inPoint * ( 2*(e**4)) ) / prec, "u^2" )


