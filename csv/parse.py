import csv

#open file?
file = open('data.csv')
csv_file = csv.reader(file)

#loop through all rows, even though some don't have the module we want

#my file is organized as 
#unit, module, assignment (if there), name, CSP Objectives
dict = {}

for row in csv_file:
    #if the row is a title row, with unit module and asg:
    if row[0]:
        # create a string that's combining unit number with module number with name 
        name = "%s-%s: %s" % (row[0], row[1], row[3])
        # if is an assignment
        if row[2]:
            name = "%s-%sA: %s" % (row[0], row[1], row[3])
    #make sure whole row isn't just spacing
    if row[4]:
        #make sure row is a valid learning objectie number
        if row[4][3].isdigit(): 
            LO = row[4][3:9]
            #if this learning objective has already been added
            if LO in dict:
                #append current module to that last
                dict[LO].append(name)
            #otherwise, add this learning objective to the dictionary
            else:
                dict[LO] = [name]
    
#now that everything is mapped backwards, write it to a CSV!
with open('parseddata.csv', 'w') as mycsvfile:
    #not sure why I need so many variables here, based it off an example
    writer = csv.writer(mycsvfile)
    for key in sorted(dict):
        writer.writerow([key," "])
        for module in dict[key]:
            writer.writerow([" ",module])