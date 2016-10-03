import csv
import os
import re
#macros
TYPE = 6
SPLIT = -1
TERMINATE = -2

# get list of files to open
# to use, enter relative path to folder to open

path = raw_input("directory name?")
fullpath = os.path.join(os.getcwd(),path)
directory = os.listdir(fullpath)

#open each file
for filename in  directory:
    # make sure it's a file we want, not a hidden or a directory itself
    path = os.path.join(fullpath, filename)
    if os.path.isdir(path) or filename.startswith('.'):
        continue

    # now, open file
    file = open(path)
    csv_file = csv.reader(file)

    #loop through all rows, even though some don't have the module we want
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
    
    # create filename to write it to
    newfilename = 
    #now that everything is mapped backwards, write it to a CSV!
    with open('parseddata.csv', 'w') as mycsvfile:
        #not sure why I need so many variables here, based it off an example
        writer = csv.writer(mycsvfile)
        for key in sorted(dict):
            writer.writerow([key," "])
            for module in dict[key]:
                writer.writerow([" ",module])