#
#   3x + 2y + z == 1        | 3 2  1 | 1 |
#  5x + 3y + 4z == 2  ==>   | 5 3  4 | 2 |
#     x + y - z == 1        | 1 1 -1 | 1 | 
# 

matriz = [[3, 2, 1], [5, 3, 4], [1, 1, -1]]
src = [1, 2, 1]

print()

row = len(matriz)

print("Matriz aumentada inicial: ")
for i in range (0, row):
    print("| ", end="")    
    for j in range (0, row):
        print(matriz[i][j], " ", end="")
    print("|", src[i], "|")

if row == 2:
    det = matriz[0][0]*matriz[1][1] - matriz[1][0]*matriz[0][1]
    if det == 0:
        print("Matriz no tiene solucion")
    else:
        print()
        print("Comienza la busqueda de soluciones mediante el metodo de Gauss-Jordan ")
elif row == 3:
    det = ((matriz[0][0]*matriz[1][1]*matriz[2][2]) + (matriz[1][0]*matriz[2][1]*matriz[0][2]) + (matriz[2][0]*matriz[0][1]*matriz[1][2])) - ((matriz[2][0]*matriz[1][1]*matriz[0][2]) + (matriz[2][1]*matriz[1][2]*matriz[0][0]) + (matriz[2][2]*matriz[1][0]*matriz[0][1]))
    if det == 0:
        print("Matriz no tiene solucion")
    else:
        print()
        print("Comienza la busqueda de soluciones mediante el metodo de Gauss-Jordan ")

def printMatriz():
    print("Matriz actual: ")
    for i in range (0, row):
        print("| ", end="")    
        for j in range (0, row):
            print(matriz[i][j], " ", end="")
        print("|", src[i], "|")

for iter1 in range (0, row):

    print()
    # Comprobar 0 en el elemento de la matriz principal
    if matriz[iter1][iter1] != 0:
        print("El elemento ", iter1, " de la diagonal principal es diferente de 0. No se realiza intercambio de renglones. Puede continuar.")
    else:
        print("Elemento de la columna principal != 0 mediante intercambio de renglones")
        auxCambio = []
        for eval1 in range (0, row):
            auxCambio.append(matriz[iter1][eval1])
            matriz[iter1][eval1] = matriz[iter1+1][eval1]
            matriz[iter1+1][eval1] = auxCambio[eval1]
        axuSoluc = src[iter1]
        src[iter1] = src[iter1+1]
        src[iter1+1] = axuSoluc
    printMatriz()

    print()
    # Volver elemento de matrix principal == 1
    if matriz[iter1][iter1] == 1:
        print("El elemento ", iter1, " de la diagonal principal ya es 1. No se realiza multiplicacion por un escalar. Puede continuar.")
    else:
        print("Creacion de un pivote == 1 mediante multiplicacion con un escalar.")
        auxPivote = matriz[iter1][iter1]
        for eval2 in range (0, row):
            matriz[iter1][eval2] = matriz[iter1][eval2] / auxPivote
        src[iter1] = src[iter1]/auxPivote
    printMatriz()

    print()
    #Operaciones por filas para crear columnas == 0
    print("Creacion de ceros en la columna ", iter1)
    # Guardar la fila actual en un auxiliar para usarlo en las operaciones por columnas, no la fila.
    auxFila = []
    for agreFila in range (0, row):
        auxFila.append(matriz[iter1][agreFila])
    auxSolFila = src[iter1]
    for avance1 in range (0, row):
        auxMulti = matriz[avance1][iter1]
        # Crear lista que guarde los resultados de las operaciones de acuerdo a la fila
        guardavalores = []
        for avance2 in range (0, row):
            guardavalores.append(matriz[avance1][avance2] - auxMulti*auxFila[avance2])
            # Y devolverle los valores obtenidos a la matriz original
            matriz[avance1][avance2] = guardavalores[avance2]
        src[avance1] = src[avance1] - auxMulti*auxSolFila
    # Devolucion de la fila actual tras ser alterada por las operaciones por columnas
    matriz[iter1] = auxFila
    src[iter1] = auxSolFila
    printMatriz()

print()
print("Las soluciones \"aproximadas\" del sistema de ecuaciones son: ", src)
print("Considere esta aproximacion debido al trato con numeros flotantes que Python realiza.")