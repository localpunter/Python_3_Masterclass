# user_says = input("Please enter the string you want to print: ")

# print(user_says)

# my_tuple = (
#     101, [], 10.1, 1.01,
#     'Love', 'Python', 'Java', 'C++', 'C#', 'SQL',
#     0, 0.1, (80,)
#     )

# x = my_tuple[4::5]

# print(x)

# my_dict = {1: "Cisco", 2: "HP", 3: "Juniper", 4: "Arista", 5: "Avaya"}
# sorted_vals = list(my_dict.values())
# print(sorted_vals)
# sorted_vals.sort()
# print(sorted_vals[0])


# my_dict = {1: "LG", 2: "HP", 3: "Samsung", 4: "Sony"}

# print(my_dict[3] == "Samsung")
# # or
# print(3 in my_dict)

# my_dict = {
#     'IOS': '12.4',
#     'Model': '2600',
#     'RAM': '128',
#     'Vendor': 'Cisco',
#     'Ports': '4'
#     }

# my_dict['RAM'] = '256'

# print(my_dict['RAM'])

# x = 2
# x = 11
# x = 10

# if x < 10:
#     for i in range(1, 5):
#         print(x * i)
# elif x > 10:
#     j = 1
#     while j < 5:
#         print(x * j)
#         j = j + 1
# else:
#     print(x ** 10)

# x = "Hello Python"

# if x.startswith("H") and len(x) > 12:

#     print("'/'.join(x[:7])")

# elif x[:-1] == "n" and len(x.split('o')) >= 3:

#     for i in x.strip('n'):

#         print(i * 2)

# else:

#     print((x + ' ') * 3 + "!")

# x = "Hello Python"

# if x.startswith("H") and len(x) > 12:

#     print("'/'.join(x[:7])")

# elif x[-1] == "n" and len(x.split('o')) >= 3:

#     print(x.lower()[4:])

# else:

#     print((x + ' ') * 3 + "!")

# x = "Hello Python"

# if x.startswith("H") or len(x) > 12:

#     print('/'.join(x[:7]))

# elif x[-1] == "n" and len(x.split('o')) >= 3:

#     print(x.lower()[4:])

# else:

#     print((x + ' ') * 3 + "!")

# def my_func(x, y):
#     result = x ** y
#     return result + 500

# print(my_func(10, 3))

# var1 = 100

# def var1_func():
#     global var1
#     print(var1 * 10)
#     var1 = 200

# var1_func()


# myfile = open("myfile.txt", "w")

# myfile.write("Python\nJava\nJavascript\nC++\nHTML\nCSS\nSwift")

# myfile = open("myfile.txt")

# #This should return "Javascript\n"
# print(myfile.readlines()[2])


# myfile = open("myfile2.txt", "w+")

# myfile.write("Python\nJava\nJavascript\nC++\nHTML\nCSS\nSwift")

# myfile.seek(0)

# #This should return "Javascript"
# print(myfile.readlines()[2])


# myfile = open("myfile2.txt", "w")

# myfile.write("Python\nJava\nJavascript\nC++\nHTML\nCSS\nSwift\n")

# myfile.close()

# myfile = open("myfile2.txt", "a+")

# myfile.write("Ruby")

# myfile.seek(0)

# #This should return "Ruby"
# print(myfile.readlines()[7])


# my_regex_str = '200.10.2.0 255.255.255.0 200.20.5.2 1 205 T#1 S IB 5'

import re
# a = re.match(r"255", my_regex_str)
# print(type(a))


# b = re.search(r"(.+?) +\d\d(\d)\.([0-9]{2,})\.([0-9]{1,3})\.(\d) +(.+)1 +(\d{3}) +(\w{1})#.+S(\s+)(\w)\w +(.*)", my_regex_str)
# print(b.group(0))

regex_str = "123.456.789   0 PYTHON 3"
# Return 123.456.789 with no white space after. (.+\S) or (.+\?) = '123.456.789'
# Return 123.456.789 with the white space after. (.+) = '123.456.789  '

regex = re.search(r"(.+\S)\s{2,}", regex_str)
# or - regex = re.search(r"(.+\?)\s{2,}", regex_str)

# print(regex.group(1))

# regex = re.sub(r"\w", "%", regex_str)

# print(regex)


# r1 = range(10, 20)
# print(list(filter((lambda a: a < 16), r1)))

r1 = range(10)

print(list(map((lambda a: a * 10), r1))[-1])