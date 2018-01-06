x = str(input())
arr = x.split()
hasil = int()
for i in range(len(arr)):
    hasil += int(arr[i])

rata = hasil / len(arr)
print(hasil, "%.3f"%rata)