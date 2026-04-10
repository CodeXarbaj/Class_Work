# Open file in write mode
with open("demo.txt", "w") as f:
    
    # Loop to take 5 sentences
    for i in range(5):
        sentence = input(f"Enter sentence {i+1}: ")
        
        # Write each sentence with new line
        f.write(sentence + "\n")

print("5 sentences successfully written to file!")
#closing the file
f.close()