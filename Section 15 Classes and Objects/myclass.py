# from newclass import MyNewRouter


class MyRouter():
    """This is a class that describes the characteristics or a router."""

    def __init__(self, routername, model, serialno, ios):
        self.routername = routername
        self.model = model
        self.serialno = serialno
        self.ios = ios

    def print_router(self, manuf_date):
        print("\nThe router name is: ", self.routername)
        print("The router model is: ", self.model)
        print("The router serial number is: ", self.serialno)
        print("The IOS version is: ", self.ios)
        print("The model and date combined: ", self.model + manuf_date)


router1 = MyRouter("R1", "2600", "123456", "12.4")

print(router1)
print(router1.routername)
print(router1.model)
print(router1.serialno)
print(router1.ios)

router1.print_router("14031973")


router2 = MyRouter("Netgear", "6700", "00300021", "candyfloss")

router2.print_router("30071981")

router2.ios = "flossycandy"
print("\nThe IOS has been changed to:", router2.ios)

print("getattr return the attribute - Router name:",
      getattr(router2, "routername"))
setattr(router2, "routername", "TP-Link")
print("setattr is used to change the attribute name - Router name:",
      getattr(router2, "routername"))


# class MyNewRouter(MyRouter):
def __init__(self, routername, model, serialno, ios, portsno):
    MyRouter.__init__(self, routername, model, serialno, ios)
    self.portsno = portsno


def print_new_router(self, string):
    print(string + self.model)


# new_router1 = MyNewRouter("new router 1", "1888", 101010101, 19.67, 10)
# print(new_router1)


getattr(router2, "ios")  # getting the value of an attribute

setattr(router2, "ios", "12.1")  # setting the value of an attribute

hasattr(router2, "ios")  # checking if an object attribute exists

delattr(router2, "ios")  # deleting an attribute

# verifying if an object is an instance of a particular class
isinstance(router2, MyRouter)
