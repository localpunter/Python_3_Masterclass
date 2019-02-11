# user_says = input("Please enter the string you want to print: ")

# print(user_says)

# my_tuple = (
#     101, [], 10.1, 1.01,
#     'Love', 'Python', 'Java', 'C++', 'C#', 'SQL',
#     0, 0.1, (80,)
#     )

# x = my_tuple[4::5]

# print(x)

my_dict = {1: "Cisco", 2: "HP", 3: "Juniper", 4: "Arista", 5: "Avaya"}
sorted_vals = list(my_dict.values())
print(sorted_vals)
sorted_vals.sort()
print(sorted_vals[0])


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
