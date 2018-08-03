from LinkedList import LinkedList
from LinkedList import DLinkedList

# Simple Queue
class Queue:
	
# constructor : initialises Simple Queue
# _rear : points to rear of queue
	def __init__(self):
		self.queue = LinkedList()
		self._rear = None
		# front will be head of LinkedList in background
	
# toString : returns string in the form of list
	def __str__(self):
		return str(self.get_list())

# representation : represented in the form of list
	def __repr__(self):
		return str(self.get_list())

# method create_node : returns node of queue, useful to extend in priority queue
	def create_node(self, data):
		return self.queue.create_node(data)

# method get_list : gets list of elements
# parameters : no parameters
# returns :queue in the form of list
	def get_list(self):
		return self.queue.get_list()

# method get_front : returns front node of queue
	def get_front(self):
		return self.queue.get_head()

# method get_rear : returns rear node of queue
	def get_rear(self):
		return self._rear

# method set_front : sets front of queue
	def set_front(self, element):
		self.queue.set_head(element)

# method set_rear : sets rear of queue
	def set_rear(self, element):
		self._rear = element

# method front : returns data element at front node
	def front(self):
		return self.queue.get_head().get_data()

# method length : returns length of queue
	def length(self):
		return self.queue.get_length()

# method is_empty : checks if list is empty
# returns :	True - if queue is empty
		False - otherwise
	def is_empty(self):
		return self.length() == 0

# method enqueue : inserts data in queue
# parameters : data - data to add in queue
# returns : nothing
	def enqueue(self, data):
		nnode = self.create_node(data)
		if self.is_empty():
			self.set_front(nnode)
			self.set_rear(nnode)
		else:
			self.get_rear().set_next(nnode)
			self.set_rear(nnode)
		self.queue.incr_length()

# method dequeue : removes and returns first data element
# parameters : no parameters
# returns :	None - if queue is empty, else
# 		data - data element at front of queue
	def dequeue(self):
		if self.is_empty():
			return None
		else:
			data = self.front()
			self.queue.delete_first()
			if self.is_empty():
				self.set_rear(None)
			return data

# PriorityQueue : a new field 'priority' is added to each node
class PriorityQueue(Queue):

# constructor : initialises PriorityQueue
# ascending - True, if priority is ascending (small priority first). False, it is descending.
	def __init__(self, ascending = True):
		super().__init__()
		self.ascending = ascending
		if ascending:
			self.need_swap = lambda x, y : (x.priority >= y.priority)
		else:
			self.need_swap = lambda x, y : (x.priority <= y.priority)
	
# toString : returns string in the form of list
	def __str__(self):
		return str(self.get_list_priority())

# representation : represented in the form of list
	def __repr__(self):
		return str(self.get_list_priority())

# method create_node : returns node of queue, useful to extend in priority queue
	def create_node(self, data, priority):
		nnode = super().create_node(data)
		nnode.priority = priority
		return nnode

# method get_list_priority : gets list with elements as string - element (priority)
# parameters : no parameters
# returns : list of elements with priority 
	def get_list_priority(self):
		if self.length() != 0:
			current = self.get_front()
			llist = []
			while current != self.queue.get_last_next():
				llist.append(str(current.get_data())+' ('+str(current.priority)+')')
				current = current.get_next()
			return llist
		else:
			return []	

# method enqueue : inserts element into queue according to it's priority
# parameters :	data - data to insert
#		priority - priority of element
# returns : nothing
	def enqueue(self, data, priority):
		nnode = self.create_node(data, priority)
		if self.length() == 0:
			self.set_front(nnode)
			self.set_rear(nnode)
		else:
			if not self.need_swap(nnode, self.get_front()):
			# priority is high, attach to front
				nnode.set_next(self.get_front())
				self.set_front(nnode)
			elif self.need_swap(nnode, self.get_rear()):
			# priority is least, attach to rear
				self.get_rear().set_next(nnode)
				self.set_rear(nnode)
			else:
				current = self.get_front()
				next = self.get_front().get_next()
				while self.need_swap(nnode, next):
					current = current.get_next()
					next = current.get_next()	
				nnode.set_next(next)
				current.set_next(nnode)
		self.queue.incr_length()

# Double Ended Queue, directly extend Doubly Linked List
class DQueue(DLinkedList):
	
# constructor : initialises Double Ended Queue
	def __init__(self):
		super().__init__()

# method get_front : returns front of Queue	
	def get_front(self):
		return self.get_head()

# method get_rear : returns rear of Queue
	def get_rear(self):
		return self.get_tail()

# method front : returns data element of Queue
	def front(self):
		return self.get_front().get_data()

# method rear : returns data element of Queue
	def rear(self):
		return self.get_rear().get_data()

# method length : returns length of Queue
	def qlength(self):
		return self.get_length()

# method push_front : inserts to front of Queue
# paramters : data - data to insert to front of Queue
# returns : nothing
	def push_front(self, data):
		super().insert_first(data)

# method push_rear : inserts to rear of Queue
# parameters : data - data to insert to rear of Queue
# returns : nothing
	def push_rear(self, data):
		super().insert_last(data) 

# method pop_front : removes and returns element to front of Queue
# parameters : no parameters
# returns : 	None - if queue is empty
#		data - data element at front of Queue
	def pop_front(self):
		if self.qlength() == 0:
			return None
		else:
			data = self.front()
			super().delete_first()
			return data

# method pop_rear : removes and returns element to rear of Queue
# parameters : no parameters
# returns :	None - if queue is empty
#		data - data element at rear of Queue
	def pop_rear(self):
		if self.qlength() == 0:
			return 0
		else:
			data = self.rear()
			super().delete_last()
			return data

# method push : general method to push element
# parameters : 	data - data to be inserted
#		front - default is False, True if data element is to be pushed to front
# returns : nothing
	def push(self, data, front=False):
		if front:
			return self.push_front(data)
		else:
			return self.push_rear(data)

# method pop : general method to pop element
# parameters :	rear - default is False, True if data element is to be poped off rear
# returns : nothing
	def pop(self, rear=False):
		if rear:
			return self.pop_rear()
		else:
			return self.pop_front()