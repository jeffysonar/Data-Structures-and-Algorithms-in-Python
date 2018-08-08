from Node import BinaryTreeNode as BNode
from Queue import Queue
from Stack import Stack
from Sorting import insertion_sort as sort

class BinaryTree:

# constructor : initialises Binary Tree
# root : root of Binary Tree
# pre : preorder traversal list
# ino : inorder traversal list
# post : postorder traversal list
	def __init__(self, pre = None, ino = None, post = None):
		if pre and ino:
			self.build_pre_in(pre, ino)
		elif post and ino:
			self.build_post_in(post, ino)
		else:
			self.root = None

# toString : returns string with preorder, inorder and postorder traversal
	def __str__(self):
		return ("PreOrder : "+str(self.preorder())+"\nInOrder : "+str(self.inorder())+"\nPostOrder : "+str(self.postorder()))

# representation : returns representation with preorder, inorder and postorder traversal
	def __repr__(self):
		return ("PreOrder : "+str(self.preorder())+"\nInOrder : "+str(self.inorder())+"\nPostOrder : "+str(self.postorder()))

# method get_root : returns root of tree
	def get_root(self):
		return self.root

# method set_root : returns root of tree
	def set_root(self, root):
		self.root = root

# method build_pre_in : builds tree from preorder and inorder traversal list
# parameters :	pre - preorder traversal list
#		ino - inorder traversal list
# returns : root node of tree
	def build_pre_in(self, pre, ino):
		def _buildprein(pre, ino, current):
			if len(ino) == 0:
				_buildprein.pointer -= 1
				return None
			if len(ino) == 1:
				return BNode(ino[0])

			_buildprein.pointer += 1
			current.set_left(_buildprein(pre, ino[:ino.index(current.get_data())], BNode(pre[_buildprein.pointer])))

			_buildprein.pointer += 1
			current.set_right(_buildprein(pre, ino[ino.index(current.get_data())+1:], BNode(pre[_buildprein.pointer])))

			return current
		_buildprein.pointer = 0
		self.set_root(_buildprein(pre, ino, BNode(pre[0])))
		return self.get_root()

# method build_post_in : builds tree from postorder and inorder traversal list
# parameters :	post - postorder traversal list
#		ino - inorder traversal list
# returns : root node of tree
	def build_post_in(self, post, ino):
		def _buildpostin(post, ino, current):
			if len(ino) == 0:
				_buildpostin.pointer += 1
				return None
			if len(ino) == 1:
				return BNode(ino[-1])

			_buildpostin.pointer -= 1
			current.set_right(_buildpostin(post, ino[ino.index(current.get_data())+1:], BNode(post[_buildpostin.pointer])))

			_buildpostin.pointer -= 1
			current.set_left(_buildpostin(post, ino[:ino.index(current.get_data())], BNode(post[_buildpostin.pointer])))

			return current
		_buildpostin.pointer = len(post) - 1
		self.set_root(_buildpostin(post, ino, BNode(post[-1])))
		return self.get_root()

# method preorder_rec : traverse tree in preorder, recursively 
# parameters for inner method :	root - current root of tree (subtree)
#				result - result list
# returns : preorder traversed list
	def preorder_rec(self):
		def _preorder_rec(root, result):
			if not root:
				return
			result.append(root.get_data())
			_preorder_rec(root.get_left(), result)
			_preorder_rec(root.get_right(), result)
		result = []
		_preorder_rec(self.get_root(), result)
		return result

# method preorder_ite : traverse tree in preorder, iteratively
# parameters :	no parameters
# returns : preorder traversed list
	def preorder_ite(self):
		if not self.get_root():
			return
		result = []
		stack = []
		stack.append(self.get_root())
		while stack:
			node = stack.pop()
			result.append(node.get_data())
			if node.get_right(): stack.append(node.get_right())
			if node.get_left(): stack.append(node.get_left())
		return  result

