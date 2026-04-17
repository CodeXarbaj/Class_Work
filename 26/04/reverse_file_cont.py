#7. Reverse File Content
#Read a file and write its content in reverse order (line-wise) into another file.
#algorithm
#Open input file
#Open output file
#Read all lines
#Reverse lines
#Write to new file
#Close files
#End
f = open("input.txt", "r")
out = open("reverse.txt", "w")

lines = f.readlines()

for line in reversed(lines):
    out.write(line)

f.close()
out.close()