#algorithm
#Start
#Open file in write mode
#Create empty list
#Take 20 sentences as input
#Store each sentence with newline
#Write all sentences to file
#Print success message
#End

# program for writing data into the file
# opening file for write operation
with open("firstfile.txt", "w") as filev:

    # create a blank list
    sentences = []

    # writing 20 sentences into file
    print("Enter any 20 sentences =  ")
    for x in range(20):
        # input of data from user
        sentence = input()
        # inserting sentences
        sentences.append(sentence + "\n")
        print("------------------------------------------------")

    # writing data into the file
    filev.writelines(sentences)
    print("Data inseted compeltely")