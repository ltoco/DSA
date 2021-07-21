class Node:
	def __init__(self, data=None):
		self.data = data
		self.next = None

class Head:
	def __init__(self, node=None):
		self.next = node

if __name__ == '__main__':
	node1 = Node(10)
	node2 = Node(20)
	node3 = Node(30)
	
	# head.next = node1
	head = node1
	node1.next = node2
	node2.next = node3
	# head = Head(node1)
	print(f"node1.next.next.data: {node1.next.next.data}")
	print("Printing linked list")
	while(head):
		print(head.data)
		head = head.next
