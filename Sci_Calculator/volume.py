from measurement.measures import Volume

vLength = float(input("\nEnter the length in mm: "))
vWidth = float(input("\nEnter the width in mm: "))
vHeight = float(input("\nEnter the height in mm: "))

volume = (vLength * vWidth * vHeight)

vmms = Volume(cubic_millimeter = volume)
vFoot = (vmms.cubic_foot)
vInch = ((vFoot % 1) * 12)

print("\nVolume in Millimeters:", round(vmms.cubic_millimeter, 2), "mm3")
print("\nVolume in Centimeters:", round(vmms.cubic_centimeter, 2), "cm3")
print("\nVolume in Meters:", round(vmms.cubic_meter, 2), "m3")
print("\nVolume in Milliliters:", round(vmms.ml, 2), "ml")
print("\nVolume in Centiliters:", round(vmms.cl, 2), "cl")
print("\nVolume in Litres:", round(vmms.l, 2), "l")
print("\nVolume in Inches:", round(vmms.cubic_inch, 2), "in3")
print("\nVolume in Feet & Inches:", int(vmms.cubic_foot), "ft3 ", round(vInch, 2), "in3")
