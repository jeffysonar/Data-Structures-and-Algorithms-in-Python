from Node import SLNode as Node
from Node import DLNode as DNode

# Singly Linked List
class LinkedList:

# constructor : initialises Linked List
# head : head (first) node of Linked List
# length : number of elements/length in/of Linked List
	def __init__(self):
		self.length = 0
		self.head = None
	
# representation : returns as a list
	def __repr__(self):
		return str(self.get_list())

# toString : returns as a list
	def __str__(self):
		return str(self.get_list())	

# method create_node : creates a Link Node
# parameters : data - given data
# returns : a new node
	def create_node(self, data = None, next = None):
		return Node(data, next)

# method get_last_next : TWEAK to inherit methods for circular linked list easily
# parameters : no parameters
# return : None as next of last node
	def get_last_next(self):
		return None

# method get_head : gets first node of Linked List
# parameters : no parameters
# returns : head (first node) of Linked List
	def get_head(self):
		return self.head
	
# method set_head : sets first node of Linked List
# parameters : node - a Single Link Node
# returns : nothing	
	def set_head(self, node):
		self.head = node

# method get_head : gets first node of Linked List
# paramters : no parameters
# returns : length of Linked List
	def get_length(self):
		return self.length

# method incr_head : increments length of Linked List by 1
	def incr_length(self):
		self.length = self.length + 1

# method decr_length : decrements length of Linked List by 1
	def decr_length(self):
		self.length = self.length - 1

# method get_list : gets Linked List as a List
# parameters : no parameters
# returns : list of data elements in Linked List
	def get_list(self):
		if self.get_length() != 0:
			current = self.get_head()
			llist = []
			while current != self.get_last_next():
				llist.append(current.get_data())
				current = current.get_next()
			return llist
		else:
			return []
	
		
# insert methods

# method insert_first : inserts a new node to head of Linked List
# parameters : data - data to insert in new node
# returns : nothing
	def insert_first(self, data):
		nnode = self.create_node(data)		
		if self.get_length() == 0:
			self.set_head(nnode)
			nnode.set_next(self.get_last_next())
		else:
			nnode.set_next(self.get_head())
			self.set_head(nnode)
		self.incr_length()

# method insert_last : inserts a new node to tail of Linked List
# parameters : data - data to insert in new node	
# returns : nothing
	def insert_last(self, data):
		if self.get_length() == 0:
			self.insert_first(data)
			return
		nnode = self.create_node(data, self.get_last_next())
		current = self.get_head()
		while current.has_next(self.get_last_next()):
			current = current.get_next()
		current.set_next(nnode)
		self.incr_length()
	
# method insert_index : inserts a new node at given location (index)
# parameters : 	data - data to be inserted
#		index - position from 0
# returns : nothing
	def insert_index(self, data, index):
		if index == 0:
			return self.insert_head(data)
		# if index is greater than or equal to last index , insert into last	
		if index >= (self.get_length() - 1):
			return self.insert_last(data)
		nnode = self.create_node(data)
		count = 0
		current = self.get_head()
		while count < (index - 1):
			count = count + 1
			current = current.get_next()
		nnode.set_next(current.get_next())
		current.set_next(nnode)
		self.incr_length()

# method insert : general method for insert
# parameters :	data - data to be inserted
#		index - position from 0
# returns : nothing
	def insert(self, data, index = -1):
		if ((index == 0) | (self.get_length() == 0)):
			self.insert_first(data)
		elif ((index != -1) & (index < self.get_length())):
			self.insert_index(data, index)
		else:
		# for index not mentioned or exceeds list_length
			self.insert_last(data)

# delete methods

# method delete_first : deletes first node of Linked List
# parameters : no parameters
# returns : 	True - successful delete
#		False - if list is empty
	def delete_first(self):
		if self.get_length() <= 0:
			return False
		if self.get_length() > 1:
			nnode = self.get_head()
			self.set_head(nnode.get_next())
			nnode.set_next(None)
		else:
			if self.get_length() == 1:
				self.set_head(None)
		self.decr_length()
		return True	

# method delete_last : deletes last node of Linked List
# parameters : no parameters
# returns : 	True - successful delete
#		False - if list is empty
	def delete_last(self):
		if self.get_length() <= 0:
			return False
		if self.get_length() > 1:
			current = self.get_head()
			while current.get_next().has_next(self.get_last_next()):
				current = current.get_next()
			current.get_next().set_next(None)
			current.set_next(self.get_last_next())
		else: 
		# single node left
			self.set_head(None)
		self.decr_length()
		return True

