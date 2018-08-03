from LinkedList import LinkedList

# Stack Implementation using LinkedList

class Stack:

# constructor : initialises Stack
	def __init__(self):
		self.stack = LinkedList()
		self._top = None

# toString : returns string in form of list
	def __str__(self):
		return ('top -> '+str(self.stack))

# representation : returns representation in form of list
	def __repr__(self):
		return ('top -> '+str(self.stack))

# method set_top : sets element on top of stack
# parameter : element - element to be set at top of stack
# returns : nothing
	def set_top(self, element):
		self._top = element

# method get_top : gets element on top of stack
# parameter : no parameters
# returns : returns element on top of stack
	def get_top(self):
		return self._top

# method get : gets element on top of stack
# parameter : no parameters
# returns : returns element on top of stack
	def top(self):
		return self._top.get_data()

# method push : inserts data onto stack
# parameters : data - data to be inserted
# returns : nothing
	def push(self, data):	
		self.stack.insert_first(data)
		self.set_top(self.stack.get_head())

# method pop : removes and returns element on top of stack
# parameters : no parameters
# returns : 	None - if stack is empty (underflow), else
#		data - element on top of stack
	def pop(self):
		if self.stack.get_length() == 0:
			return None
		data = self.top()
		self.stack.delete_first()
		self.set_top(self.stack.get_head())
		return data

# method is_empty : check if stack is empty
# parameters : no parameters
# returns :	True - if stack is empty
#		False - if stack is not empty
	def is_empty(self):
		return self.stack.get_length() == 0

# method size : returns size of stack
# parameters : no paramters
# returns : size of stack (number of elements present in stack)
	def size(self):
		return self.stack.get_length()
		