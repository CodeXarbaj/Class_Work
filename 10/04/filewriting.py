
with open("demo.txt", "w") as f:
    lines = []
    
    for i in range(5):
        sentence = input(f"Enter sentence {i+1}: ")
        lines.append(sentence + "\n")
    
    f.writelines(lines)

print("Done!")
f.close()
