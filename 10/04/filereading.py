#to open file for read operation
filev = open("firstfile.txt", "r")
if(filev):
    #to real data from file
    data = filev.read()
    print(data)
    print("----------------------------")
    print("No of char :", len(data))
    #closing file
    filev.close()
else:
    print("unable to open file")