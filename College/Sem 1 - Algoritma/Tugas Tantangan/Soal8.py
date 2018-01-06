read = open('dataku.dat', 'r').read()
banyakInt = len(read) / 2

def rata(a):
    ans = 0
    for i in range(len(a)):
        if a[i] != ' ':
            ans += int(a[i])
    return ans / banyakInt

print("Data :", read)
print("Banyak Nilai Integer :", "%.f"%banyakInt)
print("Rata-Rata :", rata(read))
