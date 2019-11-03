
A = [[3, 2, 1], [5, 3, 4], [1, 1, -1]]

n = len(A)


print("Matriz actual: ")
for i in range (0, n):
    print("| ", end="")
    for j in range (0, n):
        print(A[i][j], " ", end="")
    print("|")