#3. Word Frequency Counter
#Given a file article.txt,
#Count frequency of each word (ignore case and punctuation).

#algorithm
#Start
#Open article.txt in read mode
#Read file content
#Convert text to lowercase
#Remove punctuation
#Split text into words
#Create empty dictionary
#Count frequency of each word
#Print word and frequency
#End

# open file
with open("article.txt", "r") as file:

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
