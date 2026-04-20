#a file with name student.txt contains record in the format name,mark,city acstract and save only the student data who marks is greater than 75 into a new file

#algorithm
#   1-open a file name student.txt in read mode & check, is file empty
#   2-open another file new_student.txt in write mode
#   3-Using readline to read all the lines in source file and store data in content variable
#   4-for line in content:
#   5-remove extra space and newline using strip()
#   6-now split all the data using strip() function ny using ,
#   7-using if and copy data 
#   8- if len(data) == 3:
#           name = data[0]
#          marks = int(data[1])
#           city = data[2]
#   9- using condition and write data in destination file
#   10-   if marks > 75:
#          destination.write(line + "\n")

#   11- Close source and destination file
# open source file
source = open("student.txt", "r")
# check if file is empty 
if source:
    destination = open("new_student.txt", "w")
    # read all line using 
    content = source.readlines()
    for line in content:
        # remove extra spaces and newline
        line = line.strip()
           # split data using "," like name, marks, ciry
        data = line.split(",")    
        # check valid format means here should be 3 data in format name mark city  
        if len(data) == 3:
            name = data[0]
            marks = int(data[1])
            city = data[2]
            
            # condition marks > 75
            if marks > 75:
                destination.write(line + "\n")
    
    source.close()
    destination.close()
    