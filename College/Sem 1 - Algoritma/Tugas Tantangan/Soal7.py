n = int(input())

saveFile = open('dataku.dat','w')
for i in range(n):
    x = int(input())
    saveFile.write(str(x) + " ")
saveFile.close()
print("Data berhasil di tulis ke file : dataku.dat")