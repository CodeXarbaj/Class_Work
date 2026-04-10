# program for writing data into the file
# opening file for write operation
filev = open("firstfile.txt", "w")
# create a black list
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
# closing the file
filev.close()