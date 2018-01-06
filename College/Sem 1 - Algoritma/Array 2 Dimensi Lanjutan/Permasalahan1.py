x = input().split()

matrix = []
ans = True

for i in range(int(x[0])):
	matrix += [[]]
	s = input().split()
	for j in range(int(x[1])):
		matrix[i] += [int(s[j])]

for i in range(int(x[0])):
	if matrix[i][i] == 1:
		for j in range(int(x[1])):
			if i != j:
				if matrix[i][j] == 1:
					ans = False
					break
	else:
		ans = False
		break


print("I") if ans else print("O")