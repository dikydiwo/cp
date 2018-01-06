x = input().split()
y = input().split()

def cekArray(a,b):
    ans = False
    if len(a) == len(b):
        for i in range(len(a)):
            if a[i] == b[i]:
                ans = True
            else:
                ans = False
                break
    return ans

print(cekArray(x,y))