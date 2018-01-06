x = str(input()).upper()

pangkat = 0
num = int()
arr = []

for i in range(0, len(x)):

    arr += [0]

    if x[i] == 'A':
        arr[i] = 10
    elif x[i] == 'B':
        arr[i] = 11
    elif x[i] == 'C':
        arr[i] = 12
    elif x[i] == 'D':
        arr[i] = 13
    elif x[i] == 'E':
        arr[i] = 14
    elif x[i] == 'F':
        arr[i] = 15
    else:
        arr[i] = x[i]

for i in range(len(arr)-1,-1,-1):
    num += (16**pangkat) * int(arr[i])
    pangkat += 1

num1 = num
binary = str()
reverse = str()

while num1 > 0:
    modBinary = num1 % 2
    num1 //= 2
    binary += str(modBinary)

for i in range(len(binary)):
    reverse += binary[i]

print(num, reverse)