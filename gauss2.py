#
#   3x + 2y + z == 1        | 3 2  1 | 1 |
#  5x + 3y + 4z == 2  ==>   | 5 3  4 | 2 |
#     x + y - z == 1        | 1 1 -1 | 1 | 
# 

matriz = [[3, 2, 1], [5, 3, 4], [1, 1, -1]]
src = [1, 2, 1]

print()

row = len(matriz)

for i in range (0, row):
    print("| ", end="")    
    for j in range (0, row):
        print(matriz[i][j], " ", end="")
    print("|")

for i in range (0, row):
    print(" ", matriz[i][i], end="")

print()
print("#### #### #### #### #### #### #### #### #### #### #### #### ")
#### #### #### #### #### #### #### #### #### #### #### #### 

for iter1 in range (0, row):

    if matriz[iter1][iter1] != 0:
        print("Prosigue1 ==>")
    else:
        print("Evaluacion1 elemento de la columna principal != 0")
        auxCambio = []
        for eval1 in range (0, row):
            auxCambio.append(matriz[iter1][eval1])
            matriz[iter1][eval1] = matriz[iter1+1][eval1]
            matriz[iter1+1][eval1] = auxCambio[eval1]


    if matriz[iter1][iter1] == 1:
        print("Prosigue2 ==>")
    else:
        print("Evaluacion2 creacion de un pivote == 1")
        auxPivote = matriz[iter1][iter1]
        for eval2 in range (0, row):
            matriz[iter1][eval2] = matriz[iter1][eval2] / auxPivote
    
    auxFila = matriz[iter1]
    print(auxFila)
    for avance1 in range (0, row):
        auxMulti = matriz[avance1][iter1]
        print(auxMulti)
        for avance2 in range (0, row):
            matriz[avance1][avance2] = matriz[avance1][avance2] - auxMulti*auxFila[avance2]
    matriz[iter1] = auxFila
    print(auxFila)
    print(matriz[iter1])

    for i in range (0, row):
        print("| ", end="")
        for j in range (0, row):
            print(matriz[i][j], " ", end="")
        print("|")

