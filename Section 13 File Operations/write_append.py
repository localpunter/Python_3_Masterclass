# Files - writing and appending to a file

newfile = open("newfile.txt", "w")

newfile.write("I like Python!\nDo you?")
newfile.close()

newfile = open("newfile.txt", "w")
newfile.write("\nThis is a great day for science!")
newfile.close()

newfile = open("newfile.txt", "w")
newfile.writelines(["Alan ", "Rachel ", "Jack"])
newfile.close()

newfile = open("newfile.txt", "a")
newfile.write("\nThis string was appended!")
newfile.close()

newfile = open("newfile.txt", "w+")
newfile.write("\nThis is another string!")
newfile.close()

# print(newfile.closed)

with open("newfile.txt", "w") as f:
    f.write("Hello Python!!!")

print(f.closed)

# opens/creates a new file for writing; the "w" method also creates the file for writing if the file doesn’t exist and overrides the file if the file already exists; remember to close the file after writing to it to save the changes!
newfile = open("newfile.txt", "w")

# this method takes a sequence of strings as an argument and writes those strings to the file
newfile.writelines(["Cisco", "Juniper", "HP", "\n"])

newfile = open("newfile.txt", "a")  # opening a file for appending

# opens a file for both writing and reading at the same time
newfile = open("newfile.txt", "w+")

# opens for exclusive creation, failing if the file already exists
newfile = open("newfile.txt", "x")

# Files - closing a file
newfile.closed  # checking if a file is closed

newfile.close()  # closing a file

# using the with-as solution, the files gets closed automatically, without needing the close() method
with open("python.txt", "w") as f:
    f.write("Hello Python!\n")
