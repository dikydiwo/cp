x = int(input())

for i in range(x):
    for j in range(x-i-1):
        print(' ', end="")
    for j in range(i*2+1):
        print('*', end="")
    print()

for i in range(x-2,-1,-1):
    for j in range(x-i-1):
        print(' ', end="")
    for j in range(i*2+1):
        print('*', end="")
    print()