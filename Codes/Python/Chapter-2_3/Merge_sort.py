# Sample codes for Insertion sort
from random import randint

def merge(A, left, right, middle):
	s_left = A[left:middle]
	s_right = A[middle:right]
	s_left.append('a')    # place on the bottome a sentinel element, as all numbers are smaller than 'a'
	s_right.append('a')

	i = 0
	j = 0
	for k in range(left, right):
		if s_left[i] < s_right[j]:
			A[k] = s_left[i]
			i += 1
		else:
			A[k] = s_right[j]
			j += 1


def Merge_sort(A, left, right):
	# Input: A is a list of numbers, left and right are integer indicating postion
	# Output: sorted list A (ascending order)

	if left < right-1:
		middle = (left+right) / 2
		Merge_sort(A, left, middle)
		Merge_sort(A, middle, right)
		merge(A, left, right, middle)

def main():
	
	# Initialization
	A = []
	print "Original A:"
	for i in range(10):
		A.append(randint(1,10))
		print str(A[-1])+' ',
	print "\n"

	Merge_sort(A, 0, len(A))
	
	print "Sorted A:"
	for i in range(len(A)):
		print str(A[i])+' ',
	print "\n"


if __name__ == "__main__":
	main()
