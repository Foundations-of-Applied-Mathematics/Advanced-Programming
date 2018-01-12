def print_vals(N=40):
	"""Print values between 1 and N inclusive"""
	for i in N:
		print(i)


def determine_divisibility(a=4,b=7,c=11):
	"""Determine if the sum of a and b is divisible by c"""
	if a + b % c == 0:
		return True
	else:
		return False


def get_front(data):
	"""Return the data with its first element removed"""
	if len(data) == 0:
		raise ValueError("Invalid length of data, input required")
	return data.pop(0)


def power_of_two(x):
	"""determine if x is a power of 2"""
	while x%2 == 0:
		if x == 1:
			return True
	return False


def power_of_two(x):
	"""determine if x is a power of 2"""
	while x%2 == 0:
		x /= 2
		if x == 1:
			return True
	return False
