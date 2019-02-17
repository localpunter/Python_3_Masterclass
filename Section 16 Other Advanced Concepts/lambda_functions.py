# Lambda functions - anonymous functions
# lambda arg1, arg2, ..., arg n: an expression using the arguments general syntax

a = lambda x, y: x * y
print(type(a)) # returns <class 'function'>

print(a(2, 10))
print(a(5, 50))


def myfunc(mylist):
    list_xy = []
    for x in range(10):
        for y in range(5):
            result = x * y
            list_xy.append(result)
    return list_xy + mylist

print(myfunc([100, 101, 102, 103, 104, 105]))
print(myfunc([]))

# or we can use a lambda function, a list comprehension and concatenation on a single line of code

b = lambda mylist: [x * y for x in range (10) for y in range(5)] + mylist
print(b([100, 101, 102, 103, 104, 105]))
print(b([]))

b = [x * y for x in range (10) for y in range(5)]
print(b)

my_lam = lambda x, y: x * y

print(my_lam(10, 20))