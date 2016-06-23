import csv

#open file?
file = open('data.csv')
csv_file = csv.reader(file)

#loop through all rows, even though some don't have the module we want

#my file is organized as 
#unit, module, assignment (if there), name, CSP Objectives

for row in csv_file:
    #if the row is a title row, with unit module and asg:
    if row[0]:
        # create a string that's combining unit number with module number with name 
        name = "%s-%s: %s" % (row[0], row[1], row[3])
        # if is an assignment
        if row[2]:
            name = "%s-%sA: %s" % (row[0], row[1], row[3])
    print name
    
    