# method preorder : general method for preorder traversal
# parameters :	no parameters
# returns : preorder traversed list
	def preorder(self):
		return self.preorder_rec()

# method inorder_rec : traverse tree in inorder, recursively 
# parameters for inner method :	root - current root of tree (subtree)
#				result - result list
# returns : inorder traversed list
	def inorder_rec(self):
		def _inorder_rec(root, result):
			if not root:
				return
			_inorder_rec(root.get_left(),result)
			result.append(root.get_data())
			_inorder_rec(root.get_right(),result)
		result = []
		_inorder_rec(self.get_root(), result)
		return result

# method inorder_ite : traverse tree in inorder, iteratively
# parameters :	no parameters
# returns : inorder traversed list
	def inorder_ite(self):
		if not self.get_root():
			return
		result = []
		stack = []
		node = self.get_root()
		while stack or node:
			if node:
				stack.append(node)
				node = node.get_left()
			else:
				node = stack.pop()
				result.append(node.get_data())
				node = node.get_right()
		return result

# method inorder : general method for inorder traversal
# parameters :	no parameters
# returns : inorder traversed list
	def inorder(self):
		return self.inorder_rec()

# method postorder_rec : traverse tree in postorder, recursively 
# parameters for inner method :	root - current root of tree (subtree)
#		result - result list
# returns : postorder traversed list
	def postorder_rec(self):
		def _postorder_rec(root, result):
			if not root:
				return
			_postorder_rec(root.get_left(), result)
			_postorder_rec(root.get_right(), result)
			result.append(root.get_data())
		result = []
		_postorder_rec(self.get_root(), result)
		return result

# method postorder_ite : traverse tree in postorder, iteratively
# parameters :	no parameters
# returns : postorder traversed list
	def postorder_ite(self):
		if not self.get_root():
			return
		result = []
		visited = set()
		stack = []
		node = self.get_root()
		while stack or node:
			if node:
				stack.append(node)
				node = node.left
			else:
				node = stack.pop()
				if node.get_right() and node.get_right() not in visited:
					stack.append(node)
					node = node.get_right()
				else:
					visited.add(node)
					result.append(node.get_data())
					node = None
		return result

# method postorder : general method for postorder traversal
# parameters :	no parameters
# returns : postorder traversed list
	def postorder(self):
		return self.postorder_rec()

# method levelorder : method for level order traversal
# parameters : no parameters
# returns : returns level order traversed list
	def levelorder(self):
		result = []
		queue = Queue()
		queue.enqueue(self.get_root())
		while not queue.is_empty():
			current = queue.dequeue()
			result.append(current)
			if current.get_left() is not None:
				queue.enqueue(current.get_left())
			if current.get_right() is not None:
				queue.enqueue(current.get_right())
		return result

# method bfs : Breadth First Search (BFS)
# parameters : 	element - to search
# returns:	None - if element is absent in tree
#		element - else
	def bfs(self, element):
		result = []
		queue = Queue()
		queue.enqueue(self.get_root())
		while not queue.is_empty():
			current = queue.dequeue()
			if current.get_data() == element:
				return element
			if current.get_left() is not None:
				queue.enqueue(current.get_left())
			if current.get_right() is not None:
				queue.enqueue(current.get_right())				
		return None

# method dfs : Depth First Search (DFS)
# parameters : 	element - to search
# returns:	None - if element is absent in tree
#		element - else
	def dfs(self, element):
		result = []
		stack = Stack()
		stack.push(self.get_root())
		while not stack.is_empty():
			current = stack.pop()
			if current.get_data() == element:
				return element
			if current.get_right() is not None:
				stack.push(current.get_right())
			if current.get_left() is not None:
				stack.push(current.get_left())
		return None

# method find_max : finds maximum element in tree
# parameters : no parameters
# returns : maximum element in this tree
	def find_max(self):
		def _find_max(root):
			if not root:
				return
			if root.get_data() > _find_max.max:
				_find_max.max = root.get_data()
			_find_max(root.get_left())
			_find_max(root.get_right())
			return _find_max.max
		_find_max.max = self.root.get_data()
		return _find_max(self.get_root())

