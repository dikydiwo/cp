matrixRow = int(input("Masukkan Jumlah Baris Matrix: "))
matrixCol = int(input("Masukkan Jumlah Kolom Matrix: "))

matrix = []

for i in range(0, matrixRow):
    x = input("Masukkan Nilai Matrix Baris Ke " + str(i+1) + ", Sebanyak " + str(matrixCol) + " : ").split()
    matrix += [[]]
    for j in range(0, matrixCol):
        matrix[i] += [int(x[j])]

def cekMatrixSegitigaAtas(a):
    ans = False
    cnt = 0

    if matrixRow == matrixCol:
        for i in range(0,matrixRow):
            cnt = 0
            for j in range(0, matrixCol):
                if matrix[i][j] == 0:
                    cnt += 1
            if cnt == i:
                ans = True
            else:
                ans = False
                break

    if ans == True:
        return "Matrix Segitiga Atas"
    else:
        return "Bukan Matrix Segita Atas"

print("############# Matrix #############")
for i in range(0,matrixRow):
    for j in range(0, matrixCol):
        print(matrix[i][j], end="\t")
    print()

print()
print(cekMatrixSegitigaAtas(matrix))


