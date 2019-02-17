#Map and Filter

def product10(a):
    return a * 10


r1 = range(10)

print(map(product10, r1))
print(list(map(product10, r1)))
print(tuple(map(product10, r1)))
print(set(map(product10, r1)))


print(map((lambda a: a * 10), r1))
print(list(map((lambda a: a * 10), r1)))
print(tuple(map((lambda a: a * 10), r1)))
print(set(map((lambda a: a * 10), r1)))

print(" ")

print(filter((lambda a: a > 5), r1))
print(list(filter((lambda a: a > 5), r1)))
print(tuple(filter((lambda a: a > 5), r1)))
print(set(filter((lambda a: a > 5), r1)))


# map() - takes a function and a sequence as arguments and applies the function to all the elements of the sequence, returning a list as the result
# def product10(a):
#     return a * 10


list1 = range(10)

# result is [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]; applying the product10() function to each element of list1
map(product10, list1)
# or...
# result is [0, 10, 20, 30, 40, 50, 60, 70, 80, 90] as well
map((lambda a: a * 10), list1)

# filter() - takes a function and a sequence as arguments and extracts all the elements in the list for which the function returns True
filter(lambda a: a > 5, list1)  # result is [6, 7, 8, 9]
