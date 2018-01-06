x = int(input())
y = int(input())

matrix = []

for i in range(x):
	matrix += [[]]
	data = input().split()
	for j in range(y):
		matrix[i] += [int(data[j])]

top       = 0
bottom    = x-1
left      = 0
right     = y-1
direction = 0

while top <= bottom and left <= right:
	if direction == 0:
		for i in range(left, right+1):
			print(matrix[top][i], end=" ")
		top += 1
		direction = 1
	elif direction == 1:
		for i in range(top, bottom+1):
			print(matrix[i][right], end=" ")
		right -= 1
		direction = 2
	elif direction == 2:
		for i in range(right, left-1, -1):
			print(matrix[bottom][i], end=" ")
		bottom -= 1
		direction = 3
	elif direction == 3:
		for i in range(bottom, top-1, -1):
			print(matrix[i][left], end=" ")
		left += 1
		direction = 0