# method delete_index : deletes node at given index
# parameters :	index - position from 0
# returns : 	True - successful delete
#		False - List is empty or given position is invalid
	def delete_index(self, index = -1):
		if index == -1:
			return False
		if self.get_length() != 0:
			if index == 0:
				self.delete_first()
			elif ((index > 0) & (index < self.get_length())):
				current = self.get_head()
				count = 0
				while count < (index - 1):
					current = current.get_next()
					count = count + 1
				current.set_next(current.get_next().get_next())
				self.decr_length()
				return True
			else:
				# raise ValueError('Invalid position')
				return False
		else:
			# raise ValueError('List is empty')
			return False

# method delete_data : deletes node with given data
# parameters :	data - Data to remove
#		all - True if all node with same data is to be deleted, else False
# returns : nothing
	def delete_data(self, data = None, all = False):
		if data == None:
			return False
		while self.get_head() != None:
			if self.get_head().get_data() == data:
				self.delete_first()
				if not all:
					return True
			else:
				break
		if self.get_length() != 0:
			previous = self.get_head()
			current = previous.get_next()
			while previous.has_next(self.get_last_next()):
				current = previous.get_next()
				if current.get_data() == data:
					previous.set_next(current.get_next())
					current.set_next(None)
					self.decr_length()
					if not all:
						return True
					continue
				previous = previous.get_next()
								
# method delete : general method for delete
# parameters :	data - data to be deleted
#		all - True if all node with same data is to be deleted, else False
#		index - position from 0 
# returns : False
	def delete(self, data = None, all = False, index = -1):
		if ((data == None) & (index == -1)):
			return
		if index != -1 :
			self.delete_index(index)
		else:
			self.delete_data(data, all)

# get methods
# method get_first : get first data element
# parameters : no parameters
# returns : 	None - if list is empty, else
#		data - data part of node
	def get_first(self):
		if self.get_head() != None:
			return self.get_head().get_data()
		else:
			return None

# method get_last : get last data element
# parameters : no parameters
# returns : 	None - if list is empty, else
#		data - data part of node
	def get_last(self):
		if self.get_length() == 0:
			return None
		if self.get_length() == 1:
			return self.get_first()
		else:
			current = self.get_head().get_next()
			while current.get_next() != self.get_last_next():
				current = current.get_next()
			return current.get_data()

# method get_element : get data element
# parameters : index - position from 0 
# returns : 	None - if list is empty, else
#		data - data part of node
	def get_element(self, index):
		if (index < 0) | (index >= self.get_length()):
			return None
		if index == 0:
			return self.get_first()
		else:
			current = self.get_head()
			for i in range(index):
				current = current.get_next()
			return current.get_data()

# method get : general method to get data element
# parameters : index - position from 0 
# returns : 	None - if list is empty, else
#		data - data part of node
	def get(self, index = -1):
		if index == -1:	
			return self.get_first()
		else: 
			return self.get_element(index)

# Singly Circular Linked List. 
# It extends Singly Linked List and implements (extends) only those concern with circular part.
# Rest is directly inherited.
class CircularList(LinkedList):
	
# constructor : initialises Circular LinkedList
# simply calling LinkedList constructor, no additional properties
	def __init__(self):
		super().__init__()
	
# representation : returns LL as a list
	def __repr__(self):
		return str(self.get_list())


# toString : returns LL as a list
	def __str__(self):
		return str(self.get_list())	

# method get_last_next : TWEAK implementation that saves lot of EFFORTS
	def get_last_next(self):
		return self.get_head()

# method get_list : gets Linked List as a List
# parameters : no parameters
# returns : list of data elements in Linked List
	def get_list(self):
		if self.length != 0:
			llist = [self.get_head().get_data()]
			current = self.get_head().get_next()
			while current != self.get_last_next():	
				llist.append(current.get_data())
				current = current.get_next()
			return llist
		else:
			return []

# method insert_first : extends base class method to update last_next to new head link
# parameters : data - data to insert in new node
# returns : nothing
	def insert_first(self, data):
		super().insert_first(data)
		current = self.get_head().get_next()
		while current.get_next() != self.get_last_next().get_next():
			current = current.get_next()
		current.set_next(self.get_head())

# method delete_first : extends base class method to update last_next to new head link
# parameters : no parameters
# returns :	True - for successful delete
#		False - if list is empty
	def delete_first(self):
		temp_head = self.get_head()
		if super().delete_first():
			current = self.get_head().get_next()
			while current.get_next() != temp_head:
				current = current.get_next()
			current.set_next(self.get_head())
			return True
		else:
			return False 

# Doubly Linked List
# It extends Simply Linked List and implements (extends methods) that only is concerned with second (prev) link.
# Rest is directly inherited.
class DLinkedList(LinkedList):

# constructor : initialises Circular Linked List
# tail : tail (last) node of Linked List
	def __init__(self):
		super().__init__()
		self.tail = None
	
# representation : returns as a list
	def __repr__(self):
		return str(self.get_list())

# toString : returns as a list
	def __str__(self):
		return str(self.get_list())

