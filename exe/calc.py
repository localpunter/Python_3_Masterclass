# Importing the necessary module for advanced math operations
import math


# While loop for continuously running the program and allowing the user to
# always go back to the main menu and choose another option
while True:
    # The user picks the math operation from the menu
    # (\n is used to insert a new row in the menu)
    print(
        "\nChoose the math operation.\n\n00 - Addition\n01 - Subtraction\n\
            02 - Multiplication\n03 - Division\n04 - Modulo\n\
            05 - Raising to a power\n06 - Square root\n07 - Logarithm\n\
            08 - Sine\n09 - Cosine\n10 - Tangent\n11 - Ohms Law & Power\n"
    )

    # The variable that saves the users choice
    oper = input("\nSelect an option from the menu: ")

    # ADDITION
    if oper == "0" or oper == "00":
        # This stores the first value, converted from string to float
        val1 = float(input("\nEnter the first value: "))
        # This stores the second value, converted from string to float
        val2 = float(input("\nEnter the second value: "))

        print("\nThe result is: " + str(val1 + val2) + "\n")

        # Going back to the main menu or exiting the program
        back = input("\nGo back to the main menu? (y/n) ")

        if back == "y":
            continue
        else:
            break

    # SUBTRACTION
    elif oper == "1" or oper == "01":
        val1 = float(input("\nEnter the first value: "))
        val2 = float(input("\nEnter the second value: "))

        print("\nThe result is: " + str(val1 - val2) + "\n")

        back = input("\nGo back to the main menu? (y/n) ")

        if back == "y":
            continue
        else:
            break

    # MULTIPLICATION
    elif oper == "2" or oper == "02":
        val1 = float(input("\nEnter the first value: "))
        val2 = float(input("\nEnter the second value: "))

        print("\nThe result is: " + str(val1 * val2) + "\n")

        back = input("\nGo back to the main menu? (y/n) ")

        if back == "y":
            continue
        else:
            break

    # DIVISION
    elif oper == "3" or oper == "03":
        val1 = float(input("\nEnter the first value: "))
        val2 = float(input("\nEnter the second value: "))

        print("\nThe result is: " + str(val1 / val2) + "\n")

        back = input("\nGo back to the main menu? (y/n) ")

        if back == "y":
            continue
        else:
            break

    # MODULO
    elif oper == "4" or oper == "04":
        val1 = float(input("\nEnter the first value: "))
        val2 = float(input("\nEnter the second value: "))

        print("\nThe result is: " + str(val1 % val2) + "\n")

        back = input("\nGo back to the main menu? (y/n) ")

        if back == "y":
            continue
        else:
            break

    # RAISING TO A POWER
    elif oper == "5" or oper == "05":
        val1 = float(input("\nEnter the base value: "))
        val2 = float(input("\nEnter the value to the power of: "))

        print("\nThe result is: " + str(math.pow(val1, val2)) + "\n")

        back = input("\nGo back to the main menu? (y/n) ")

        if back == "y":
            continue
        else:
            break

    # SQUARE ROOT
    elif oper == "6" or oper == "06":
        val1 = float(
            input("\nEnter the value for extracting the square root: "))

        print("\nThe result is: " + str(math.sqrt(val1)) + "\n")

        back = input("\nGo back to the main menu? (y/n) ")

        if back == "y":
            continue
        else:
            break

    # LOGARITHM
    elif oper == "7" or oper == "07":
        val1 = float(
            input("\nEnter the value for calculating the logarithm: "))
        val2 = float(
            input("\nEnter the value for calculating the logarithm base: "))

        print("\nThe result is: " + str(math.log(val1, val2)) + "\n")

        back = input("\nGo back to the main menu? (y/n) ")

        if back == "y":
            continue
        else:
            break

    # SINE
    elif oper == "8" or oper == "08":
        val1 = float(
            input("\nEnter the value (in degrees) for calculating the Sine: "))

        print("\nThe result is: " + str(math.sin(math.radians(val1))) + "\n")

        back = input("\nGo back to the main menu? (y/n) ")

        if back == "y":
            continue
        else:
            break

    # COSINE
    elif oper == "9" or oper == "09":
        val1 = float(input(
            "\nEnter the value (in degrees) for calculating the Cosine: "))

        print("\nThe result is: " + str(math.cos(math.radians(val1))) + "\n")

        back = input("\nGo back to the main menu? (y/n) ")

        if back == "y":
            continue
        else:
            break

    # TANGENT
    elif oper == "10":
        val1 = float(input(
            "\nEnter the value (in degrees) for calculating the Tangent: "))

        print("\nThe result is: " + str(math.tan(math.radians(val1))) + "\n")

        back = input("\nGo back to the main menu? (y/n) ")

        if back == "y":
            continue
        else:
            break

    # OHMS LAW & POWER
    elif oper == "11":
        watt = float(input("\nEnter Watts/Power (P): "))
        volt = float(input("\nEnter Volts (V): "))
        amp = float(input("\nEnter Amps/Current (I): "))
        ohm = float(input("\nEnter Ohms (R): "))
        result = None
        result1 = None

        # VOLTAGE
        if amp != 0 and ohm != 0:
            result = (amp * ohm)  # returns Volts
            result1 = (ohm * (amp ** 2))  # returns Watts
            print("\nThe Voltage is:", str(result), "volts" +
                  "\nThe Power is:", str(result1), "watts")

        elif watt != 0 and amp != 0:
            result = (watt / amp)  # returns Volts
            result1 = (watt / (amp ** 2))  # returns Ohms
            print("\nThe Voltage is:", str(result), "volts" +
                  "\nThe Resistance is:", str(result1), "ohms")

        elif watt != 0 and ohm != 0:
            result = (math.sqrt(watt * ohm))  # returns Volts
            result1 = (math.sqrt(watt / ohm))  # returns Amps
            print("\nThe Voltage is:", str(result), "volts" +
                  "\nThe Current is:", str(result1), "amps")

        # RESISTANCE (OHMS)
        elif volt != 0 and amp != 0:
            result = (volt / amp)  # returns Ohms
            result1 = (amp * volt)  # returns Watts
            print("\nThe Resistance is:", str(result), "ohms" +
                  "\nThe Power is:", str(result1), "watts")

        elif watt != 0 and amp != 0:
            result = (watt / (amp ** 2))  # returns Ohms
            result1 = (watt / amp)  # returns Volts
            print("\nThe Resistance is:", str(result), "ohms" +
                  "\nThe Voltage is:", str(result1), "volts")

        elif volt != 0 and watt != 0:
            result = ((volt ** 2) / watt)  # returns Ohms
            result1 = (watt / volt)  # returns Amps
            print("\nThe Resistance is:", str(result), "ohms" +
                  "\nThe Current is:", str(result1), "amps")

        # CURRENT (AMPS)
        elif volt != 0 and ohm != 0:
            result = (volt / ohm)  # returns Amps
            result1 = ((volt ** 2) / ohm)  # returns Watts
            print("\nThe Current is:", str(result), "amps" +
                  "\nThe Power is:", str(result1), "watts")

        elif watt != 0 and volt != 0:
            result = (watt / volt)  # returns Amps
            result1 = ((volt ** 2) / watt)  # returns Ohms
            print("\nThe Current is:", str(result), "amps" + "\nThe Current is:\
                ", str(result1), "amps")

        elif watt != 0 and ohm != 0:
            result = (math.sqrt(watt / ohm))  # returns Amps
            result1 = (math.sqrt(watt * ohm))  # returns Volts
            print("\nThe Current is:", str(result), "amps" +
                  "\nThe Voltage is:", str(result1), "volts")

        # POWER (WATTS)
        elif ohm != 0 and amp != 0:
            result = (ohm * (amp ** 2))  # returns Watts
            result1 = (amp * ohm)  # returns Volts
            print("\nThe Power is:", str(result), "volts" +
                  "\nThe Voltage is:", str(result1), "volts")

        elif amp != 0 and volt != 0:
            result = (amp * volt)  # returns Watts
            result1 = (volt / amp)  # returns Ohms
            print("\nThe Power is:", str(result1), "watts" +
                  "\nThe Resistance is:", str(result), "ohms")

        elif volt != 0 and ohm != 0:
            result = ((volt ** 2) / ohm)  # returns Watts
            result1 = (volt / ohm)  # returns Amps
            print("\nThe Power is:", str(result1), "watts" +
                  "\nThe Current is:", str(result), "amps")

        back = input("\nGo back to the main menu? (y/n) ")

        if back == "y":
            continue
        else:
            break

    # Handling invalid options
    else:
        print("That option is invalid!\n")
        continue
