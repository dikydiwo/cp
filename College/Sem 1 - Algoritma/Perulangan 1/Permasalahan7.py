x = str(input())

arr = x.split()
index = len(arr)
count = [0,0,0,0,0,0,0,0,0,0]

for i in range(index):
    for j in range(0,10):
        if arr[i] == str(j):
            count[j] += 1

for k in range(0,10):
    print(count[k])