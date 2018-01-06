x = input().split()
pembilang = int(x[0])
penyebut  = int(x[1])
for i in range(0, int(x[4])):
    if(pembilang % penyebut == 0):
        total = pembilang / penyebut
        print(int(total))
    else:
        print(str(pembilang) +'/'+str(penyebut))
    pembilang += int(x[2])
    penyebut  += int(x[3])
