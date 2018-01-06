#--------------------- Fungsi ---------------------#
def Konversi(a):
    indeks = []
    for i in range(len(a)):
        if float(a[i]) >= 3.25 and float(a[i]) <= 4:
            indeks += ['A']
        elif float(a[i]) >= 2.25 and float(a[i]) < 3.25:
            indeks += ['B']
        elif float(a[i]) >= 1.75 and float(a[i]) < 2.25:
            indeks += ['C']
        elif float(a[i]) >= 0.75 and float(a[i]) < 1.75:
            indeks += ['D']
        elif float(a[i]) >= 0 and float(a[i]) < 0.75:
            indeks += ['E']
    return indeks

def CountX(a):
    arr = [0,0,0,0,0,0]

    arr[0] = len(a)
    for i in range(len(a)):
        if   a[i] == 'A': arr[1] += 1
        elif a[i] == 'B': arr[2] += 1
        elif a[i] == 'C': arr[3] += 1
        elif a[i] == 'D': arr[4] += 1
        elif a[i] == 'E': arr[5] += 1

    for i in range(len(arr)):
        if arr[i] == 0: arr[i] = "Data kosong"

    return arr

def IPKelas(a):
    ans = 0
    for i in range(len(a)): ans += float(a[i])
    return ans / len(a)

def CetakNilai(a):
    print("Banyak Nilai  :", a[0])
    print("Banyak Nilai A:", a[1])
    print("Banyak Nilai B:", a[2])
    print("Banyak Nilai C:", a[3])
    print("Banyak Nilai D:", a[4])
    print("Banyak Nilai E:", a[5])

def CetakLulus(a):
    arr = [0,0]
    arr[0] = a[1] + a[2] + a[3]
    arr[1] = a[4] + a[5]
    print("Banyak Nilai Yang Lulus      :", arr[0])
    print("Banyak Nilai Yang Tidak Lulus:", arr[1])


#--------------------- Main ---------------------#

num = 0
cond = True
saveFile = open('nilai.dat','w')
while num <= 100 and cond:
    n = float(input("Input nilai: "))
    if n >= 0 and n <= 4:
        saveFile.write(str(n) + '\n')
        num+=1
    else: cond = False
saveFile.close()
readFile = open('nilai.dat','r').read().split()

menu = int(input("Pilihan Menu: 1-3"))
if   menu == 1: CetakNilai(CountX(Konversi(readFile)))
elif menu == 2: CetakLulus(CountX(Konversi(readFile)))
elif menu == 3: print("IP Kelas:","%.1f"%IPKelas(readFile))
else: print("Pilihan menu salah")

