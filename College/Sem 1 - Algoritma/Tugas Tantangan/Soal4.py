matrixRow1 = int(input("Masukkan Jumlah Baris Matrix ke 1: "))
matrixCol1 = int(input("Masukkan Jumlah Kolom Matrix ke 1: "))
matrixRow2 = int(input("Masukkan Jumlah Baris Matrix ke 2: "))
matrixCol2 = int(input("Masukkan Jumlah Kolom Matrix ke 2: "))

matrix1 = []
matrix2 = []

for i in range(0,matrixRow1):
    x = input("Masukkan Nilai Matrix 1 Baris Ke " + str(i+1) + ", Sebanyak " + str(matrixCol1) + " : ").split()
    matrix1 += [[]]
    for j in range(0,matrixCol1):
        matrix1[i] += [int(x[j])]

for i in range(0,matrixRow2):
    y = input("Masukkan Nilai Matrix 2 Baris Ke " + str(i+1) + ", Sebanyak " + str(matrixCol2) + " : ").split()
    matrix2 += [[]]
    for j in range(0,matrixCol2):
        matrix2[i] += [int(y[j])]

def cekMatrix(a,b):
    ans = False
    if len(a) == len(b):
        ans = True
        for i in range(0,matrixRow1):
            if ans == False:
                break
            for j in range(0,matrixCol1):
                if matrix1[i][j] == matrix2[i][j]:
                    ans = True
                else:
                    ans = False
                    break
    if ans:
        return "Kedua Matrix Sama"
    else:
        return "Kedua Matrix Tidak Sama"

print("############# Matrix 1 #############")
for i in range(0,matrixRow1):
    for j in range(0, matrixCol1):
        print(matrix1[i][j], end="\t")
    print()
print()

print("############# Matrix 2 #############")
for i in range(0,matrixRow2):
    for j in range(0, matrixCol2):
        print(matrix2[i][j], end="\t")
    print()

print()
print(cekMatrix(matrix1,matrix2))
