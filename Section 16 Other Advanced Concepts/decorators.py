# Decorators - functions that take another function as a parameter and extend its functionality and behavior without modifying it


def my_decorator(target_function):
    def function_wrapper():
        return "Python is such a " + target_function() + " language!"
    return function_wrapper


@my_decorator
def target_function():
    return "cool"


# returns 'Python is the coolest programming language!'
print(target_function())
