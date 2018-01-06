x = str(input()).lower()

arr = [0,0]

for i in range(len(x)):
    if x[i] == 'a' or x[i] == 'e' or x[i] == 'i' or x[i] == 'o' or x[i] == 'u':
        arr[0] += 1
    else:
        arr[1] += 1

for i in range(len(arr)):
    print(arr[i])
