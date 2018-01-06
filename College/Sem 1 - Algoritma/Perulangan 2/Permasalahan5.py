x = str(input())

arr = x.split()

num  = arr[0]
num1 = arr[1]

hasil  = int()
hasil1 = int()
a = 0
b = 0
total = int()

binary = str()

for i in range(len(num)-1,-1,-1):
    hasil += int(num[i]) * (2**a)
    a += 1

for i in range(len(num1)-1,-1,-1):
    hasil1 += int(num1[i]) * (2**b)
    b += 1

total = hasil + hasil1

while total > 0:
    modBinary = total % 2
    total //= 2
    binary += str(modBinary)

reverse = str()

for i in range(len(binary)-1,-1,-1):
    reverse += binary[i]

print(reverse)