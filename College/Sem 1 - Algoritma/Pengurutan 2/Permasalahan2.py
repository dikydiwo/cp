x = input().split()
data = []

first  = 0
second = 1
result = 0

ans = 0

for i in range(int(x[0])):
    result = first + second
    data += [first]
    first = second
    second = result

for i in range(len(data)):
    if data[i] == int(x[1]):
        ans = i + 1
        break

print(ans)