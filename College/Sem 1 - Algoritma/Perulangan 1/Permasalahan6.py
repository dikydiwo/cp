x = int(input())
arr   = []
count = [0,0,0,0,0,0,0,0,0,0]
for i in range(x):
    y = int(input())
    arr += [y]

for k in range(len(arr)):
    for l in range(0,10):
        if arr[k] == l:
            count[l] += 1

for m in range(0,10):
    print(count[m])
