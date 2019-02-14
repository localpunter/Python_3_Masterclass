# Files - opening and reading a file

myfile = open("routers.txt", "r")

# print(".mode returns the mode the file is in:", myfile.mode)
# print(myfile.read())


# myfile.seek(0)
# print(myfile.read(5))

# print(myfile.readline())
# print(myfile.readlines())

myfile.seek(0)

# def begins_with_A():
for line in myfile.readlines():
    if line.startswith("A"):
        print(line)


myfile = open("routers2.txt", "x")

# "r" is the file access mode for reading and it is the default mode when opening a file
myfile = open("routers.txt", "r")

myfile.mode  # checking the mode in which a file has been opened

myfile.read()  # method that returns the entire content of a file in the form of a string

myfile.read(5)  # returning only the first 5 characters (bytes) in the file

myfile.seek(0)  # moving the cursor at the beginning of the file

myfile.tell()  # checking the current position of the cursor inside the file

# returns the file content one line at a time, each time you use the method
myfile.readline()

myfile.readlines()  # returns a list where each element is a line in the file
