import sys

def brute_force_1(arr):
	n = len(arr)
	max_sum = 0
	start = 0
	end = 0
	for i in range(0, n):
		for j in range(i, n):
			sum = 0
			for k in range(i, j+1):
				sum+=arr[k]
			if sum > max_sum:
				max_sum = sum
				start, end = i, j	

	return (max_sum, start, end)

def brute_force_2(arr):
	n = len(arr)
	max_sum = 0
	start = 0
	end = 0
	for i in range(0, n):
		sum = 0
		for j in range(i, n):
			sum+=arr[j]
			if sum > max_sum:
				max_sum = sum
				start, end = i, j
		print(f"sum: {sum}, i: {i}, j: {j}")
			

	return (max_sum, start, end)

def kadane_algo_1(arr):
	max_sum = arr[0]
	sum = 0
	start = 0
	end = 0
	pointer = 0
	n = len(arr)
	for i in range(n):
		sum+=arr[i]
		if sum > max_sum:
			start = pointer
			end = i
			max_sum = sum 
		if sum<0:
			sum = 0 
			pointer = i + 1

	return max_sum, start, end

def kadane_algo_2(arr):
	max_sum = arr[0]
	n = len(arr)
	start = 0
	end = 0
	pointer = 0
	for i in range(1, n):
		if arr[i-1] > 0:
			arr[i]+=arr[i-1]
		if arr[i] > max_sum:
			max_sum = arr[i]
	return max_sum

if __name__ == '__main__':
	# arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
	# arr = [5, 4, -1, 7, 8]
	arr = [-5, -4, -1, -9]
	# max_sum, start, end = brute_force_1(arr)
	# max_sum, start, end = brute_force_2(arr)
	max_sum, start, end = kadane_algo(arr)
	# print(max_sum)
	print(f"Max sum is: {max_sum}, start: {start}, end: {end}")
