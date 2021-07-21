def pascal_triange(n):
	output = [[0 for i in range(n)] for j in range(n)]
	for i in range(n):
		for j in range(n-i): # no of space before 1st row = 4, 2nd row = 3 ... 5th row = 0
			print(' ', end = '')
		for j in range(i+1):
			if j == 0 or j == i:
				output[i][j] = 1
				print(' ', output[i][j], end='')
			else:
				output[i][j] = output[i-1][j-1] + output[i-1][j]
				print(' ', output[i][j], end='')
		print()

	return output

def pascal_triangle_using_PnC(n):
	C = 1
	for i in range(n):
		for j in range(i+1):
			if j == 0 or j == i+1:
				print(C, end='')
			else: 
				C = C * (i - j + 1)//j
				print(' ', C, sep =' ', end ='')
		print()


if __name__ == '__main__':
	n = 5
	# print(pascal_triange(n))
	pascal_triangle_using_PnC(n)

