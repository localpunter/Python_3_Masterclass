# Importing the necessary module for advanced math operations
import math


# While loop for continuously running the program and allowing the user to always go back to the main menu and choose another option
while True:
    # The user picks the math operation from the menu (\n is used to insert a new row in the menu)
    print(
        "\nChoose the math operation.\n\n00 - Addition\n01 - Subtraction\n02 - Multiplication\n03 - Division\n04 - Modulo\n05 - Raising to a power\n06 - Square root\n07 - Logarithm\n08 - Sine\n09 - Cosine\n10 - Tangent\n11 - Ohms Law & Power\n12 - Distance, Speed & Time\n13 - Perimeter, Area & Volume\n\nFOR ANY MEASUREMENT YOU DO NOT HAVE, ENTER '0'.")

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
        val1 = float(input("\nEnter the value for extracting the square root: "))

        print("\nThe result is: " + str(math.sqrt(val1)) + "\n")

        back = input("\nGo back to the main menu? (y/n) ")

        if back == "y":
            continue
        else:
            break



    # LOGARITHM
    elif oper == "7" or oper == "07":
        val1 = float(input("\nEnter the value for calculating the logarithm: "))
        val2 = float(input("\nEnter the value for calculating the logarithm base: "))

        print("\nThe result is: " + str(math.log(val1, val2)) + "\n")

        back = input("\nGo back to the main menu? (y/n) ")

        if back == "y":
            continue
        else:
            break


    # SINE
    elif oper == "8" or oper == "08":
        val1 = float(input("\nEnter the value (in degrees) for calculating the Sine: "))

        print("\nThe result is: " + str(math.sin(math.radians(val1))) + "\n")

        back = input("\nGo back to the main menu? (y/n) ")

        if back == "y":
            continue
        else:
            break



    # COSINE
    elif oper == "9" or oper == "09":
        val1 = float(input("\nEnter the value (in degrees) for calculating the Cosine: "))

        print("\nThe result is: " + str(math.cos(math.radians(val1))) + "\n")

        back = input("\nGo back to the main menu? (y/n) ")

        if back == "y":
            continue
        else:
            break



    # TANGENT
    elif oper == "10":
        val1 = float(input("\nEnter the value (in degrees) for calculating the Tangent: "))

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
            result = (amp * ohm) # returns Volts
            result1 = (ohm * (amp ** 2)) # returns Watts
            print("\nThe Voltage is:", str(round(result, 2)), "volts" + "\nThe Power is:", str(round(result1, 2)), "watts")

        elif watt != 0 and amp != 0:
            result = (watt / amp) # returns Volts
            result1 = (watt / (amp ** 2)) # returns Ohms
            print("\nThe Voltage is:", str(round(result, 2)), "volts" + "\nThe Resistance is:", str(round(result1, 2)), "ohms")

        elif watt != 0 and ohm!= 0:
            result = (math.sqrt(watt * ohm)) # returns Volts
            result1 = (math.sqrt(watt / ohm)) # returns Amps
            print("\nThe Voltage is:", str(round(result, 2)), "volts" + "\nThe Current is:", str(round(result1, 2)), "amps")


        # RESISTANCE (OHMS)
        elif volt != 0 and amp !=0:
            result = (volt / amp) # returns Ohms
            result1 = (amp * volt) # returns Watts
            print("\nThe Resistance is:", str(round(result, 2)), "ohms" + "\nThe Power is:", str(round(result1, 2)), "watts")

        elif watt != 0 and amp != 0:
            result = (watt / (amp ** 2)) # returns Ohms
            result1 = (watt / amp) # returns Volts
            print("\nThe Resistance is:", str(round(result, 2)), "ohms" + "\nThe Voltage is:", str(round(result1, 2)), "volts")

        elif volt != 0 and watt != 0:
            result = ((volt ** 2) / watt) # returns Ohms
            result1 = (watt / volt) # returns Amps
            print("\nThe Resistance is:", str(round(result, 2)), "ohms" + "\nThe Current is:", str(round(result1, 2)), "amps")


        # CURRENT (AMPS)
        elif volt != 0 and ohm != 0:
            result = (volt / ohm) # returns Amps
            result1 = ((volt ** 2) / ohm) # returns Watts
            print("\nThe Current is:", str(round(result, 2)), "amps" + "\nThe Power is:", str(round(result1, 2)), "watts")

        elif watt != 0 and volt != 0:
            result = (watt / volt) # returns Amps
            result1 = ((volt ** 2) / watt) # returns Ohms
            print("\nThe Current is:", str(round(result, 2)), "amps" + "\nThe Current is:", str(round(result1, 2)), "amps")

        elif watt != 0 and ohm != 0:
            result = (math.sqrt(watt / ohm)) # returns Amps
            result1 = (math.sqrt(watt * ohm)) # returns Volts
            print("\nThe Current is:", str(round(result, 2)), "amps" + "\nThe Voltage is:", str(round(result1, 2)), "volts")


        # POWER (WATTS)
        elif ohm != 0 and amp != 0:
            result = (ohm * (amp ** 2)) # returns Watts
            result1 = (amp * ohm) # returns Volts
            print("\nThe Power is:", str(round(result, 2)), "volts" + "\nThe Voltage is:", str(round(result1, 2)), "volts")

        elif amp != 0 and volt != 0:
            result = (amp * volt) # returns Watts
            result1 = (volt / amp) # returns Ohms
            print("\nThe Power is:", str(round(result1, 2)), "watts" + "\nThe Resistance is:", str(round(result, 2)), "ohms")

        elif volt != 0 and ohm != 0:
            result = ((volt ** 2) / ohm) # returns Watts
            result1 = (volt / ohm) # returns Amps
            print("\nThe Power is:", str(round(result1, 2)), "watts" + "\nThe Current is:", str(round(result, 2)), "amps")


        back = input("\nGo back to the main menu? (y/n) ")

        if back == "y":
            continue
        else:
            break


    # DISTANCE, SPEED & TIME
    elif oper == "12":
        distance = float(input("\nEnter Distance in km (D): "))
        speed = float(input("\nEnter Speed in km/h (S): "))
        time = float(input("\nEnter Time in minutes (T): "))
        speedKm = float(speed / 3.6)
        timeM = float(time * 60)
        distanceKm = float(distance * 1000)
        result = None
        result1 = None

        # DISTANCE (meters & km)
        if speed != 0 and time != 0:
            result = ((speedKm) * (timeM)) # returns Distance in meters
            result1 = ((speedKm) * (timeM) / (1000)) # return Distance in km
            result2 = ((speedKm) * (timeM) / (1609.344)) # return Distance in miles
            print("\nThe Distance is:", str(round(result, 2)), "meters " + "OR", str(round(result1, 2)), "km" + " OR", str(round(result2, 2)), "miles")

        # SPEED
        elif distance != 0 and time != 0:
            result = ((distanceKm) / (timeM)) # returns Speed in meters per second
            result1 = ((distanceKm) / (timeM) * (3.6)) # returns Speed in km/h
            result2 = ((distanceKm) / (timeM) * (2.237)) # returns Speed in mp/h
            print("\nThe Speed is:", str(round(result, 2)), "m/s " + "OR", str(round(result1, 2)), "km/h" + " OR", str(round(result2, 2)), "mp/h")

        # TIME
        import time
        result = ( distanceKm / speedKm) # returns Time in seconds
        def convert(seconds):
            if distance != 0 and speed != 0:
                return time.strftime("%H:%M:%S", time.gmtime(n)) # coverts from seconds to hh:mm:ss
        n = result
        print("\nThe Time taken is (hh:mm:ss):", convert(n))



        back = input("\nGo back to the main menu? (y/n) ")

        if back == "y":
            continue
        else:
            break

    # PERIMETER, AREA & VOLUME
    elif oper == "13":

        # The user picks what shape they want to measure
        print(
        "\nChoose what shape you want to measure.\n\n01 - Square/Rectangle/Cube/Cuboid\n02 - Triangle/Triangular Prism\n03 - Circle/Cylinder\n04 - Sphere")

        # The variable that saves the users shape choice
        shapeSelect = input("\nSelect an option from the menu: ")

        if shapeSelect == "01" or shapeSelect == "1" or shapeSelect == "02" or shapeSelect == "2" or shapeSelect == "03" or shapeSelect == "3" or shapeSelect == "04" or shapeSelect == "4":

            # The user picks what they want to measure
            print(
            "\nChoose what you want to measure.\n\n01 - Perimeter\n02 - Area\n03 - Volume")

            # The variable that saves the users measurement choice
            measureSelect = input("\nSelect an option from the menu: ")

            #SQUARE/RECTANGLE/CUBE/CUBOID
            if ((shapeSelect == "01" or shapeSelect == "1") and (measureSelect == "01" or measureSelect == "1")):
                length = float(input("\nEnter Length in mm (L): "))
                width = float(input("\nEnter Width in mm (W): "))
                perimeter = ((length * 2) + (width * 2))
                perimeterCm = (perimeter / 10)
                perimeterM = (perimeter / 1000)
                print("\nThe Perimeter is:", str(round(perimeter, 2)), "mm "+ "OR", str (round(perimeterCm, 2)), "cm " + "OR", str(round(perimeterM, 2)), "m") # Returns Perimeter in mm, cm and m

            elif ((shapeSelect == "01" or shapeSelect == "1") and (measureSelect == "02" or measureSelect == "2")):
                length = float(input("\nEnter Length in mm (L): "))
                width = float(input("\nEnter Width in mm (W): "))
                area = (length * width)
                areaCm = (area / 100)
                areaM = (areaCm / 10000)
                print("\nThe Area is:", str(round(area, 2)), "mm2 " + "OR", str (round(areaCm, 2)), "cm2 " + "OR", str(round(areaM, 2)), "m2") #Returns Area in mm2, cm2 and m2

            elif ((shapeSelect == "01" or shapeSelect == "1") and (measureSelect == "03" or measureSelect == "3")):
                length = float(input("\nEnter Length in mm (L): "))
                width = float(input("\nEnter Width in mm (W): "))
                depth = float(input("\nEnter Depth in mm (D): "))
                volume = (length * width * depth)
                volumeCm = (volume / 1000)
                volumeM = (volumeCm / 1000000)
                print("\nThe Volume is:", str(round(volume, 2)), "mm3 " +"OR", str (round(volumeCm, 2)), "cm3 " + "OR", str(round(volumeM, 2)), "m3") #Returns Volume in mm3, cm3 and m3

            #TRIANGLE/TRIANGULAR PRISM
            if shapeSelect == "02" or shapeSelect == "2":
                print("\n***PLEASE NOTE***:\nFor Perimeter use: 'base, side & side1'.\nFor Area use 'base & height'.\nFor Volume use 'base, height & length'.")
                base = float(input("\nEnter the length of the base in mm (B): "))
                height = float(input("\nEnter the length of the height in mm (H): "))
                side = float(input("\nEnter the length of the side in mm (S): "))
                side1 = float(input("\nEnter the length of the other side in mm (S): "))
                length = float(input("\nEnter the length in mm (L): "))
                perimeter = None
                area = None
                volume = None

                #PERIMETER
                if(measureSelect == "01" or measureSelect == "1") and (base != 0 and side != 0 and side1 != 0):
                    perimeter = (base + side + side1)
                    perimeterCm = (perimeter / 10)
                    perimeterM = (perimeter / 1000)
                    print("\nThe Perimeter is:", str(round(perimeter, 2)), "mm " + "OR", str(round(perimeterCm, 2)), "cm " + "OR", str(round(perimeterM, 2)), "m")

                #AREA
                elif (measureSelect == "02" or measureSelect == "2") and (base != 0 and height != 0 and length == 0):
                    area = ((base / 2) * (height))
                    areaCm = (area / 100)
                    areaM = (area / 10000)
                    print("\nThe Area is:", str(round(area, 2)), "mm2 " + "OR", str(round(areaCm, 2)), "cm2 " + "OR", str(round(areaM, 2)), "m2")

                #VOLUME
                elif (measureSelect == "03" or measureSelect == "3") and (base !=0 and height != 0 and length != 0):
                    volume = ((base / 2) * (height) * (length))
                    volumeCm = (volume / 1000)
                    volumeM = (volumeCm / 1000000)
                    print("\nThe volume is:", str(round(volume, 2)), "mm3 " + "OR", str(round(volumeCm, 2)), "cm3 " + "OR", str(round(volumeM, 2)), "m3")

            # CIRCLE/CYLINDER
            from math import pi
            if (shapeSelect == "03" or shapeSelect == "3"):
                radius = float(input("\nEnter the radius in mm (R): "))
                diameter = float(input("\nEnter the diameter in mm (D): "))
                height = float(input("\nEnter the height in mm (H): "))
                perimeter = None
                area = None
                volume = None

                #PERIMETER/CIRCUMFERENCE
                if (measureSelect == "01" or measureSelect == "1") and (height == 0):
                    if diameter != 0:
                        perimeter = (pi * diameter)
                    elif diameter == 0 and radius != 0:
                        perimeter = (pi * (radius * 2))
                    perimeterCm = (perimeter / 10)
                    perimeterM = (perimeter / 1000)
                    print("\nThe Perimeter of the circle is:", str(round(perimeter, 2)), "mm " + "OR", str(round(perimeterCm, 2)), "cm " + "OR", str(round(perimeterM, 2)), "m")

                #AREA CIRCLE
                elif (measureSelect == "02" or measureSelect == "2") and height == 0:
                    if radius == 0 and diameter != 0:
                        area = (pi * ((diameter / 2) * (diameter / 2)))
                    elif radius != 0:
                        area = (pi * (radius * radius))
                    areaCm = (area / 100)
                    areaM = (areaCm / 10000)
                    print("\nThe Area of the circle is:", str(round(area, 2)), "mm2 " + "OR", str(round(areaCm, 2)), "cm2 " + "OR", str(round(areaM, 5)), "m2")

                # AREA CYLINDER
                elif (measureSelect == "02" or measureSelect == "2") and height != 0:
                    if radius == 0 and diameter !=0:
                        area = 2 * (pi * ((diameter / 2) * (diameter / 2))) + (2 * (pi *(diameter / 2) * (height)))
                    elif radius != 0:
                        area = 2 * (pi * ((radius) * (radius))) + (2 * (pi * (radius) *(height)))
                    areaCm = (area / 100)
                    areaM = (areaCm / 10000)
                    print("\nThe Area of the Cylinder is:", str(round(area, 2)), "mm2 " + "OR", str(round(areaCm, 2)), "cm2 " + "OR", str(round(areaM, 5)), "m2")

                # VOLUME CYLINDER
                if (measureSelect == "03" or measureSelect == "3") and height != 0:
                    if radius == 0 and diameter != 0:
                        volume = pi * ((diameter / 2) * (diameter / 2)) * height
                    elif radius != 0:
                        volume = pi * (radius * radius) * height
                    volumeCm = (volume / 1000)
                    volumeM = (volumeCm / 1000000)
                    volumemL = (volume / 1000)
                    volumecL = (volume / 10000)
                    volumeL = (volume / 1000000)
                    print("\nThe Volume of the Cylinder is:", "\n", str(round(volume, 2)), "mm3 /", str(round(volumemL, 2)), "mL" + "\nOR", str(round(volumeCm, 2)), "cm3 /", str(round(volumecL, 2)), "cL" + "\nOR", str(round(volumeM, 5)), "m3 /", str(round(volumeL, 5)), "L")

            # SPHERE
            if (shapeSelect == "04" or shapeSelect == "4"):
                radius = float(input("\nEnter the Radius in mm (R): "))
                diameter = float(input("\nEnter the Diameter in mm (D): "))
                area = None
                volume = None

                # AREA SPHERE
                if (measureSelect == "02" or measureSelect == "2"):
                    if radius == 0 and diameter != 0:
                        area = 4 * pi * ((diameter / 2) * (diameter / 2))
                    elif radius != 0:
                        area = 4 * pi * (radius * radius)
                    areaCm = (area / 100)
                    areaM = (areaCm / 10000)
                    print("\nThe Area of the Sphere is:", str(round(area, 2)), "mm2 " + "OR", str(round(areaCm, 2)), "cm2 " + "OR", str(round(areaM, 2)), "m2")

                # VOLUME SPHERE
                if (measureSelect == "03" or measureSelect == "3"):
                    if radius == 0 and diameter != 0:
                        volume = (4 * pi * ((diameter / 2) * (diameter / 2) * (diameter / 2))) / 3
                    elif radius != 0:
                        volume = (4 * pi * (radius * radius * radius)) / 3
                    volumeCm = (volume / 1000)
                    volumeM = (volumeCm / 1000000)
                    print("\nThe Volume of the Sphere is:", str(round(volume, 2)), "mm3 " + "OR", str(round(volumeCm, 2)), "cm3 " + "OR", str(round(volumeM, 5)), "m3")


            back = input("\nGo back to the main menu? (y/n) ")

            if back == "y":
                continue
            else:
                break

    # Handling invalid options
    else:
        print("That option is invalid!\n")
        continue
