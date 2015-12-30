# Sample codes for Maximum subarray problem using divide-and-conquer algorithm

from random import randint

def mid_cross(A, left, right, mid):
	left_max = -float('inf')
	left_sum = 0
	left_point = mid
	i = mid - 1
	while i >= left:
		left_sum += A[i]
		if left_sum > left_max:
			left_max = left_sum
			left_point = i
		i -= 1
	
	right_max = -float('inf')
	right_sum = 0
	right_point = mid
	i = mid 
	while i < right:
		right_sum += A[i]
		if right_sum > right_max:
			right_max = right_sum
			right_point = i+1
		i += 1
	
	return (left_max+right_max, left_point, right_point)


def Maximum_subarray(A, left, right):
	# Input: A is a list of numbers, left and right are integer indicating postion
	# Output: tuple of (max subarray value, left point, right point)

	if left == right-1:
		return (A[left], left, right)
	else:
		mid = (left+right) / 2
		(left_max, left_left, left_right) = Maximum_subarray(A, left, mid)
		(right_max, right_left, right_right) = Maximum_subarray(A, mid, right)
		(mid_max, mid_left, mid_right) = mid_cross(A, left, right, mid)

		if left_max >= right_max and left_max >= mid_max:
			return (left_max, left_left, left_right)
		elif right_max >= left_max and right_max >= mid_max:
			return (right_max, right_left, right_right)
		else:
			return (mid_max, mid_left, mid_right)

def main():
	
	# Initialization
	A = []
	print "Array A:"
	for i in range(10):
		A.append(randint(-10,10))
		print str(A[-1])+' ',
	print "\n"

	(max_value, left, right) = Maximum_subarray(A, 0, len(A))
	
	print "Maximum subarray value: %d" % max_value
	print "The subarray is: ",
	for i in range(left, right):
		print str(A[i])+' ',
	print "\n"


if __name__ == "__main__":
	main()
