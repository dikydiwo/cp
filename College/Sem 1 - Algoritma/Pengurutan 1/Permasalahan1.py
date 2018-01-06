n = input().split()
m = int(input())

for i in range(len(n)):
    for j in range(i+1,len(n)):
        if int(n[i]) > int(n[j]):
            n[i],n[j] = n[j],n[i]

minimum = 0
maximum = 0

for i in range(m):
    minimum += int(n[i])

for i in range(len(n)-1,len(n)-m-1,-1):
    maximum += int(n[i])

print(minimum, maximum)