#4. Remove Duplicate Lines
#A file contains repeated lines due to logging errors.
#Create a new file with only unique lines (preserve order).

#   Algorithm
#    Open input file in read mode
#   Open output file in write mode
#    Create empty list seen
#   Read file line by line
#    If line not in seen, write it to output file
#    Add line to seen
#    Close files

# open source file
source = open("input.txt", "r")
# open destination file
destination = open("output.txt", "w")
seen = []
# read line by line using loop 
for line in source:
    if line not in seen:
        destination.write(line)
        seen.append(line)
# close files
source.close()
destination.close()