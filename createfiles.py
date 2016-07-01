#for sys.exit
import sys

#get question year
year = raw_input("Enter year as xxxx: ")
#quiz number
quiznum = raw_input("Enter quiznum as 0, 1 , or 2: ")
#get max number of files to be made
lastquestion = int(raw_input("How many questions in the quiz? Starting from 0: "))
#get confirmation from user
print("Year = %s, Quiznum = %s, Last Question = %d") % (year,quiznum,lastquestion)

# raw_input returns the empty string for "enter"
yes = set(['yes','y', 'ye', ''])
no = set(['no','n'])
choice = raw_input("Do you want to continue with creating the files? ").lower()
if choice in no:
	print("restart this program you dummy")
	sys.exit()

#now we can start making the files!
for question in range(0, lastquestion + 1):
	#create the question title
	title = year+"_"+quiznum+"_"+str(question)+".yaml"
	
	#create file with title, copy template.yaml into it
	#no error checking, eeks! Don't feed bad input
	with open(title, "w+") as f1:
	    for line in open('template.yaml'):
	    	if "original_exam:" in line:
          		f1.write("original_exam: "+ year+" Quiz "+quiznum + "\n")
          	elif "original_question:" in line:
          		f1.write("original_question: " + str(question) + "\n")
          	elif "authorship_year:" in line:
          		f1.write("authorship_year: " + year + "\n")
	        else:
	        	f1.write(line)
	f1.close()
