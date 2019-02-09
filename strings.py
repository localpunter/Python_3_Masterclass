# Use Indexing to return certain characters from a string
string1 = "Alan Rachel Lego"
print(string1)

# Each character must have the variable name as well as the index 'A R L'
print(
    "\nIndex 0:", string1[0],
    "\nIndex 5:", string1[5],
    "\nIndex 12:", string1[12]
)


# This will print 'A [5] [12]'
print("\n", string1[0], [5], [12])


#  print(string1[0, 5, 12]) This will return an error


# The minus sign means we start at the end of the string 'o'
print(
    "\nIndex -1:", string1[-1],
    "\nIndex -6:", string1[-6],
    "\nIndex -13:", string1[-13]
)


print("\nThe length of string1 is:", len(string1), "characters\n")


# This returns '2' as it does not see A the same as a
print(string1.index("a"))

#  This counts how many time the letter 'e' appears
print(string1.count("e"))


# This returns '6' as this is the index where 'ache' starts
print(string1.find("ache"))


b = "      Alan Rachel Lego      "
c = "££££££Alan Rachel Lego££££££"
d = "Alan,Rachel,Lego"
# .strip() removes all white spaces from the start and end of the string.
# .strip(" ") removes the character in between " "
# .replace(" ", "") removes what is before the ','
# and replaces with what comes after the ','. ("find", "replace")
# .split(",") takes ',' as the delimeter and returns a list
# "_".join(d) adds _ between all characters in d
print(
    "\nRemoves all white spaces from the start and end of the string:",
    b.strip())
print("\nRemoves the £ character:", c.strip("£"))
print(
    "\nFinds what is before the ','and replaces with what comes after:",
    b.replace(" ", ""))
print("\nTakes ',' as the delimeter and returns a list", d.split(","))
print("\nAdds '_' between all characters in d", "_".join(d))


# Strings - formatting v1
print("\nCisco model: %s, %d WAN slots, IOS %f" % ("2600XM", 2, 12.4))
print("Cisco model: %s, %d WAN slots, IOS %.f" % ("2600XM", 2, 12.4))
print("Cisco model: %s, %d WAN slots, IOS %.1f" % ("2600XM", 2, 12.4))
print("Cisco model: %s, %d WAN slots, IOS %.2f" % ("2600XM", 2, 12.4))

# Strings - formatting v2
print("Cisco model: {}, {} WAN slots, IOS {}".format("2600XM", 2, 12.4))
print("Cisco model: {0}, {1} WAN slots, IOS {2}".format("2600XM", 2, 12.4))
print("Cisco model: {2}, {0} WAN slots, IOS {1}".format("2600XM", 2, 12.4))

# Strings - slicing
string1 = "O E2 10.110.8.9 [160/5] via 10.119.254.6, 0:01:00, Ethernet2"

string1[5:15]  # slice starting at index 5 up to, but NOT including, index 15;
# so index 14 represents the last element in the slice
string1[5:]  # slice starting at index 5 up to the end of the string
string1[:10]  # slice starting at the beginning of the string up to, but NOT
# including, index 10
string1[:]  # returns the entire string
string1[-1]  # returns the last character in the string
string1[-2]  # returns the second to last character in the string
string1[-9:-1]  # extracts a certain substring using negative indexes
string1[-5:]  # returns the last 5 characters in the string
string1[:-5]  # returns the string minus its last 5 characters
string1[::2]  # adds a third element called step; skips every
# second character of the string
string1[::-1]  # returns string1's elements in reverse order
