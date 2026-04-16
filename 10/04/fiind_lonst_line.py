#9. Find Longest Line
#Identify the longest line in a file and print its length and content.
#algorithm
#Open file
#Initialize empty string
#Read line by line
#Compare length
#Store longest line
#Print result
##End
f = open("data.txt", "r")

longest = ""

for line in f:
    if len(line) > len(longest):
        longest = line

print("Longest Line:", longest)
print("Length:", len(longest))

f.close()
🧠 Short Algo
