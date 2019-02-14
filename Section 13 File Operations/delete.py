f = open("text.txt")

print(f.read())
print("This will return 0 as we haven't returned the cursor back to the start:", len(f.read()))
f.seek(0)
print("This will work as f.seek returns the cursor back to the value in ():", len(f.read()))
f.close()

f = open("text.txt", "r+")
print(f.truncate(10))
print("This will return the number of characters in the file:", len(f.read()))
f.close()