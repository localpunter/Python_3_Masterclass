# Functions - Basics


def my_function(x):
    """This is the first function of the course"""
    print(x)


my_function("Hello Python!")


def next_function(x, y):
    print("\nHello " + x)
    print("Hello " + y)


next_function("Alan", "Rachel")

next_function("Chip", "Lego")


def my_sum(x, y):
    sum = x + y
    return sum


print("\n", my_sum(345, 9843))


def my_next_sum(x, y, z):
    sum = (x + y) * z
    return sum ** 2


print("\n", my_next_sum(1, 2, 3))


# def my_new_sum(x, y, z):
#     sum = (x + y) * z
#     return  # This returns 'None' as we haven't specified what to return
# print("\n", my_new_sum(1, 2, 3))


def my_first_function(x, y):  # defining a function that takes two parameters
    sum = x + y
    return sum  # this statement is used to exit a function and return something when the function is called


# calling a function and passing two POSITIONAL arguments, the values of 1 and 2; result is 3
my_first_function(1, 2)

# calling a function and passing two KEYWORD arguments, the values of 1 and 2; result is 3
my_first_function(x=1, y=2)

# calling a function and passing mixed types of arguments, the values of 1 and 2; result is 3; rule: positional arguments always before keyword arguments!
my_first_function(1, y=2)


# specifying a default parameter value in a function definition
# def my_first_function(x, y, z=3):

# specifying a variable number of positional parameters in a function definition; args is a tuple
# def my_first_function(x, *args):

# specifying a variable number of keyword parameters in a function definition; args is a tuple
# def my_first_function(x, **kwargs):

# global my_var  # "importing" a variable in the global namespace to the local namespace of a function
