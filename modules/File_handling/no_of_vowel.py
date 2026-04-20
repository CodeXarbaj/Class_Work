# open the file in read mode
filev = open("firstfile.txt", "r")
if filev:
    # read complete file data
    data = filev.read()
    # variable to store vowel in file
    count = 0
    # check every character in file using loop
    for ch in data:
        if ch in "aeiou":
            count = count + 1
    # print total vowels in file
    print("Number of vowels in file :", count)
    # close the file
    filev.close()
else:
    print("Unable to open the file")
