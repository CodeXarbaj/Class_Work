#algorithm
#Start
#Open file in read mode
#Check file opened or not
#Read data from file
#Print data
#Print number of characters
#End

# to open file for read operation
with open("firstfile.txt", "r") as filev:
    if(filev):
        # to real data from file
        data = filev.read()
        print(data)
        print("----------------------------")
        print("No of char :", len(data))
    else:
        print("unable to open file")