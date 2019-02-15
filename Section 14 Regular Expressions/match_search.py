# Regular Expressions - the "re.match" and "re.search" methods
import re  # importing the regular expressions module
import re

# a = re.match(pattern, string, optional flags) #general match syntax; "a" is called a match object if the pattern is found in the string, otherwise "a" will be None


mystr = "You can learn any programming language, whether it is Python2, python3, Perl, Java, JavaScript or PHP"

a = re.match("You", mystr)
print(a)

print(a.group())

a = re.match("you", mystr, re.I)
print(a)


arp = "22.22.22.1   0       b4:a9:5a:ff:c8:45 VLAN#222       L"

# a = re.search(r"(.+?) +(\d) +(.+?)\s{2,}(\w)*", arp)

# print(a)

# print(a.group(1))

a = re.search(r"(.+) +(\d) +(.+?)\s{2,}(\w)*", arp)

print("Check what this returns:", a.group())
print(a.group(1))
print(a.group(2))
print(a.group(3))
print(a.group(4))
print(a.groups())


mystr = "You can learn any programming language, whether it is Python2, Python3, Perl, Java, javascript or PHP."


# checking if the characters "You" are indeed at the beginning of the string
a = re.match("You", mystr)

a.group()  # result is 'You'; Python returns the match it found in the string according to the pattern we provided

# re.I is a flag that ignores the case of the matched characters
a = re.match("you", mystr, re.I)

# general search syntax; searching for a pattern throughout the entire string; will return a match object if the pattern is found and None if it's not found
# a = re.search(pattern, string, optional flags)

arp = "22.22.22.1      0         b4:a9:5a:ff:c8:45 VLAN#222             L"

a = re.search(r"(.+?) +(\d) +(.+?)\s{2,}(\w)*", arp)  # result is '22.22.22.1'; 'r' means the pattern should be treated like a raw string; any pair of parentheses indicates the start and the end of a group; if a match is found for the pattern inside the parentheses, then the contents of that group can be extracted with the group() method applied to the match object; in regex syntax, a dot represents any character, except a new line character; the plus sign means that the previous expression, which in our case is just a dot, may repeat one or more times; the question mark matching as few characters as possible

a.groups()  # returns all matches found in a given string, in the form of a tuple, where each match is an element of that tuple
('22.22.22.1', '0', 'b4:a9:5a:ff:c8:45 VLAN#222', 'L')
