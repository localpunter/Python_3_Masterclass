# Break, Continue, Pass

# for number in range(10):
#     if number == 7:
#         break
#     print(number)


list1 = [4, 5, 6]
list2 = [10, 20, 30]

for i in list1:
    for j in list2:
        if j == 20:
            break  # stops the execution here, ignores the print statement
            # below and completely quits THIS "for" loop; however, it
            # doesn't quit the outer "for" loop, too!
        print("i * j", i * j)
    print("This is outside the nested loop")


print(" ")

list1 = [4, 5, 6]
list2 = [10, 20, 30]

for k in list1:
    for l in list2:
        if l == 20:
            continue  # ignores the rest of the code below for the current
            # iteration, then goes up to the top of the loop (inner "for")
            # and starts the next iteration
        print("k * l", k * l)
    print("This is outside the other nested loop")


for i in list1:
    pass  # pass is the equivalent of "do nothing"; it is actually a
    # placeholder for when you just want to write a piece of code that you
    # will treat later
