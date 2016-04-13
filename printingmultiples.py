from num2words import num2words

# initialize array of random order for numbers
# obviously, very unefficient, but for just 1 - 10, seems okay
first = [5, 8, 2, 9, 1, 3, 4, 0, 6, 8, 7]
second = [ 7, 5, 9, 2, 4, 6, 1, 8, 0, 3]

#initialize json
print "["
for number in first:
	for multiplier in second:
		print ' {'
		print '	"Question" : "What is %d X %d?",' % (number, multiplier)
		print '	"Spoken Question" : "What is %s times %s?", ' % (num2words(number), num2words(multiplier))
		print '	"Answer" : %d,' %(number * multiplier)
		print '	"Spoken Answer" : "The correct answer is %s."' %(num2words(number * multiplier))
		print ' },'
		print ""
print "]"