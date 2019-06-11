# Importing the necessary module for advanced math operations
import math


# While loop for continuously running the program and allowing the user to always go back to the main menu and choose another option
while True:
    # The user picks the math operation from the menu (\n is used to insert a new row in the menu)
    print(
        "\nChoose the math operation.\n\n00 - Addition\n01 - Subtraction\n02 - Multiplication\n03 - Division\n04 - Modulo\n05 - Raising to a power\n06 - Square root\n07 - Logarithm\n08 - Sine\n09 - Cosine\n10 - Tangent\n11 - Ohms Law & Power\n12 - Distance, Speed & Time\n13 - Perimeter, Area & Volume\n14 - Weight")

    # The variable that saves the users choice
    oper = input("\nSelect an option from the menu: ")

    # PERIMETER, AREA & VOLUME
    if oper == "13":

        # The user picks what shape they want to measure
        print(
        "\nChoose what shape you want to measure.\n\n01 - Square/Rectangle/Cube/Cuboid\n02 - Triangle/Triangular Prism\n03 - Circle/Cylinder\n04 - Sphere")

        # The variable that saves the users shape choice
        shapeSelect = input("\nSelect an option from the menu: ")

        if shapeSelect != 0:

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
                perimeterIn = (perimeter * 0.0393701)
                perimeterFt = (perimeter * 0.00328084)
                perimeterYd = (perimeter * 0.00109361)
                print("\nThe Perimeter is:", str(round(perimeter, 2)), "mm "+ "OR", str (round(perimeterCm, 2)), "cm " + "OR", str(round(perimeterM, 2)), "m\n", str(round(perimeterIn, 2)), "in " + "OR", str(round(perimeterFt, 2)), "ft " + "OR", str(round(perimeterYd, 2)), "yards") # Returns Perimeter in mm, cm and m

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

                #PERIMETER
                # if (measureSelect == "01" or measureSelect == "1"):
                #     perimeter = ((length * 2) + (width * 2))
                #     perimeterCm = (perimeter / 10)
                #     perimeterM = (perimeter / 1000)
                #     print("\nThe Volume is:", str(round(perimeter, 2)), "mm3 " + "OR", str (round(perimeterCm, 2)), "cm3 " + "OR", str(round(perimeterM, 2)), "m3") # Returns Perimeter in mm, cm and m

                #AREA
                # if (measureSelect == "02" or measureSelect == "2"):
                #     area = (length * width)
                #     areaCm = (area / 100)
                #     areaM = (areaCm / 10000)
                #     print("\nThe Area is:", str(round(area, 2)), "mm2 " + "OR", str (round(areaCm, 2)), "cm2 " + "OR", str(round(areaM, 2)), "m2") #Returns Area in mm2, cm2 and m2

                # #VOLUME
                # elif (measureSelect == "03" or measureSelect == "3"):
                #     volume = (length * width * depth)
                #     volumeCm = (volume / 1000)
                #     volumeM = (volumeCm / 1000000)
                #     print("\nThe Volume is:", str(round(volume, 2)), "mm3 " + "OR", str (round(volumeCm, 2)), "cm3 " + "OR", str(round(volumeM, 2)), "m3") #Returns Volume in mm3, cm3 and m3


            back = input("\nGo back to the main menu? (y/n) ")

            if back == "y":
                continue
            else:
                break

    # Weight
    elif oper == "14":

        # The user picks what weight they want to convert
        print("\nChoose what weight you want to convert.\n\n01 - Grams\n02 - Kilograms\n03 - Ounces\n04 - Pounds\n05 - Stones")

        # The variable that saves the users weight choice
        weightSelect = input("\nSelect an option from the menu: ")

        if weightSelect == "01" or weightSelect == "1":
            grams = float(input("\nEnter the number of grams (G): "))
            kilograms = (grams / 1000)
            ounces = (grams / 28.34952)
            pounds = (grams / 453.592)
            stones = (grams / 6350.293)
            print("\n", str(round(grams, 0)), "g =", str(round(kilograms, 4)), "kg " + "OR",  str(round(ounces, 2)), "oz " + "OR", str(round(pounds, 3)), "lbs " + "OR", str(round(stones, 4)), "stones") # Returns Grams in Kilos, Ounces, Pounds and Stones

        elif weightSelect == "02" or weightSelect == "2":
            kilograms = float(input("\nEnter the number of Kilograms (K): "))
            grams = (kilograms * 1000)
            ounces = (kilograms * 35.274)
            pounds = (kilograms * 2.20462)
            stones = (kilograms * 0.157473)
            print("\n", str(round(kilograms, 0)), "kg =", str(round(grams, 2)), "g " + "OR", str(round(ounces, 2)), "oz " + "OR", str(round(pounds, 2)), "lbs " + "OR", str(round(stones, 2)), "stones")

        elif weightSelect == "03" or weightSelect == "3":
            ounces = float(input("\nEnter the number of ounces (O): "))
            grams = (ounces * 28.3495)
            kilograms = (ounces / 35.274)
            pounds = (ounces / 16)
            stones = (ounces / 2243)
            print("\n", str(round(ounces, 0)), "oz =", str(round(grams, 2)), "g " + "OR", str(round(kilograms, 2)), "kg " + "OR", str(round(pounds, 2)), "lbs " + "OR", str(round(stones, 4)), "stones")

        elif weightSelect == "04" or weightSelect == "4":
            pounds = float(input("\nEnter the number of pounds (P): "))
            grams = (pounds * 453.592)
            kilograms = (pounds / 2.20462)
            ounces = (pounds * 16)
            stones = (pounds / 14)
            print("\n", str(round(pounds, 0)), "lbs =", str(round(grams, 2)), "g " + "OR", str(round(kilograms, 2)), "kg " + "OR", str(round(ounces, 2)), "oz " + "OR", str(round(stones, 2)), "stones")

        elif weightSelect == "05" or weightSelect == "5":
            stones = float(input("\nEnter the number in stones (S): "))
            grams = (stones * 6350.293)
            kilograms = (stones * 6.350293)
            ounces = (stones * 224)
            pounds = (stones * 14)
            print("\n", str(round(stones, 0)), "stones =", str(round(grams, 2)), "g " + "OR", str(round(kilograms, 2)), "kg " + "OR", str(round(ounces, 2)), "oz " + "OR", str(round(pounds, 2)), "lbs")


        back = input("\nGo back to the main menu? (y/n) ")

        if back == "y":
            continue
        else:
            break

    # Handling invalid options
    else:
        print("That option is invalid!\n")
        continue