# method find_min : finds minimum element in tree
# parameters : no parameters
# returns : minimum element in this tree
	def find_min(self):
		def _find_min(root):
			if not root:
				return
			if root.get_data() < _find_min.min:
				_find_min.min = root.get_data()
			_find_min(root.get_left())
			_find_min(root.get_right())
			return _find_min.min
		_find_min.min = self.root.get_data()
		return _find_min(self.get_root())

# BST - Binary Search Tree

class BST:

# constructor : initialises Binary Tree
# root : root of Binary Tree
# lst : list of elements 
	def __init__(self, lst):
		self.root = self.build_bst(lst)

# toString : returns as string of sorted (inorder) elements
	def __str__(self):
		return str(self.get_list())

# representation : returns representation with preorder, inorder and postorder traversal
	def __repr__(self):
		return str(self.get_list())

# method get_root : returns root of tree
	def get_root(self):
		return self.root

# method set_root : returns root of tree
	def set_root(self, root):
		self.root = root

# method get_list : gets sorted list of elements in tree
# parameters for inner method : root - root of current sub tree
# returns : list of elements in sorted form
	def get_list(self):
		def make_list(root):
			if root is None: 
				return ""
			return make_list(root.get_left())+" "+str(root.get_data())+" "+make_list(root.get_right())
		return make_list(self.get_root()).split()	
	
# method build_bst : builds bst of a passed list of elements
# parameters : lst - list of elements
# returns : root of constructed bst
	def build_bst(self, lst):
		def _build_bst(lst):
			l = len(lst)
			if l == 0:
				return None
			if l == 1: 
				return BNode(lst[0])
			return BNode(lst[l//2], _build_bst(lst[:(l//2)]), _build_bst(lst[(l//2)+1:]))
		lst = sort(lst)
		self.set_root(_build_bst(lst))
		return self.get_root()

# method insert : inserts element in BinaryTree
# parameter : 	data - data to insert
# returns : nothing
	def insert(self, data):
		def _insert(root):
			if data < root.get_data():
				if root.get_left() is None:
					root.set_left(BNode(data))
				else:
					_insert(root.get_left())
			else:
				if root.get_right() is None:
					root.set_right(BNode(data))
				else:
					_insert(root.get_right())
		if self.get_root() is None:
			self.set_root(BNode(data))
		else:
			_insert(self.get_root())		

# method delete : deletes a node present in BST
# parameters : data - data of node to delete
# returns :    True - if element is deleted
# 	       False - if element is not found
	def delete(self, data):
		def _delete(root):
			if root is None:
				return None
			current = root.get_data()
			if current == data:
				_delete.flag = True
				if (root.get_left() is None) & (root.get_right() is None): # zero child
					return None
				elif root.get_left() is None:	# right child
					return root.get_right()
				elif root.get_right() is None:  # left child
					return root.get_left()
				else:				# two children
					# we will replace it with minimum node in right subtree
					# it will be left most node in right subtree
					prev = root.get_right()
					minnode = root.get_right()
					while minnode.get_left() is not None:
						prev = minnode
						minnode = prev.get_left()
					root.set_data(minnode.get_data())
					prev.set_left(None)
					# return root
			elif data < current:
				root.set_left(_delete(root.get_left()))
			else:	# data > current
				root.set_right(_delete(root.get_right()))
			return root
		_delete.flag = False
		self.set_root(_delete(self.get_root()))
		return _delete.flag

# method search : searches an element using binary search
# parameters : data - element to search
# returns : data - if element is found
#	    None - if element is absent
	def search(self, data):
		root = self.get_root()
		while root is not None:
			current = root.get_data()
			if data == current:
				return data
			elif data < current:
				root = root.get_left()
			else: 	# data > current
				root = root.get_right()
		return None