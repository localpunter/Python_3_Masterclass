# If / Elif / Else conditionals - executing code based on one or more
# conditions being evaluated as True or False; the "elif" and "else"
# clauses are optional

x = 5

if x > 5:
    print("x is greater than 5")
    print(x * 2)
elif x == 5:
    print("x is equal to 5")
else:
    print("x is NOT greater than 5")

y = 10

if y == 5 and type(y) is int:
    print("y equals 5 and is an integer.")
    print(y)
elif y == 10 and type(y) is int:
    print("y is an integer but is not equal to 5")

x = 5

if x > 5:  # if the "x > 5" expression is evaluated as True, the code indented
    # under the "if" clause gets executed, otherwise the execution jumps to the
    # "elif" clause...
    print("x is greater than 5")
elif x == 5:  # ...if the "x == 5" expression is evaluated as True, the code
    # indented under the "elif" clause gets executed, otherwise the execution
    # jumps to the "else" clause
    print("x IS 5\n")
else:  # this covers all situations not covered by the "if" and "elif" clauses;
    # the "else" clause, if present, is always the last clause in the code
    # block
    print("x is NOT greater than 5")

# result of the above "if" block
# x IS 5


# For / For Else loops - executes a block of code a number of times,
# depending on the sequence it iterates on; the "else" clause is optional

# people = ["Alan", "Rachel", "Lego", "Chip"]

# for person in people:
#     print(person)


# my_string = "Rachel"

# for letter in my_string:
#     print(letter)
#     print(letter * 2)
#     print(letter * 3)
#     print(letter * 4)


# r = range(10)

# for i in r:
#     print(i * 2)


people = ["Alan", "Rachel", "Lego", "Chip"]
print(len(people))

print(people)
print(list(range(4)))

for element_index in range(len(people)):
    print(people[element_index])


for index, element in enumerate(people):
    print(index, element)


for person in people:
    print(person)
else:
    print("We have reached the end of the list!\n")

# vendors = ["Cisco", "HP", "Nortel", "Avaya", "Juniper"]

# for element in vendors:   # interating over a sequence and executing the code
# indented under the "for" clause for each element in the sequence
#     print(element)
# else:   # the indented code below "else" will be executed when "for" has
# finished looping over the entire list
#     print("The end of the list has been reached")

#  result of the above "for" block
# Cisco
# HP
# Nortel
# Avaya
# Juniper
# The end of the list has been reached


# WHILE / While Else loops - a while loop executes as long as an
# user-specified condition is evaluated as True; the "else" clause is optional

x = 1
# while x <= 10:
#     print(x)
#     x = x + 1   # or you could have x += 1
# else:
#     print("x is now greater than 10!")

# result of the above "while" block
# 1 2 3 4 5 6 7 8 9 10
# x is now greater than 10!
