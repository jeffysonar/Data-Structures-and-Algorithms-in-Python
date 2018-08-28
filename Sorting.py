
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
	def _merge_sort(A, p, r):
		if p < r:
			q = (p + r) // 2
			_merge_sort(A, p, q)
			_merge_sort(A, q + 1, r)
			merge(A, p, q, r)
	def merge(A, p, q, r):
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
	_merge_sort(A, 0, len(A) - 1)
	return A

def quick_sort(A, ascending=True):
	compare = compare_func(ascending)
	def _quick_sort(A, p ,r):
		if p < r:
			q = partition(A, p, r)
			_quick_sort(A, p, q-1)
			_quick_sort(A, q+1, r)
	def partition(A, p, r):
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
	_quick_sort(A, 0, len(A)-1)
	return A

print(bubble_sort([4,3,2,1,0,8,5,7,6,9], False))