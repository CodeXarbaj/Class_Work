#5. Email Extractor
#From a file data.txt,
#Extract all valid email addresses and save them into emails.txt.
#algorithm
#Start
#Open data.txt in read mode
#Open emails.txt in write mode
#Read the content of file
#Split content into words
#For each word, check if it contains @ and .
#If yes, write it into emails.txt

# open source and destination file using with
with open("data.txt", "r") as source:
    with open("emails.txt", "w") as destination:

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