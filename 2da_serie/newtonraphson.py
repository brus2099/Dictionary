propuesta = [-1, -2]
x, y = propuesta

def matrizDerivadas(prop):
    return [[2*prop[0], 2*prop[1]], [prop[1], prop[0]]]


def matrizFunciones(prop):
    return [-(prop[0]**2)-(prop[1]**2)+3, -(prop[0]*prop[1])+1]

print("Ejemplo con propuesta inicial: ", propuesta)
print("Matriz de derivadas: ", matrizDerivadas(propuesta))
print("Sustitucion en ambas ecuaciones: ", matrizFunciones(propuesta))

def muestraMatriz(deriv, func):
    print("Matriz actual: ")
    for i in range (0, 2):
        print("| ", end="")    
        for j in range (0, 2):
            print(deriv[i][j], " ", end="")
        print("|", func[i], "|")

def gauss(deriv, func):
    for iter1 in range(0, 2):
        if deriv[iter1][iter1] != 0:
            muestraMatriz(deriv, func)
        else:
            print("Intercambio de renglones")
            auxCambio = []
            for eval1 in range (0, 2):
                auxCambio.append(deriv[iter1][eval1])
                deriv[iter1][eval1] = deriv[iter1+1][eval1]
                deriv[iter1+1][eval1] = auxCambio[eval1]
            axuSoluc = func[iter1]
            func[iter1] = func[iter1+1]
            func[iter1+1] = axuSoluc
            muestraMatriz(deriv, func)

        print()
        # Volver elemento de matrix principal == 1
        if deriv[iter1][iter1] == 1:
            muestraMatriz(deriv, func)
        else:
            print("Multiplicacion con un escalar.")
            auxPivote = deriv[iter1][iter1]
            for eval2 in range (0, 2):
                deriv[iter1][eval2] = deriv[iter1][eval2] / auxPivote
            func[iter1] = func[iter1]/auxPivote
            muestraMatriz(deriv, func)

        print("Ceros en columnas")
        auxFila = []
        for agreFila in range (0, 2):
            auxFila.append(deriv[iter1][agreFila])
        auxSolFila = func[iter1]
        for avance1 in range (0, 2):
            auxMulti = deriv[avance1][iter1]
            guardavalores = []
            for avance2 in range (0, 2):
                guardavalores.append(deriv[avance1][avance2] - auxMulti*auxFila[avance2])
                deriv[avance1][avance2] = guardavalores[avance2]
            func[avance1] = func[avance1] - auxMulti*auxSolFila
        deriv[iter1] = auxFila
        func[iter1] = auxSolFila
        muestraMatriz(deriv, func)
    return deriv, func

muestraMatriz(matrizDerivadas(propuesta), matrizFunciones(propuesta))
matIdentidad, matAumento = gauss(matrizDerivadas(propuesta), matrizFunciones(propuesta))
x, y = propuesta[0] + matAumento[0], propuesta[1] + matAumento[1]
print("Punto se encuentra en ( ", x, " , ", y, ")")