x = int(input())
arr = []
for i in range(1, x+1):
    if i % 2 == 0:
        arr += [i-1]
    else:
        arr += [i+1]
for j in range(len(arr)):
    print(arr[j])