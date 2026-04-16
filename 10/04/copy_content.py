#copy content of one file to another file 
#opening a file in read mode 
source = open("source.txt", "r")
#checking file open or not
if source != None:
    #opening a file in write mode
    destination = open("destination.txt", "w")
    #using read inbuild function to read data from source file
    data = source.read()
    #using write inbuild function to write data in destination file
    destination.write(data)
    print("File copied successfully")
    #closing source and destination file
    source.close()  
    destination.close()
else:
    print("File not opened")