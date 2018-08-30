# BinaryHeap implementation using list

class BinaryHeap:

# constructor : initialises Binary Tree
# data : list of data element
# max :	True - for max heap
	False - for min heap
	def __init__(self, data=None, max=True):
		if max:
			self.compare = lambda side, largest: side > largest
			self.data = [float("infinity")]
		else:
			self.compare = lambda side, smallest: side < smallest
			self.data = [0]
		if data is None:
			return 
		self.data += data		# calculation and readability convenience
		self.heapify_tree()			
	
# toString : return heap in array form as string
	def __str__(self):
		return str(self.data[1:])
	
# representation : return heap in array form for representation
	def __repr__(self):
		return str(self.data[1:])

# method heapify_tree : heapify entire tree
	def heapify_tree(self):
		n = (len(self.data) - 1) // 2
		while n >= 1:
			self.heapify(n)
			n -=1

# method heapify : heapify passed node
# parameters :	p - node index to heapify
# returns : nothing
	def heapify(self, p):
		l = 2 * p
		r = l + 1
		toswap = p
		if l < len(self.data):
			if self.compare(self.data[l], self.data[toswap]):
				toswap = l
		if r < len(self.data):
			if self.compare(self.data[r], self.data[toswap]):
				toswap = r
		if toswap != p:
			temp = self.data[toswap]
			self.data[toswap] = self.data[p]
			self.data[p] = temp
			self.heapify(toswap)

# method extract_root : extract root from heap
# returns : data of root
	def extract_root(self):
		if len(self.data) < 2:
			return None
		temp = self.data[1]
		last = self.data.pop()
		if len(self.data) > 1:		# debug IndexError - for last element
			self.data[1] = last
			self.heapify(1)
		return temp

# method insert : insert key to heap
# parameters :	key - input key
# returns : nothing
	def insert(self, key):
		n = len(self.data)
		self.data.append(key)
		while (n > 0) and self.compare(self.data[n], self.data[n//2]):
			temp = self.data[n]
			self.data[n] = self.data[n//2]
			self.data[n//2] = temp
			n //= 2