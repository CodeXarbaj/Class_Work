# copy content of one file to another file 
# opening a file in read mode using with
with open("source.txt", "r") as source:
    # checking file open or not
    if source != None:
        # opening a file in write mode using with
        with open("destination.txt", "w") as destination:
            # using read inbuilt function to read data from source file
            data = source.read()
            # using write inbuilt function to write data in destination file
            destination.write(data)
            print("File copied successfully")
    else:
        print("File not opened")