matrixRow = int(input("Masukkan Jumlah Baris Matrix: "))
matrixCol = int(input("Masukkan Jumlah Kolom Matrix: "))

matrix= []

for i in range(0, matrixRow):
    x = input("Masukkan Nilai Matrix Baris Ke " + str(i+1) + ", Sebanyak " + str(matrixCol) + " : ").split()
    matrix += [[]]
    for j in range(0, matrixCol):
        matrix[i] += [int(x[j])]

def cekSatuan(a):
    ans = True
    for i in range(0, matrixRow):
        if ans == False:
            break
        for j in range(0, matrixCol):
            if matrix[i][j] == 0 or matrix[i][j] == 1:
                ans = True
            else:
                ans = False
                break
    if ans:
        return "Matrix Satuan"
    else:
        return "Bukan Matrix Satuan"

print("############# Matrix #############")
for i in range(0,matrixRow):
    for j in range(0, matrixCol):
        print(matrix[i][j], end="\t")
    print()

print()
print(cekSatuan(matrix))
