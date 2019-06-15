from measurement.measures import Weight

weight = float(input("\nEnter the weight in grams (G) you want to convert: "))

gms = Weight(g = weight)
stones = (gms.stone)
lbs = ((stones % 1) * 14)

# print("\nWeight in grams:", gms)
print("\nWeight in kilograms:", round(gms.kg, 2), "kg")
print("\nWeight in ounces:", round(gms.oz, 1), "oz")
print("\nWeight in pounds:", round(gms.lb, 1), "lbs")
print("\nWeight in stones & pounds:", int(gms.stone), "st ", round(lbs, 1), "lbs")

