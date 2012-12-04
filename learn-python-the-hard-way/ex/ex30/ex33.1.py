def increase(base, i):
	return base + i

def func_test(N):
	""" this is a test function"""
	i = 0
	numbers = []
	while i < N:
		print "At the top i is %d" % i
		numbers.append(i)
		i = increase(i, 1)
		print "Numbers now:", numbers
		print "At the bottom i is %d" % i

		print "The numbers:"

	for num in numbers:
		print num


func_test(7)
