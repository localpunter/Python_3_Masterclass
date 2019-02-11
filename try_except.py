# for i in range(5):
#     try:
#         print(i / 0)
#     except ZeroDivisionError as e:
#         print(e, "--> Sorry, division by 0 is not allowed!")


# for j in range(10):
#     try:
#         print(j / 2)
#     except ZeroDivisionError as e:
#         print(e, "--> Sorry, division by 0 is not allowed!")
#     print("The rest of the code is ...")


# for k in range(5):
#     try:
#         print(k / 1)
#     except ZeroDivisionError:
#         print("You can't divide by 0 you flump!")
#     except NameError:
#         print("That's not my name!")
#     except ValueError:
#         print("That's the wrong value!")

try:
    print(4 / 2)
except NameError:
    print("Name Error!")
finally:
    print("No exceptions detected in the try block!")


try:
    print(4 / 0)
except ZeroDivisionError:
    print("0 division Error!")
finally:
    print("\nDisney matter as I will be printed anyway!\n")


# Try / Except / Else / Finally - handling an exception when it occurs and
# telling Python to keep executing the rest of the lines of code in the program
try:
    print(4/0)  # in the "try" clause you insert the code that you think might
    # generate an exception at some point
except ZeroDivisionError:
    # specifying what exception types Python should expect as a consequence of
    # running the code inside the "try" block and how to handle them
    print("Division Error!")
else:
    # executes if the code inside the "try" block raises NO exceptions
    print("No exceptions raised by the try block!")
finally:
    # executed whether the code inside the "try" block raises an exception or
    # not
    print("I don't care if an exception was raised or not!")

# result of the above block
# Division Error!
# I don't care if an exception was raised or not!
