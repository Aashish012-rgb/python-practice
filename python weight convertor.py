#python weight converter
weight = float(input("Enter your weight:"))
unit = input("kilograms or Pounds?(K or L):")

if unit == "K":
    weight = weight*2.205
    unit ="Lb's."
elif unit == "L":
    weight = weight /2.205
    unit = "Kg's."
    print(f"your weight is :{round(weight, 1)} {unit}")
else:
    print(f"{unit}is not the valid input")