# method create_node : creates a Link Node
# parameters : data - given data
# returns : a new node
	def create_node(self, data = None, prev = None, next = None):
		return DNode(data, prev, next)

# method get_tail : gets last node of Linked List
# parameters : no parameters
# returns : tail (last node) of Linked List
	def get_tail(self):
		return self.tail
	
# method set_tail : sets last node of Linked List
# parameters : node - a Single Link Node
# returns : nothing	
	def set_tail(self, node):
		self.tail = node


# method get_first_prev: TWEAK to inherit methods for circular Doubly Linked List
# parameters : no parameters
# returns : return prev of first node
	def get_first_prev(self):
		return None

# get_list inclusive of reversal
# method get_list : extends base class method by adding reverse traversal
# parameters : reverse - if list is to be parsed in reverse order
# returns : list of data elements in Linked List
	def get_list(self, reverse = False):
		if self.get_length() != 0:
			if reverse:
				current = self.get_tail()
				llist = []
				while current != self.get_first_prev():
					llist.append(current.get_data())
					current = current.get_prev()
				return llist
			else:
				return super().get_list()
		else:
			return []

# insert methods

# method insert_first : inserts a new node to head of Linked List
# parameters : data - data to insert in new node
# returns : nothing
	def insert_first(self, data):
		super().insert_first(data)
		# above method increments length of LL
		if self.get_length() > 1:
			# setting prev of second node
			self.get_head().get_next().set_prev(self.get_head())
		else: # it is 1
			self.set_tail(self.get_head())

# method insert_last : inserts a new node to tail of Linked List
# parameters : data - data to insert in new node
# returns : nothing
	def insert_last(self, data):
		if self.get_length() == 0:
			return self.insert_first(data)
		nnode = self.create_node(data, self.get_tail(), self.get_last_next())
		self.get_tail().set_next(nnode)
		self.set_tail(nnode)
		self.incr_length()

# method insert_index : inserts a new node at given location (index)
# parameters : 	data - data to be inserted
#		index - position from 0
# returns : nothing
	def insert_index(self, data, index):
		if index == 0:
			return self.insert_first(data)
		# if index is last index or greater, insert at last
		if index >= (self.get_length() - 1):
			return self.insert_last(data)
		nnode = self.create_node(data)
		count = 0
		current = self.get_head()
		while count < (index - 1):
			count = count +1
			current = current.get_next()
		nnode.set_next(current.get_next())
		nnode.set_prev(current)
		current.get_next().set_prev(nnode)
		current.set_next(nnode)
		self.incr_length()

# delete methods

# method delete_first : deletes first node of Linked List
# parameters : no parameters
# returns : 	True - successful delete
#		False - if list is empty
	def delete_first(self):
		if super().delete_first():
			if self.get_length() > 1:
				self.get_head().set_prev(None)
			else: # length = 1 or 0
				if self.get_length() == 1:
					self.set_tail(self.get_head())
				else:
					self.set_tail(None)
			return True			
		else:
			return False

# method delete_last : deletes last node of Linked List
# parameters : no parameters
# returns : 	True - successful delete
#		False - if list is empty
	def delete_last(self):
		if self.get_length() <= 0:
			return False
		if self.get_length() == 1:
			return self.delete_first()
		temp = self.get_tail()
		self.set_tail(temp.get_prev())
		self.get_tail().set_next(None)
		temp.set_prev(None)
		self.decr_length()
		return True

# method delete_index : deletes node at given index
# parameters :	index - position from 0
# returns : 	True - successful delete
#		False - List is invalid or given position is invalid
	def delete_index(self, index = -1):
		if index == -1:
			return False
		if self.get_length() != 0:
			if index == 0:
				return self.delete_first()
			elif index == (self.get_length() - 1):
				return self.delete_last()
			elif ((index > 0) & (index < (self.get_length() - 1))):
				current = self.get_head()
				count = 0
				while count < (index - 1):
					current = current.get_next()
					count = count + 1
				temp = current.get_next()
				current.set_next(temp.get_next())
				temp.set_prev(None)
				temp.set_next(None)
				temp = current.get_next()
				temp.set_prev(current)
				self.decr_length()
				return True	
		else:
			return False

