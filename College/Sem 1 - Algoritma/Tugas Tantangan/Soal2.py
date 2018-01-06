matrixRow = int(input("Masukkan Jumlah Baris Matrix: "))
matrixCol = int(input("Masukkan Jumlah Kolom Matrix: "))

if matrixRow <= 10 and matrixCol <= 10:

    matrix = []

    for i in range(0,matrixRow):
        x = input("Masukkan baris ke " + str(i+1) + ", Sebanyak " + str(matrixCol) + " : ").split()
        matrix += [[]]
        for j in range(0,matrixCol):
            matrix[i] += [int(x[j])]

    def cekElemen(a,b):
        return a * b

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

    print("############# Matrix #############")
    for i in range(0,matrixRow):
        for j in range(0,matrixCol):
            print(matrix[i][j], end="\t")
        print()

    print()
    print("Banyak Elemen Matrix :", cekElemen(matrixRow, matrixCol))
    print("Banyak Elemen Matrix Yang Genap :", cekGenap(matrix))
    print("Banyak Elemen Matrix Yang Ganjil:", cekGanjil(matrix))

else:
    print("Jumlah Ukuran Matrix Tidak Boleh Lebih Dari 10x10")
