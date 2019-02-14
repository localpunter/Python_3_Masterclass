# Ranges - unlike in Python 2, where the range() function returned a list,
# in Python 3 it returns an iterator; cannot be sliced

r = range(10)
print(r)

print(list(r))
print(set(r))
print(tuple(r))

# Return the index of 30 from the range
r1 = range(10, 100, 10)
print(r1.index(30))


# Return a list [9, 10, 11] from the range
r = range(3, 21)
my_slice = list(r)[6:9]
print(my_slice)


# r = range(10) defining a range

# r
# range(0, 10) the result

# type(r)
# <class 'range' > the result

list(r)  # converting a range to a list
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]  # the result

list(r)[2:5]  # slicing a range by using the list() function first
[2, 3, 4]  # the result
