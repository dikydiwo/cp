x = int(input())
num1 = 0
num2 = 1
result = int()
hasil  = []
for i in range(x):
    result = num1 + num2
    hasil.append(num1)
    num1 = num2
    num2 = result

index = len(hasil)
reverse = str()

for a in range(x):
    reverse += str(hasil[index - 1]) + "\n"
    index -= 1

print(reverse)
