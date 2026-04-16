#4. Remove Duplicate Lines
#A file contains repeated lines due to logging errors.
#Create a new file with only unique lines (preserve order).
# open source file
source = open("data.txt", "r")

# open destination file
destination = open("emails.txt", "w")

# read content
text = source.read()

# split words
words = text.split()

for word in words:
    # simple check for email
    if "@" in word and "." in word:
        # clean common punctuation
        word = word.strip(",.!?()[]{}")
        destination.write(word + "\n")

# close files
source.close()
destination.close()