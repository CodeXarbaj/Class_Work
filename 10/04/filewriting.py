# program for writing data into the file

# opening file for write operation
filev = open("firstfile.txt", "w")

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

# closing the file
filev.close()