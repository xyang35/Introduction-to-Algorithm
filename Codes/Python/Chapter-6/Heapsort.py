# Sample codes for Heapsort algorithm
# Heap data structure is implemented as an array

from random import randint
import pdb

heap_size = 0

# for heap structure
def parent(idx):
	return (idx-1)/2

def left(idx):
	return 2*idx+1

def right(idx):
	return 2*idx+2

def MAX_HEAPIFY(A, i):
    # To maintain the max_heap property

	global heap_size
	l = left(i)
	r = right(i)
	if l < heap_size and A[l]>A[i]:
		largest = l
	else:
		largest = i
	
	if r < heap_size and A[r]>A[largest]:
		largest = r
	
	if not largest == i:
		temp = A[i]
		A[i] = A[largest]
		A[largest] = temp
		MAX_HEAPIFY(A, largest)    # call this function recursively

def BUILD_MAX_HEAP(A):
	# to build a max_heap
	global heap_size
	heap_size = len(A)
	for i in range(len(A)/2, 0, -1):
		MAX_HEAPIFY(A, i-1)

def Heapsort(A):
	# Input: A is a list of numbers
	# Output: sorted list of numbers

	global heap_size
	BUILD_MAX_HEAP(A)
	for i in range(len(A),1,-1):
		# exchange the last element to be the largest element
		temp = A[i-1]
		A[i-1] = A[0]
		A[0] = temp

		heap_size -= 1
		MAX_HEAPIFY(A, 0)

def main():
	
	# Initialization
	A = []
	print "Original A:"
	for i in range(10):
		A.append(randint(1,10))
		print str(A[-1])+' ',
	print "\n"
	
	Heapsort(A)
	
	print "Sorted A:"
	for i in range(len(A)):
		print str(A[i])+' ',
	print "\n"


if __name__ == "__main__":
	main()
