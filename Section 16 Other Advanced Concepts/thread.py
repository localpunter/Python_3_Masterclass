# Threading

import threading
import time


# Defining the main function
def my_function():
    print("Start a thread")
    time.sleep(3)
    print("End the thread!")

# Defines an empty list of threads
threads = []

# Runs 5 concurrent sessions of my_function
for i in range(5):
    th = threading.Thread(target = my_function)
    th.start() # Starting the thread
    threads.append(th)

# Waiting for all the threads to terminate
for th in threads:
    th.join()


# def my_function():
#     print("Start a thread")
#     time.sleep(3)
#     print("End the thread!")


# threads = []

# for i in range(5):
#     my_function()


# start()  # simply starts or initiates the thread

# join()  # makes sure the program waits for all threads to terminate

# using the Thread class form the 'threading' module and telling it the target function to be executed using the 'target' argument
# th = threading.Thread(target=myfunction)
