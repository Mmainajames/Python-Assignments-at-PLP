
# Step 1: Create input.txt with your message (if it doesn't exist yet)
with open("input.txt", "w") as infile:
    infile.write("Python programming is cheap but there is a catch, ")

# Step 2: Read from input.txt
with open("input.txt", "r") as infile:
    content = infile.read()

# Step 3: Modify the content by appending the new text
modification = " consistency is the key to becoming a great Python Developer"
modified_content = content + modification

# Step 4: Write the modified content to output.txt
with open("output.txt", "w") as outfile:
    outfile.write(modified_content)

print("Modification complete! Check output.txt for results.")
