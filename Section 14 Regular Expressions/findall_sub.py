# Regular Expressions - the "re.findall" and "re.sub" methods
import re

# arp = "22.22.22.1    0      b4:a9:5a:ff:c8:45  VLAN#222         L"
arp = "22.22.22.1    0      b4:a9:5a:ff:c8:45  VLAN#222    10.10.10.1     L"


# This returns the IP add as a list
a = re.findall(r"\d\d\.\d{2}\.[0-9][0-9]\.[0-9]{1,3}", arp)
print(a)

# This returns the IP address as a tuple
b = re.findall(r"(\d\d)\.(\d{2})\.([0-9][0-9])\.([0-9]{1,3})", arp)
print(b)


arp = "22.22.22.1    0      b4:a9:5a:ff:c8:45  VLAN#222         L"
c = re.sub(r"\d", "7", arp)
print(c)


# returns a list where each element is a pattern that was matched inside the target string
a = re.findall(r"\d\d\.\d{2}\.[0-9][0-9]\.[0-9]{1,3}", arp)
['22.22.22.1']  # result of the above operation - a list with only one element, the IP address matched by the regex

# replaces all occurrences of the specified pattern in the target string with a string you enter as an argument
b = re.sub(r"\d", "7", arp)
# result of the above operation
'77.77.77.7      7         b7:a7:7a:ff:c7:77 VLAN#777             L   77.77.77.77'
