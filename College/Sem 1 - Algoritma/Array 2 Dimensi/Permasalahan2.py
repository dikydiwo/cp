x    = int(input())
y    = int(input())

matrix1 = []
matrix2 = []

for i in range(x):
    data = input().split()
    matrix1 += [[]]
    for j in range(x):
        matrix1[i] += [int(data[j])]
for i in range(x):
    data = input().split()
    matrix2 += [[]]
    for j in range(x):
        matrix2[i] += [int(data[j])]

matrix = []
for i in range(x):
    matrix += [[]]
    for j in range(x):
        matrix[i] += [int(matrix1[i][j]) + int(matrix2[i][j])]
        print(matrix[i][j], end=" ")
    print()