x = input().split()
y = input().split()

condA  = True
condS  = True
condSS = True

if y[0] == "awal" or y[0] == "akhir":
    for i in range(len(x)):
        if y[1] == x[i]:
            condA = False
            break
elif y[0] == "samping":
    for i in range(len(x)):
        if y[1] == x[i]:
            condS = False
            break
    for i in range(len(x)):
        if y[2] == x[i]:
            condSS = True
            break
        else:
            condSS = False

arr = []
if y[0] == "awal" and condA == True:
    for i in range(len(x)+1):
        if i == 0:
            arr += [int(y[1])]
        else:
            arr += [int(x[i-1])]
elif y[0] == "akhir" and condA == True:
    for i in range(len(x)+1):
        if i == len(x):
            arr += [int(y[1])]
        else:
            arr += [int(x[i])]
elif y[0] == "samping" and condS == True and condSS == True:
    for i in range(len(x)):
        if x[i] == y[2]:
            arr += [int(x[i])]
            arr += [int(y[1])]
        else:
            arr += [int(x[i])]
else:
    for i in range(len(x)):
        arr += [int(x[i])]

print(arr)