#algorithm
#Open both files in read mode
#Open output file
#Read lines from both files
#Merge lines
#Add line number while writing
#Close files
#End

f1 = open("file1.txt", "r")
f2 = open("file2.txt", "r")
out = open("merge.txt", "w")

lines = f1.readlines() + f2.readlines()

count = 1
for line in lines:
    out.write(str(count) + ". " + line)
    count += 1

f1.close()
f2.close()
out.close()