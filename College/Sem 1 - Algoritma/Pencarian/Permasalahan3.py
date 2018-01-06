s1 = input().split()
s2 = input().split()

big   = []
arr1  = []
arr2  = []
cond1 = False
cond2 = False

for i in range(len(s1)):
    for j in range(i+1,len(s1)):
        if int(s1[i]) > int(s1[j]):
            s1[i],s1[j] = s1[j],s1[i]

for i in range(len(s1)-1,-1,-1):
    big += s1[i]

for i in range(len(s2)):
    cond1 = False
    cond2 = False
    for j in range(len(big)):
        if int(big[j]) < int(s2[i]):
            cond1 = True
            break
    for j in range(len(big)):
        if cond1 == False:
            arr1 += ['X']
            break
        elif int(big[j]) < int(s2[i]) and cond1 == True:
            arr1 += [int(big[j])]
            break

    for j in range(len(s1)):
        if int(s1[j]) > int(s2[i]):
            cond2 = True
            break
    for j in range(len(s1)):
        if cond2 == False:
            arr2 += ['X']
            break
        elif int(s1[j]) > int(s2[i]) and cond2 == True:
            arr2 += [int(s1[j])]
            break

for i in range(len(s2)):
    print(arr1[i],arr2[i])