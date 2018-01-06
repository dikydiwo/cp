a = input().split()
b = input().split()

matrixA = []
matrixB = []
matrix  = []

for i in range(int(a[0])):
	matrixA += [[]]
	x = input().split()
	for j in range(int(a[1])):
		matrixA[i] += [int(x[j])*3]
for i in range(int(b[0])):
	matrixB += [[]]
	x = input().split()
	for j in range(int(b[1])):
		matrixB += [int(x[j])*2]
for i in range(int(a[1])):
	row = []
	for j in range(int(a[0])):
		total = 0
		for k in range(int(a[1])):
			total = total + (matrixA[i][k] * matrixB[k][j])
		row += [total]
	matrix += [row]
for i in range(len(matrix)):
	for j in range(len(matrix[0])):
		print(matrix[i][j], end=" ")
	print()