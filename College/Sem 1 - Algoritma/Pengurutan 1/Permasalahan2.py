s = str(input()).upper()

alph = []
cnt  = []

for i in range(65, 91):
    alph += ["%c"%i]
    cnt  += [0]

for i in range(len(alph)):
    for j in range(len(s)):
        if alph[i] == s[j]:
            cnt[i] += 1

for i in range(len(alph)):
    for j in range(i+1, len(alph)):
        if cnt[j] > cnt[i]:
            cnt[i],cnt[j]   = cnt[j],cnt[i]
            alph[i],alph[j] = alph[j],alph[i]

for i in range(len(alph)):
    for j in range(len(alph)):
        if alph[j] > alph[i] and cnt[i] == cnt[j]:
            alph[i],alph[j] = alph[j],alph[i]

for i in range(len(alph)):
    if cnt[i] != 0: print(alph[i],cnt[i])
