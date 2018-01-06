pembilang = []
penyebut  = []

for i in range(5):
    n = input().split()
    pembilang += [n[0]]
    penyebut  += [n[1]]

for i in range(5):
    for j in range(i+1, 5):
        if int(pembilang[j])/int(penyebut[j]) < int(pembilang[i])/int(penyebut[i]):
            pembilang[i],pembilang[j] = pembilang[j],pembilang[i]
            penyebut[i],penyebut[j]   = penyebut[j],penyebut[i]
    print(pembilang[i],penyebut[i])

