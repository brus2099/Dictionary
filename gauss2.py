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
        print("Prosigue ==>")

        if matriz[iter1][iter1] == 1:
            print("Prosigue ==>")
        
        else:
            print("Evaluacion2 creacion de un pivote == 1")
            aux = matriz[iter1][iter1]
            for eval2 in range (0, row):
                matriz[iter1][eval2] = matriz[iter1][eval2] / aux

    else:
        print("Evaluacion1 elemento de la columna principal != 0")
        aux = []
        for eval1 in range (0, row):
            aux.append(matriz[iter1][eval1])
            matriz[iter1][eval1] = matriz[iter1+1][eval1]
            matriz[iter1+1][eval1] = aux[eval1]
        
    
    for i in range (0, row):
        print("| ", end="")    
        for j in range (0, row):
            print(matriz[i][j], " ", end="")
        print("|")

