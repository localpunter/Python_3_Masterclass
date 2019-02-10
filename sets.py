list4 = [1, 2, 3, 4, 5, 2, 3]

print("\nA list can contain duplicates:", list4)

print("\nA set can only contain unique values:", set(list4))

print("\nLength of the list:", len(list4))

print("\nLength of the set from the list", (len(set(list4))))

print(list4)

set0 = {11, 12, 13, 14, 15}

print("\nThis is set 1:", set0)

set0.add(16)
print("\nThis adds 16 to the set:", set0)

set0.remove(11)
print("\nThis removes 11 from the set:", set0)

set0.add(16)
print("\nYou cannot add a value that already exists in the set", set0)

set0.pop()
print("\nThis randomly removes an element:", set0)

set0.pop()
print("\nThis randomly removes an element:", set0)

set1 = {1, 2, 3, 4}
set2 = {3, 5, 8}

print("\nSet1:", set1)
print("Set2:", set2)

print("\nShows the elements that appear in both sets", set1.intersection(set2))

print("\nShows the difference between set 1 & 2", set1.difference(set2))
print("\nShows the difference between set 2 & 1", set2.difference(set1))

new_set = set1.union(set2)
print("This joins the 2 sets and will remove any dups:", new_set)


set3 = {"Alan", "Rachel", "Lego", 73, 81, 0.5}
print("\nThis is set3:", set3)

set4 = {0.5, 81, 73, "Lego", "Rachel", "Alan"}
print("This is set4:", set4)

set1 = {"1.1.1.1", "2.2.2.2", "3.3.3.3", "4.4.4.4"}  # creating a set

list1 = [11, 12, 13, 14, 15, 15, 15, 11]
string1 = "aaabcdeeefgg"


# Frozensets - immutable sets. The elements of a frozenset remain the
# same after creation.
fs1 = frozenset(list1)  # defining a frozenset

fs1
frozenset({11, 12, 13, 14, 15})  # the result

type(fs1)
# <class 'frozenset' > the result

# proving that frozensets are indeed immutable
# fs1.add(10)
# AttributeError: 'frozenset' object has no attribute 'add'

# fs1.remove(1)
# AttributeError: 'frozenset' object has no attribute 'remove'

# fs1.pop()
# AttributeError: 'frozenset' object has no attribute 'pop'

# fs1.clear()
# AttributeError: 'frozenset' object has no attribute 'clear'

# Sets - methods
set1.intersection(set2)  # returns the common elements of the two sets

set1.difference(set2)  # returns the elements that set1 has and set2 doesn't

# unifying two sets; the result is also a set, so there are no duplicate
# elements; not to be confused with concatenation
set1.union(set2)

set1.pop()  # removes a random element from the set; set elements cannot be
# removed by index because sets are UNORDERED collections of elements, so
# there are no indexes to use

set1.clear()  # clearing a set; the result is an empty set
