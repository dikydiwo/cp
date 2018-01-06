k = int(input())
read = open('DataPoint.dat', 'r').read()
arr = []
arr2 = []
kuadran = []
for i in range(len(read)):
    if read[i] != ' ' and read[i] != '\n':
        if read[i] == '-':
            continue
        else:
            if read[i-1] == '-':
                arr += ['-'+read[i]]
            else:
                arr += [read[i]]

num = 0
cond = True
while num < len(arr) and cond == True:
    if int(arr[num]) > 4 or int(arr[num+1]) < -4:
        kuadran += [0]
        arr2 += ["(" + str(arr[num]) + ", " + str(arr[num+1]) + ")"]
        num+=2
    elif int(arr[num]) < -4 or int(arr[num+1]) > 4:
        kuadran += [0]
        arr2 += ["(" + str(arr[num]) + ", " + str(arr[num+1]) + ")"]
        num+=2
    else:
        if int(arr[num]) > 0 and int(arr[num+1]) > 0:
            kuadran += [1]
            arr2 += ["(" + str(arr[num]) + ", " + str(arr[num+1]) + ")"]
            num+=2
        elif int(arr[num]) < 0 and int(arr[num+1]) > 0:
            kuadran += [2]
            arr2 += ["(" + str(arr[num]) + ", " + str(arr[num+1]) + ")"]
            num+=2
        elif int(arr[num]) < 0 and int(arr[num+1]) < 0:
            kuadran += [3]
            arr2 += ["(" + str(arr[num]) + ", " + str(arr[num+1]) + ")"]
            num+=2
        elif int(arr[num]) > 0 and int(arr[num+1]) < 0:
            kuadran += [4]
            arr2 += ["(" + str(arr[num]) + ", " + str(arr[num+1]) + ")"]
            num+=2

def jumlahKuadran(a):
    ans = 0
    for i in range(len(kuadran)):
        if kuadran[i] == a:
            ans+=1
    return "Jumlah Kuadran " + str(a) + " : " + str(ans)

def dataKuadran(a):
    for i in range(len(kuadran)):
        if kuadran[i] == a:
            print(arr2[i])

def plot(a):
    for i in range(len(kuadran)):
        print(str(arr2[i]))

print("############# Plot Koordinat #############")
plot(read)
print()
print(jumlahKuadran(k))
print()
print("############# Data Yang Bernilai Kuadran " + str(k) + " #############")
dataKuadran(k)
