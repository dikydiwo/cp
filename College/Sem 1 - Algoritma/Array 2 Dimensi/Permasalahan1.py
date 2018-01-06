x = input().split()
y = input().split()

matrix = []
start = 0
stop  = int(x[1])

for i in range(int(x[0])):
    matrix += [[]]
    for j in range(start, stop):
        matrix[i] += [int(y[j])]
    start += int(x[1])
    stop  += int(x[1])

print(matrix)
for i in range(int(x[0])):
    for j in range(int(x[1])):
        print(matrix[i][j],end=" ")
    print()