s = input().split()
sortby = str(input())

if sortby == "asc":
    for i in range(len(s)):
        for j in range(i+1,len(s)):
            if s[j] < s[i]:
                s[i],s[j] = s[j],s[i]
        print(s[i])
elif sortby == "desc":
    for i in range(len(s)):
        for j in range(i+1, len(s)):
            if s[j] > s[i]:
                s[i],s[j] = s[j],s[i]
        print(s[i])