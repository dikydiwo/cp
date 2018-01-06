x = str(input())

reverse = str()

for i in range(len(x)-1,-1,-1):
    reverse += x[i]

if x.lower() == reverse.lower():
    print('palindrom')
else:
    print('bukan palindrom')