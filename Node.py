# class SLNode is class for Single Link Node. 
# It implements methods that are common and applicable to all Linked List Node.

class SLNode:

# constructor : initialises Single Link Node
# data : hold data of self node
# next : holds reference to next node
	def __init__(self, data = None, next = None):
		self.data = data
		self.next = next

# representation : returns data		
	def __repr__(self):
		return str(self.get_data())

# toString : returns data
	def __str__(self):
		return str(self.get_data())
	
# method set_data : sets given data to self node
# parameters : data - given data
# returns : nothing
	def set_data(self, data):
		self.data = data
	
# method get_data : gets data of self node	
# parameters : no parameters
# returns : data of self node
	def get_data(self):
		return self.data
	
# method set_next : sets next node to self node 
# parameters : next - next node
# returns : nothing
	def set_next(self, next):
		self.next = next
	
# method get_next : gets next node of self node	
# parameters : no parameters
# returns : next node to self node
	def get_next(self):
		return self.next
	
# method has_next : checks if next node is available
# parameters : no parameters
# returns : 	true - if next node is available
#		false - if next node is None	
	def has_next(self, last_next = None):
		return self.next != last_next
		
##########################################################

# class DLNode is class for Double Link Node
# It extends SLNode and adds previous (second link)

class DLNode(SLNode):

# constructor : initialises Double Link Node
# prev : holds reference to previous node
	def __init__(self, data = None, prev = None, next = None):
		super().__init__(data, next)
		self.prev = prev

# method set_prev : sets prev node to self node 
# parameters : prev - prev node
# returns : nothing
	def set_prev(self, prev):
		self.prev = prev
	
# method get_prev : gets prev node of self node	
# parameters : no parameters
# returns : prev node to self node
	def get_prev(self):
		return self.prev
	
# method has_prev : checks if prev node is available
# parameters : no parameters
# returns : 	true - if prev node is available
#		false - if prev node is None	
	def has_prev(self, first_prev = None):
		return self.prev != first_prev

##########################################################
	
# Binary Tree Node - node definition for binary tree
	
class BinaryTreeNode:
# constructor : initialises Binary Tree Node
# data : holds data
# left : points to left node
# right : points to right node
	def __init__(self, data, left = None, right = None):
		self.data = data
		self.left = left
		self.right = right

# representation : returns data		
	def __repr__(self):
		return str(self.get_data())

# toString : returns data
	def __str__(self):
		return str(self.get_data())

# method set_data : sets data in Binary Node
# parameters : data - data to insert
# returns : nothing
	def set_data(self, data):
		self.data = data

# method get_data : gets data in Binary Node
# parameters : no parameters
# returns : data element of node
	def get_data(self):
		return self.data

# method get_left : gets left sub tree
# parameters : no parameters
# returns : left subtree of node
	def get_left(self):
		return self.left

# method get_right : gets right sub tree
# parameters : no parameters
# returns : right subtree of node
	def get_right(self):
		return self.right

# method set_left : sets left sub tree to node
# parameters : node - root of left sub tree
# returns : nothing
	def set_left(self, node):
		self.left = node

# method set_right : sets right sub tree to node
# parameters : node - root of right sub tree
# returns : nothing
	def set_right(self, node):
		self.right = node

			
