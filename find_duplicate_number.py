import sys

def hare_tortoise(arr):
	slow, fast = arr[0], arr[0]
	print(f"Slow: {slow}, Fast: {fast}")
	while(True):
		slow = arr[slow]
		fast = arr[arr[fast]]
		print(f"Slow: {slow}, Fast: {fast}")
		if slow == fast:
			break

	# sys.exit()
	slow = arr[0]
	print("After repositioning")
	print(f"Slow: {slow}, Fast: {fast}")

	# We do slow!=fast and not while(true) because there are chances that afte the 1st while and reinitialization, 
	# slow and fast would already be pointing the same element and we need not go inside the for loop as we have
	# already found the duplicate element
	while(slow!=fast):
		slow = arr[slow]
		fast = arr[fast]
		print(f"Slow: {slow}, Fast: {fast}")
		# if slow == fast:
		# 	break

	return slow

if __name__ == '__main__':
	arr = [1,3,4,2,2]
	arr = [5,2,6,5,3,4,1] 
	# arr = [3,1,3,4,2]
	duplicate = hare_tortoise(arr)
	print(duplicate)

