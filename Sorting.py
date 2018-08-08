
# method sort_swap : swaps elements at x and y index of list A
def sort_swap(A,x,y):

    temp = A[x]

    A[x] = A[y]

    A[y] = temp



# compare_func : returns comparing function depending upon ascending parameter
def compare_func(ascending):

    return lambda curr, x : (curr < x) if ascending is True else (curr > x)

# method bubble_sort : sorts given list using bubble sort
# parameters : 	A - input list
#		ascending - True if sorting is ascending, else False
# returns : sorted array


def bubble_sort(A, ascending=True):

    compare = compare_func(ascending)

    for i in range(len(A) - 1):

        for j in range(i+1, len(A)):

            if compare(A[j], A[i]):

                sort_swap(A, i, j)

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























