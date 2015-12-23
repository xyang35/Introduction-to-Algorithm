# Sample codes for Insertion sort
from random import randint

def Insertion_sort(A):
	# Input: A is a list of numbers
	# Output: sorted list A (ascending order)
	
	for i in range(1, len(A)):
		key = A[i]
		j = i-1
		while j>=0 and A[j]>key:
			A[j+1] = A[j]
			j -= 1
		A[j+1] = key

def main():
	
	# Initialization
	A = []
	print "Original A:"
	for i in range(10):
		A.append(randint(1,10))
		print str(A[-1])+' ',
	print "\n"

	Insertion_sort(A)
	
	print "Sorted A:"
	for i in range(len(A)):
		print str(A[i])+' ',
	print "\n"


if __name__ == "__main__":
	main()
