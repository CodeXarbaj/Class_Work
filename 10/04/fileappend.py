#algorithm
#Start
#Open file in append mode
#Repeat 3 times
#Take sentence input from user
#Write sentence into file with newline
#Print success message
#End

# Open the file in append mode 
with open("demo.txt", "a") as f:
    # Loop to take input 3 times from user
    for i in range(3):
    
        # Take sentence input from user
        sentence = input(f"Enter sentence {i+1}: ")
        
        # Write the sentence into file with a new line
        f.write(sentence + "\n")

# Print message after writing is done
print("Data successfully appended to file!")
#closing the file 