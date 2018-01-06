matrixRow = int(input("Masukkan Jumlah Baris Matrix: "))
matrixCol = int(input("Masukkan Jumlah Kolom Matrix: "))

matrix = []

for i in range(0,matrixRow):
    x = input("Masukkan Nilai Matrix Baris Ke " + str(i+1) + ", Sebanyak " + str(matrixCol) + " : ").split()
    matrix += [[]]
    for j in range(0,matrixCol):
        matrix[i] += [int(x[j])]

def cekGenap(a):
    genap = 0
    for i in range(0,matrixRow):
        for j in range(0,matrixCol):
            if a[i][j] % 2 == 0:
                genap += 1
    return genap

def cekGanjil(a):
    ganjil = 0
    for i in range(0,matrixRow):
        for j in range(0,matrixCol):
            if a[i][j] % 2 != 0:
                ganjil += 1
    return ganjil

def cekPositif(a):
    positif = 0
    for i in range(0, matrixRow):
        for j in range(0, matrixCol):
            if a[i][j] >= 0:
                positif += 1
    return positif

def cekNegatif(a):
    negatif = 0
    for i in range(0, matrixRow):
        for j in range(0, matrixCol):
            if a[i][j] < 0:
                negatif += 1
    return negatif

print("############# Matrix #############")
for i in range(0,matrixRow):
    for j in range(0, matrixCol):
        print(matrix[i][j], end="\t")
    print()

print()
print("Banyak Genap:", cekGenap(matrix))
print("Banyak Ganjil:", cekGanjil(matrix))
print("Banyak Positif:", cekPositif(matrix))
print("Banyak Negatif:", cekNegatif(matrix))