# method delete_data : deletes node with given data
# parameters :	data - Data to remove
#		all - True if all node with same data is to be deleted, else False
# returns : nothing
	def delete_data(self, data = None, all = False, reverse = False):
		if data == None:
			return False
		if reverse:
			while self.get_tail() != None:
				if self.get_tail().get_data() == data:
					self.delete_last()
					if not all:
						return True
				else:
					break
			if self.get_length() != 0:
				next = self.get_tail()
				current = next.get_prev()
				while next.has_prev(self.get_first_prev()):
					current = next.get_prev()
					if current.get_data() == data:
						next.set_prev(current.get_prev())
						if current.get_prev() != self.get_first_prev():
							current.get_prev().set_next(next)
						else:
							self.set_head(next)
						current.set_next(None)
						current.set_prev(None)
						self.decr_length()
						if not all:
							return True
						continue
					next = next.get_prev()
		else:
			while self.get_head() != None:
				if self.get_head().get_data() == data:
					self.delete_first()
					if not all:
						return True
				else:
					break
			if self.get_length() != 0:
				previous = self.get_head()
				current = previous.get_next()
				while previous.has_next(self.get_last_next()):
					current = previous.get_next()
					if current.get_data() == data:
						previous.set_next(current.get_next())
						if current.get_next() != self.get_last_next():
							current.get_next().set_prev(previous)
						else:
							self.set_tail(previous)
						current.set_next(None)
						current.set_prev(None)
						self.decr_length()
						if not all:
							return True
						continue
					previous = previous.get_next()

# method delete : general method for delete
# parameters :	data - data to be deleted
#		all - True if all node with same data is to be deleted, else False
#		index - position from 0 
# returns : False
	def delete(self, data = None, all = False, index = -1, reverse = False):
		if ((data == None) & (index == -1)):
			return
		if index != -1 :
			self.delete_index(index)
		else:
			self.delete_data(data, all, reverse)
					
# get methods

# method get_last : get last data element
# parameters : no parameters
# returns : 	None - if list is empty, else
#		data - data part of node
	def get_last(self):
		if self.get_tail() != None:
			return self.get_tail().get_data()
		else:
			return None

# method get_element : get data element (for last n/2 element to improve performance)
# parameters : index - position from 0 
# returns : 	None - if list is empty, else
#		data - data part of node
	def get_element(self, index):
		if (index < 0) | (index >= self.get_length()):
			return None
		if index == 0:
			return self.get_first()
		elif index == (self.get_length() - 1):
			return self.get_last()
		else:
			if index < (self.get_length()/2): 
				current = self.get_head()
				for i in range(index):
					current = current.get_next()
				return current.get_data()
			else:
				current = self.get_tail()
				for i in range(self.get_length() - index - 1):
					current = current.get_prev()
				return current.get_data() 

# Doubly Circular Linked List
# It extends DLinkedList and implements (extends methods) that are concerned with circular part.
# Rest is directly inherited.
class DCircularList(DLinkedList):

# constructor : initialises constructor
# simply calling DLinkedList constructor
	def __init__(self):
		super().__init__()

# representation : returns LL as a list
	def __repr__(self):
		return str(self.get_list())

# toString : returns LL as a list
	def __str__(self):
		return str(self.get_list())

# method get_last_next : TWEAK implementation
	def get_last_next(self):
		return self.get_head()

# method get_first_prev : TWEAK implementation to Doubly
	def get_first_prev(self):
		return self.get_tail()

# method get_list : extends base class method by adding reverse traversal
# parameters : reverse - if list is to be parsed in reverse order
# returns : list of data elements in Linked List
	def get_list(self, reverse = False):
		if self.get_length() != 0:
			if reverse:
				llist = [self.get_tail().get_data()]
				current = self.get_tail().get_prev()
				while current != self.get_first_prev():
					llist.append(current.get_data())
					current = current.get_prev()
				return llist
			else:				
				llist = [self.get_head().get_data()]
				current = self.get_head().get_next()
				while current != self.get_last_next():
					llist.append(current.get_data())
					current = current.get_next()
				return llist
		else:
			return []

# method insert_first : extends DLinkedList method to update end link pointing each other
# parameters : data - data to be inserted
# returns : nothing
	def insert_first(self, data):
		super().insert_first(data)
		self.get_head().set_prev(self.get_tail())
		self.get_tail().set_next(self.get_head())

# method insert_last : extends DLinkedList method to update end link pointing each other
# parameters : data - data to be inserted
# returns : nothing
	def insert_last(self, data):
		super().insert_last(data)
		# self.get_tail().set_next(self.get_head())
		# already done by passing in create_node
		# left to update first_prev
		self.get_head().set_prev(self.get_tail())

# method delete_first : extends DlinkedList method to update end link pointing each other
# parameters : no parameters
# returns :	True - successful deletion
#		False - if list is empty
	def delete_first(self):
		if super().delete_first():
			if self.get_length() > 0:
				self.get_head().set_prev(self.get_tail())
				self.get_tail().set_next(self.get_head())
			return True
		else:
			return False

# method delete_last : extends DLinkedList method to update end link pointing each other
# parameters : no parameters
# returns :	True - successful deletion
#		False - if list is empty
	def delete_last(self):
		if super().delete_last():
			if self.get_length() > 0:
				self.get_tail().set_next(self.get_head())
				self.get_head().set_prev(self.get_tail())
			return True
		else:
			return False

