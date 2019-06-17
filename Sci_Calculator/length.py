from measurement.measures import Distance, Area, Volume

print(
        "\nChoose what unit you want to convert.\n\n01 - MM\n02 - CM\n03 - M\n04 - In\n05 - Ft\n06 - Yd")

unitSelect = input("\nSelect a unit from the menu: ")

if unitSelect != 0:

    print("\nChoose what you want to convert.\n\n01 - Length\n02 - Perimeter\
        \n03 - Area\n04 - Volume")

    measureSelect = input("\nSelect an option from the menu: ")

    if (unitSelect == "01" or unitSelect == "1") and measureSelect == "01"\
    or measureSelect == "1":
        length = float(input("\nPlease enter the length in mm: "))

        mms = Distance(mm = length)
        cms = (mms.cm)
        ms = (mms.m)
        lYards = (mms.yd)
        lFoot = ((lYards % 1) * 3)
        lFeet = (mms.ft)
        lInches = ((lFeet % 1) * 12)

        print("\nLength in centimeters:", cms)
        print("\nLength in meters:", ms)
        print("\nLength in inches:", round(mms.inch, 2), "in")
        print("\nLength in feet & inches:", int(mms.ft), "ft ", round(lInches, 2), "in")
        print("\nLength in yards:", int(mms.yd), "yd ", int(lFoot), "ft ", round(lInches, 2), "in")


# length = float(input("\nPlease enter the length in mm: "))

# mms = Distance(mm = length)
# lYards = (mms.yd)
# lFoot = ((lYards % 1) * 3)
# lFeet = (mms.ft)
# lInches = ((lFeet % 1) * 12)

# print("\nLength in centimeters:", round(mms.cm, 2), "cm")
# print("\nLength in meters:", round(mms.m, 2), "m")
# print("\nLength in inches:", round(mms.inch, 2), "in")
# print("\nLength in feet & inches:", int(mms.ft), "ft ", round(lInches, 2), "in")
# print("\nLength in yards:", int(mms.yd), "yd ", int(lFoot), "ft ", round(lInches, 2), "in")


# length = input("\nPlease enter the length in mm: ")
# width = input("\nPlease enter the width in mm: ")

# mms = Distance(mm = length)
# lYards = (mms.yd)
# lFoot = ((lYards % 1) * 3)
# lFeet = (mms.ft)
# lInches = ((lFeet % 1) * 12)
# wmms = Distance(mm = width)
# wYards = (wmms.yd)
# wFoot = ((wYards % 1) * 3)
# wFeet = (wmms.ft)
# wInches = ((wFeet % 1) * 12)

# perimeterIn = ((mms.inch * 2) + (wmms.inch * 2))
# perimeterFt = ((mms.ft * 2) + (wmms.ft * 2))
# perimeterFtIn = ((perimeterFt % 1) * 12)
# print("\nPerimeter in millimeters:", ((mms * 2) + (wmms * 2)))
# print("\nPerimeter in centimeters:", ((mms.cm * 2) + (wmms.cm * 2)), "cm")
# print("\nPerimeter in meters:", ((mms.m * 2) + (wmms.m * 2)), "m")
# print("\nPerimeter in inches:", round(perimeterIn, 2), "in")
# print("\nPerimeter in feet & inches:", int(perimeterFt), "ft", round(perimeterFtIn, 2), "in")