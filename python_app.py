
# Modules and importing - Basics
# importing all the names (variables and functions) from the math module
# from math import *
# importing only a function (sin()) from the math module; there's no need to add the parantheses of the function when importing it
from math import sin
from math import pi  # importing only a variable (pi) from the math module
import sys  # importing the sys module; the import statements should be placed before any other code in your application
import my_module
import sys


print("This is my app!")

print(my_module.my_var)

my_module.my_function()

# print(help(sys))

print(dir(sys))


