# initialize array of random order for numbers
# obviously, very unefficient, but for just 1 - 10, seems okay

first = [5, 8, 2, 9, 1, 3, 4, 0, 6, 8, 7]
second = [ 7, 5, 9, 2, 4, 6, 1, 8, 0, 3]
for number in first:
	for multiplier in second:
		print "What is %d X %d" % (number, multiplier)
		print "answer is: %s" % (number * multiplier)