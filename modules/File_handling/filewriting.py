#algorithm
#Start
#Open file in write mode
#Create empty list
#Take 5 sentences as input
#Store sentences in list
#Write list into file
#Print success message
#End

# program for writing data into the file

# opening file for write operation
with open("firstfile.txt", "w") as filev:

    # blank list of sentences
    sentences = []

    # writing five sentences into the file
    print("Enter any five sentence : ")

    for x in range(5):
        # input of data from user
        sentence = input()
        
        # inserting the sentence into the list
        sentences.append(sentence)
        
        print("-----------------------------")

    # writing data into the file
    filev.writelines(sentences)

    print("Data Successfully written")
