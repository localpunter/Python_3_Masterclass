list1 = []


for i in range(10):
    result = i ** 2
    list1.append(result)

print(list1)
print(type(list1))


list2 = [x ** 2 for x in range(10)]
print(list2)


list3 = [x ** 2 for x in range(10) if x > 5]
print(list3)
print([x * 10 for x in range(11) if x >= 7])

# ...we can use a list comprehension
list2 = [x ** 2 for x in range(10)]

list3 = [x ** 2 for x in range(10) if x > 5]  # with a conditional statament
