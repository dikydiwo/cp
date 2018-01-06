n = int(input())
saveFile = open('DataPoint.dat', 'w')
for i in range(n):
    x = input().split()
    saveFile.write(x[0] + " ")
    saveFile.write(x[1] + "\n")
saveFile.close()
print("Data berhasil di tulis ke file : DataPoint.dat")