x = str(input()).lower()

arr = [0,0,0,0,0]

for i in range(0, len(x)):
    if x[i] == 'a':
        arr[0] += 1
    elif x[i] == 'e':
        arr[1] += 1
    elif x[i] == 'i':
        arr[2] += 1
    elif x[i] == 'o':
        arr[3] += 1
    elif x[i] == 'u':
        arr[4] += 1

for i in range(len(arr)):
    print(arr[i])