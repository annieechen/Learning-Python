from num2words import num2words
import random 

# initialize array of random order for numbers
# obviously, very unefficient, but for just 1 - 10, seems okay
first = [5, 8, 2, 9, 1, 3, 4, 0, 6, 8, 7]
second = [ 7, 5, 9, 2, 4, 6, 1, 8, 0, 3]

#initialize json
print "["
for number in first:
	for multiplier in second:
		third  = random.randint(0,9)
		print ' {'
		print '	"Question" : "What is %d + %d X %d?",' % (third, number, multiplier)
		print '	"Spoken Question" : "What is %s plus %s times %s?", ' % (num2words(third), num2words(number), num2words(multiplier))
		print '	"Answer" : %d,' % (third + (number * multiplier))
		print '	"Spoken Answer" : "The correct answer is %s."' %(third + (number * multiplier))
		print ' "Difficulty Level" : 1,'
		print '	"Max Time" : 60,'
		print ' "Most Common Mistake" : %d' % ((third + number ) * multiplier)
		print ' },'
		print ""
print "]"