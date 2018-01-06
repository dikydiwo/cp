x = str(input())

num = x.split()
arr = []
hasil = int()

for i in range(int(num[2]), int(num[0])*int(num[1]), int(num[1])):
    arr += [i]

for i in range(len(arr)):
    if i % 2 != 0:
        arr[i] = -arr[i]

for i in range(len(arr)):
    print(arr[i])

for i in range(len(arr)):
    hasil += int(arr[i])

print(hasil)