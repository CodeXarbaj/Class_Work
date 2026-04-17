#algorithm
#Open both files in read mode
#Open output file
#Read lines from both files
#Merge lines
#Add line number while writing
#Close files
#End

with open("file1.txt", "r") as f1:
    with open("file2.txt", "r") as f2:
        with open("merge.txt", "w") as out:

            lines = f1.readlines() + f2.readlines()

            count = 1
            for line in lines:
                out.write(str(count) + ". " + line)
                count += 1