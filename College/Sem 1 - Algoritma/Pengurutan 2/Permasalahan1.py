s = input().split()

alph = []
val  = []

for i in range(97,123):
    alph += ["%c"%i]
for i in range(1,27):
    val += [i]

def cnt(a):
    ans = 0
    for i in range(len(a)):
        for j in range(len(alph)):
            if a[i] == alph[j]:
                ans += val[j]
                break
    return ans

if cnt(s[0]) > cnt(s[1]): print(s[0])
elif cnt(s[0]) < cnt(s[1]): print(s[1])
else: print("sama")