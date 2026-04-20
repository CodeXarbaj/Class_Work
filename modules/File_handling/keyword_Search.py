#8. Keyword Search Tool
#Ask user for a keyword and return all lines from file containing that keyword.
#algorithm
#Open file
#Take keyword input
#Read file line by line
#Check if keyword in line
#Print matching lines
#Close file
#End

f = open("data.txt", "r")

keyword = input("Enter keyword: ")

for line in f:
    if keyword in line:
        print(line)

f.close()
