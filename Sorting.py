
# method sort_swap : swaps elements at x and y index of list A
def sort_swap(A,x,y):

	temp = A[x]

	A[x] = A[y]

	A[y] = temp



# compare_func : returns comparing function depending upon ascending parameter
def compare_func(ascending):

	return (lambda curr, x : (curr < x)) if ascending is True else (lambda curr, x : (curr > x))

# method linear_sort : sorts given list using linear sort
# parameters : 	A - input list
#		ascending - True if sorting is ascending, else False
# returns : sorted array


def linear_sort(A, ascending=True):

	compare = compare_func(ascending)

	for i in range(len(A) - 1):

		for j in range(i+1, len(A)):

			if compare(A[j], A[i]):

				sort_swap(A, i, j)

	return A


# method bubble_sort : sorts given list using bubble sort
# parameters : 	A - input list
#		ascending - True if sorting is ascending, else False
# returns : sorted array


def bubble_sort(A, ascending=True):

	compare = compare_func(ascending)

	for i in range(1, len(A)):
		print(A[:len(A) - i])
		for j in range(len(A) - i):
			if compare(A[j+1], A[j]):

				sort_swap(A, j, j+1)

	return A



# method selection_sort : sorts given list using selection sort
# parameters : 	A - input list
#		ascending - True if sorting is ascending, else False
# returns : sorted array
def selection_sort(A, ascending=True):

	compare = compare_func(ascending)

	for i in range(len(A)):

		least = i

		for j in range(i+1, len(A)):

			if compare(A[j], A[least]) is True:

				least = j

		sort_swap(A, least, i)


	return A

# method insertion_sort : sorts given list using insertion sort
# parameters : 	A - input list
#		ascending - True if sorting is ascending, else False
# returns : sorted array


def insertion_sort(A, ascending=True):

	compare = compare_func(ascending)

	for i in range(1, len(A)):

		j = i - 1

		x = A[i]

		while compare(x, A[j]) and j >= 0:

			A[j+1] = A[j]

			j -= 1

		A[j+1] = x

	return A

























# method merge_sort : sorts given list using merge sort
# parameters : 	A - input list
#		ascending - True if sorting is ascending, else False
# returns : sorted array
def merge_sort(A, ascending=True):
	compare = compare_func(ascending)
	def _merge_sort(p, r):
		if p < r:
			q = (p + r) // 2
			_merge_sort(p, q)
			_merge_sort(q + 1, r)
			merge(p, q, r)
	def merge(p, q, r):
		L = A[p:(q+1)] + [float("infinity")]
		R = A[q+1:r+1] + [float("infinity")]
		i = j = 0
		for k in range(p, r+1):
			if compare(L[i], R[j]):
				A[k] = L[i]
				i += 1
			else:
				A[k] = R[j]
				j += 1
	_merge_sort(0, len(A) - 1)
	return A

# method quick_sort : sorts given list using quick sort
# parameters : 	A - input list
#		ascending - True if sorting is ascending, else False
# returns : sorted array
def quick_sort(A, ascending=True):
	compare = compare_func(ascending)
	def _quick_sort(p ,r):
		if p < r:
			q = partition(p, r)
			_quick_sort(p, q-1)
			_quick_sort(q+1, r)
	def partition(p, r):
		pivot = A[r]
		i = p
		j = p
		while j < r:
			if compare(A[j], pivot):
				sort_swap(A, i, j)
				i += 1
			j += 1
		sort_swap(A, i, r)
		return i 
	_quick_sort(0, len(A)-1)
	return A

# method heap_sort : sorts given list using heap sort
# parameters : 	A - input list
#		ascending - True if sorting is ascending, else False
# returns : sorted array
def heap_sort(A, ascending=True):
	from Heap import BinaryHeap
	h = BinaryHeap(A, not ascending)
	for i in range(len(A)):
		A[i] = h.extract_root()
	return A

# method tree_sort : sorts given list using tree sort
# parameters : 	A - input list
#		ascending - True if sorting is ascending, else False
# returns : sorted array
def tree_sort(A, ascending=True):
	from Tree import BST
	def traverse(root):
		if not root:
			return
		traverse(get_left(root))
		A[traverse.point] = root.get_data()
		traverse.point += 1
		traverse(get_right(root))
	t = BST()
	for i in range(len(A)):
		t.insert(A[i])
	if ascending:
		get_left = lambda root: root.get_left()
		get_right = lambda root: root.get_right()
	else:
		get_left = lambda root: root.get_right()
		get_right = lambda root: root.get_left()
	traverse.point = 0
	traverse(t.root)
	return A	

# method tim_sort : sorts given list using tim sort
# parameters : 	A - input list
#		ascending - True if sorting is ascending, else False
# returns : sorted array
def tim_sort(A, ascending=True):
	run = 32
	compare = compare_func(ascending)
	def _tim(p, r):
		if (r - p) > run:
			q = (p + r) // 2
			_tim(p, q)
			_tim(q+1, r)
			A[p:q+1] = insertion_sort(A[p:q+1], ascending)
			A[q+1:r+1] = insertion_sort(A[q+1:r+1], ascending)
			merge(p, q, r)
		else:
			A[p:r+1] = insertion_sort(A[p:r+1], ascending)
	def merge(p, q, r):
		L = A[p:(q+1)] + [float("infinity")]
		R = A[q+1:r+1] + [float("infinity")]
		i = j = 0
		for k in range(p, r+1):
			if compare(L[i], R[j]):
				A[k] = L[i]
				i += 1
			else:
				A[k] = R[j]
				j += 1
	_tim(0, len(A) - 1)
	return A