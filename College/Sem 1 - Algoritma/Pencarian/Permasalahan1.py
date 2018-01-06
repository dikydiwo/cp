key = [2,22,222,3,33,333,4,44,444,5,55,555,6,66,666,7,77,777,7777,8,88,888,9,99,999,9999,0]
val = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ']

s = input().split()
ans = ""

for i in range(len(s)):
	for j in range(len(key)):
		if s[i] == str(key[j]):
			ans += val[j]
			break

print(ans)
