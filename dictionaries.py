# Dictionaries - a dictionary is an unordered set of key-value pairs

dict1 = {}
print("\nThis will return the type of dict1:", type(dict1))

dict1 = {"Alan": "73", "Rachel": "81", "Lego": "0.5"}

print("This returns the value attributed to Lego:", dict1["Lego"])

dict1["Chip"] = "0.05"

print("\nThis will add key 'Chip' and value '0.05' to dict1:", dict1)

dict1["Lego"] = "0.75"

print("This will change the value of Lego to 0.75:", dict1)

del dict1["Chip"]

print("This will delete both the key and value of Chip:", dict1)

print("\nThis will print the length of the dictionary:", len(dict1))

print("\nThis will return just the keys from the dictionary:", dict1.keys())
print("This will return just the values from the dictionary:", dict1.values())
print("Returns a list of tuples with each key value pair:", dict1.items())

num = 10
num_bin = bin(num)
print("\nThis converts 10 into binary:", num_bin)

num_hex = hex(num)
print("This converts 10 into hex:", num_hex)

bin_to_num = int(num_bin, 2)
print("\nThis converts num_bin to an Int:", bin_to_num)

hex_to_num = int(num_hex, 16)
print("This converts num_hex to an Int:", hex_to_num)

# This converts the values of the dictionary to a list, sorts the list
# alphabetically and returns index[0]

my_dict = {1: "Cisco", 2: "HP", 3: "Juniper", 4: "Arista", 5: "Avaya"}
sorted_vals = list(my_dict.values())
print(sorted_vals)
sorted_vals.sort()
print(sorted_vals[0])

# dict1 = {} creating an empty dictionary

# dict1 = {"Vendor": "Cisco", "Model": "2600", "IOS": "12.4", "Ports": "4"}

# dict1["IOS"] returns "12.4"; extracting a value for a specified key

# dict1["IOS"] = "12.3" modifies an existing key-value pair

# dict1["RAM"] = "128" adds a new key-value pair to the dictionary

# del dict1["Ports"] deleting a key-value pair from the dictionary

# len(dict1) returns the number of key-value pairs in the dictionary

# "IOS" in dict1 verifies if "IOS" is a key in the dictionary

# "IOS2" not in dict1 verifies if "IOS2" is not a key in the dictionary

#  Dictionaries - methods
# dict1.keys() returns a list having the keys in the dictionary as elements

# dict1.values() returns a list having the values in the dictionary as elements

# dict1.items() returns a list of tuples, each tuple containing the
# key and value of each dictionary pair

#  Conversions between data types
# str()   converting to a string
# int()   converting to an integer
# float()   converting to a float
# list()   converting to a list
# tuple()   converting to a tuple
# set()   converting to a set
# bin()   converting to a binary representation
# hex()   converting to a hexadecimal representation
# int(variable, 2)   converting from binary back to decimal
# int(variable, 16)   converting from hexadecimal back to decimal
