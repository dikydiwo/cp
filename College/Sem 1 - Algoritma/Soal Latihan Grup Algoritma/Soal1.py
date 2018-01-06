matrix = []
for i in range(8):
    x = str(input("Masukkan Karakter Pada Matrix Baris Ke " + str(i+1) + ", Sebanyak 8: ")).upper()
    matrix += [[]]
    for j in range(8):
        matrix[i] += [x[j]]

kata = str(input("Masukkan Kata Dicari(1-8 Kata): ")).upper()
if len(kata) >= 1 and len(kata) <= 8:
    awal  = [0,0]
    akhir = [0,0]
    num = 0
    hasil = ""
    for i in range(8):
        if hasil == kata:
            akhir[0] = awal[0]
            akhir[1] = awal[1] + (len(kata)-1)
            break
        hasil = ""
        num = 0
        for j in range(8):
            if hasil == kata:

                break
            elif matrix[i][j] == kata[num]:
                hasil += matrix[i][j]
                num += 1
                if awal[0] == 0 and awal[1] == 0:
                    awal[0] = i+1
                    awal[1] = j+1
            else:
                hasil = ""
                num = 0
                awal[0] = 0
                awal[1] = 0

    if hasil == kata:
        print("Awal  =",awal)
        print("Akhir =",akhir)
    else:
        print("Kata tidak ditemukan")
else:
    print("Kata Kelebihan")