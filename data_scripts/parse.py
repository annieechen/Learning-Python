import csv
import os
import re
#macros
TYPE = 5
SPLIT = "-1"
TERMINATE = "-2"

# create a dict to refer to numbers from keys
mapping = {
    'HINT 1': "1",
    'HINT 2': "2",
    'HINT 3': "3",
    'INCORRECT': "4",
    'CORRECT': "5",
    'LAST INCORRECT': "6",
}

# get list of files to open
# to use, enter relative path to folder to open

path = raw_input("directory name?")
fullpath = os.path.join(os.getcwd(),path)
directory = os.listdir(fullpath)

# create a new folder for the sequences
folderpath = os.path.join(fullpath, "sequences")
os.makedirs(folderpath)
#open each file
for filename in  directory:
    # make sure it's a file we want, not a hidden or a directory itself
    path = os.path.join(fullpath, filename)
    print path
    if os.path.isdir(path) or filename.startswith('.'):
        print "skipping" + filename
        continue

    # now, open to read file
    file = open(path)
    csv_file = csv.reader(file)

    # create filename to write it to
    newfilename = re.sub('\.txt$', '_seq.txt', filename)
    print newfilename + "that was new file"
    # write our sequences to a regular file
    output = open(os.path.join(folderpath, newfilename), 'w') 

    curr_list = []
    for row in csv_file:
        # if it's a value we care about
        if row[TYPE] in mapping:
            if row[TYPE] == "CORRECT" or row[TYPE] == "LAST INCORRECT":
                # last in this line, write to file and clear
                curr_list.append(mapping[row[TYPE]])
                curr_list.append(SPLIT)
                curr_list.append(TERMINATE)
                s = ' '.join(curr_list)
                output.write(s + '\n')
                curr_list[:] = []
            else:
                # just add the type to list
                curr_list.append(mapping[row[TYPE]])
                curr_list.append(SPLIT)
        elif row[TYPE] == "END":
            break
    file.close()
    output.close()