# The order of operations is:
# 1. Rasing to a power (**)
# 2. Multiplication, division, modulo (*, /, %)
# 3. Addition, subtraction (+, -)
# Where more than 1 operation is in the same order,
# it's worked from left to right

# The order of the below example is: 5**2 = 25, /5 = 5, *2 = 10,
# 100-10 = 90, +4 = 94
eq = 100 - 5 ** 2 / 5 * 2 + 4
print(eq)

# There are 2 way to call the power of:
a = 5 ** 5
b = pow(5, 5)
print(a, b)


# Numbers - math operations
# 1 + 2  addition

# 2 – 1  subtraction

# 4 / 2  division

# 4 * 2  multiplication

# 4 ** 2  raising to a power

# modulo (this means finding out the remainder after division
# of one number by another)
# 5 % 2

# Numbers - float division vs. integer division (special case)
# 3 / 2   float division; result is 1 in Python 2 and 1.5 in Python 3

# 3 // 2   integer division; result is 1 in Python 2 and Python 3

# Numbers - conversion between numeric types
# int(1.5) result is 1

# float(2) result is 2.0

# Numbers - useful functions
# abs(5) the distance between the number in between parantheses and 0

# abs(-5) returns the same result as abs(5)

# max(1, 2) returns the largest number

# min(1, 2) returns the smallest number

# pow(3, 2) another way of raising to a power
