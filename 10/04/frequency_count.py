#3. Word Frequency Counter
#Given a file article.txt,
#Count frequency of each word (ignore case and punctuation).

#   Open article.txt in read mode
#   Read file content, text = file.read()
#   Convert text to lowercase
#   Remove punctuation
#   Split text into words using split()
#   Create empty dictionary
#   Count frequency of each word
#   Print word and its frequency
#   Close file





# open file
file = open("article.txt", "r")

# read content
text = file.read()

# convert to lowercase
text = text.lower()

# remove punctuation manually
clean_text = ""
for ch in text:
    if ch.isalnum() or ch.isspace():
        clean_text += ch

# split into words
words = clean_text.split()

# count frequency
freq = {}

for word in words:
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1

# print result
for word in freq:
    print(word, ":", freq[word])

# close file
file.close()




